"""
DermaScan Utilities
Image text extraction and ingredient parsing.
"""

import re
from PIL import Image
import io
import ssl
import easyocr
import numpy as np

# SSL fix for model download
ssl._create_default_https_context = ssl._create_unverified_context

# Load OCR model once
reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image: Image.Image) -> str:
    """
    Extract text from uploaded product image using EasyOCR.
    """
    try:
        # Convert PIL image to numpy array
        img = np.array(image)

        # Read text
        result = reader.readtext(img, detail=0)

        text = " ".join(result)

        if text.strip():
            return text.strip()
        else:
            return _fallback_message()

    except Exception:
        return _fallback_message()


def _fallback_message():
    return """Tesseract OCR not installed on this system.

To use image OCR:
1. Install tesseract: sudo apt-get install tesseract-ocr (Linux) or brew install tesseract (Mac)
2. Install pytesseract: pip install pytesseract

Alternatively, please COPY and PASTE the ingredients list manually in the 'Manual Input' tab.

Example ingredient list to try:
Water, Glycerin, Niacinamide, Dimethicone, Phenoxyethanol, Fragrance, Retinol, Salicylic Acid, Titanium Dioxide, Zinc Oxide, Hyaluronic Acid, Vitamin C, Tocopherol, Ceramide NP, Centella Asiatica Extract"""


def parse_ingredients_text(text: str) -> list:
    """
    Parse raw ingredients text into a clean list.
    Handles various formats: comma-separated, newline-separated, bulleted, etc.
    """
    if not text or not text.strip():
        return []

    # Remove common label prefixes
    prefixes_to_remove = [
        r"ingredients?[\s:]+",
        r"inci[\s:]+",
        r"composition[\s:]+",
        r"contains?[\s:]+",
        r"ingrédients?[\s:]+",
    ]
    cleaned = text.strip()
    for prefix in prefixes_to_remove:
        cleaned = re.sub(prefix, "", cleaned, flags=re.IGNORECASE)

    # Remove parenthetical amounts/percentages
    cleaned = re.sub(r'\(\s*[\d.]+\s*%?\s*\)', '', cleaned)
    
    # Normalize separators
    # Replace newlines, semicolons, | with commas
    cleaned = re.sub(r'[\n\r;|]+', ',', cleaned)
    
    # Remove asterisks and other common annotation markers
    cleaned = re.sub(r'[\*†‡§¶#][\w\s]*$', '', cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r'[\*†‡§¶#]', '', cleaned)
    
    # Remove trailing notes/disclaimer text
    disclaimer_patterns = [
        r'\bfor\s+external\s+use\s+only.*$',
        r'\bkeep\s+out\s+of\s+reach.*$',
        r'\bmanufactured\s+by.*$',
        r'\bdistributed\s+by.*$',
        r'\bnet\s+wt.*$',
        r'\bwt\.\s*\d.*$',
    ]
    for pattern in disclaimer_patterns:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE | re.DOTALL)

    # Split by comma
    raw_ingredients = [i.strip() for i in cleaned.split(',')]

    # Clean each ingredient
    final_ingredients = []
    for ing in raw_ingredients:
        # Remove leading/trailing punctuation except hyphens in names
        ing = ing.strip(' .\t-_')
        
        # Skip empty, very short, or obviously non-ingredient tokens
        if not ing or len(ing) < 2:
            continue
        
        # Skip pure numbers
        if re.match(r'^[\d\s.%]+$', ing):
            continue
        
        # Skip common non-ingredient phrases
        skip_patterns = [
            r'^may\s+contain',
            r'^ci\s*\d{4,}',  # color index numbers handled separately
            r'^\d+\s*(mg|ml|g|oz|%)',
            r'^www\.',
            r'^\+?\d[\d\s\-\(\)]+$',  # phone numbers
        ]
        skip = False
        for pattern in skip_patterns:
            if re.match(pattern, ing, re.IGNORECASE):
                skip = True
                break
        if skip:
            continue
        
        # Limit length (ingredient names shouldn't be > 80 chars)
        if len(ing) > 80:
            ing = ing[:80]
        
        # Capitalize first letter only for display
        final_ingredients.append(ing)

    # Remove exact duplicates preserving order
    seen = set()
    unique = []
    for ing in final_ingredients:
        key = ing.lower().strip()
        if key not in seen:
            seen.add(key)
            unique.append(ing)

    return unique


def get_product_category_guess(ingredients: list) -> str:
    """Guess product type from ingredient profile."""
    ing_lower = [i.lower() for i in ingredients]
    
    has_spf = any(x in ing_lower for x in ["titanium dioxide", "zinc oxide", "oxybenzone", "avobenzone"])
    has_retinol = "retinol" in ing_lower
    has_aha_bha = any(x in ing_lower for x in ["glycolic acid", "salicylic acid", "lactic acid"])
    has_heavy_emollient = any(x in ing_lower for x in ["shea butter", "beeswax", "carnauba"])
    
    if has_spf:
        return "☀️ Sunscreen / SPF Product"
    elif has_retinol:
        return "🌙 Retinol / Anti-aging Treatment"
    elif has_aha_bha:
        return "✨ Chemical Exfoliant / Toner"
    elif has_heavy_emollient:
        return "💧 Moisturizer / Body Cream"
    else:
        return "🧴 Skincare Product"
