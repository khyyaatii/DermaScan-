"""
DermaScan Ingredient Database
Comprehensive INCI ingredient data with risk levels, EWG scores, functions, and descriptions.
"""

RISK_LEVELS = ["Safe", "Low", "Moderate", "High", "Danger"]

CATEGORIES = [
    "Humectant", "Emollient", "Emulsifier", "Preservative", "Surfactant",
    "Active", "Antioxidant", "UV Filter", "Fragrance", "Colorant",
    "Thickener", "Chelating Agent", "Skin Conditioning", "Penetration Enhancer",
    "Anti-aging", "Exfoliant", "Brightening", "Soothing", "Antimicrobial", "pH Adjuster"
]

INGREDIENT_DATABASE = {
    # ─── Water & Solvents ──────────────────────────────────────────────────────
    "water": {
        "risk": "Safe", "ewg_score": 1, "category": "Solvent",
        "function": "Solvent / Base",
        "description": "Universal solvent and base for most cosmetic formulas. Completely safe.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All"], "avoid_for": []
    },
    "aqua": {
        "risk": "Safe", "ewg_score": 1, "category": "Solvent",
        "function": "Solvent / Base",
        "description": "INCI name for water. Completely safe.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All"], "avoid_for": []
    },
    "butylene glycol": {
        "risk": "Low", "ewg_score": 1, "category": "Humectant",
        "function": "Humectant / Solvent",
        "description": "Lightweight humectant that draws moisture into skin. Also enhances penetration of other ingredients.",
        "concern": "May cause mild irritation in very high concentrations.",
        "cosdna_score": 1, "good_for": ["Dry", "Normal"], "avoid_for": ["Sensitive"]
    },
    "propylene glycol": {
        "risk": "Moderate", "ewg_score": 3, "category": "Humectant",
        "function": "Humectant / Solvent",
        "description": "Attracts water to skin, but can cause irritation or allergic reactions in some people.",
        "concern": "Known skin irritant for sensitive skin. Possible allergen.",
        "cosdna_score": 3, "good_for": ["Oily"], "avoid_for": ["Sensitive", "Eczema"]
    },
    "ethoxydiglycol": {
        "risk": "Low", "ewg_score": 1, "category": "Solvent",
        "function": "Solvent / Penetration Enhancer",
        "description": "Solvent that helps ingredients penetrate skin more effectively.",
        "concern": "", "cosdna_score": 1, "good_for": ["All"], "avoid_for": []
    },

    # ─── Humectants ────────────────────────────────────────────────────────────
    "glycerin": {
        "risk": "Safe", "ewg_score": 1, "category": "Humectant",
        "function": "Humectant / Skin Conditioner",
        "description": "Excellent moisture-attracting ingredient derived from plants or synthetically. Suitable for all skin types.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Dry", "Sensitive"], "avoid_for": []
    },
    "hyaluronic acid": {
        "risk": "Safe", "ewg_score": 1, "category": "Humectant",
        "function": "Humectant / Anti-aging",
        "description": "Powerful humectant that can hold up to 1000x its weight in water. Plumps and hydrates skin.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Dry", "Mature", "Combination"], "avoid_for": []
    },
    "sodium hyaluronate": {
        "risk": "Safe", "ewg_score": 1, "category": "Humectant",
        "function": "Humectant / Anti-aging",
        "description": "Salt form of hyaluronic acid with smaller molecular weight for deeper penetration.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All"], "avoid_for": []
    },
    "panthenol": {
        "risk": "Safe", "ewg_score": 1, "category": "Humectant",
        "function": "Humectant / Skin Conditioner",
        "description": "Pro-vitamin B5 that moisturizes, soothes, and promotes skin healing.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Sensitive", "Dry"], "avoid_for": []
    },
    "urea": {
        "risk": "Low", "ewg_score": 1, "category": "Humectant",
        "function": "Humectant / Exfoliant",
        "description": "Natural component of skin's NMF. Highly effective moisturizer and mild exfoliant at higher concentrations.",
        "concern": "High concentrations may cause slight tingling.", "cosdna_score": 1,
        "good_for": ["Dry", "Mature"], "avoid_for": []
    },
    "sorbitol": {
        "risk": "Safe", "ewg_score": 1, "category": "Humectant",
        "function": "Humectant / Skin Conditioner",
        "description": "Sugar alcohol that attracts and retains moisture in skin.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Dry"], "avoid_for": []
    },
    "aloe barbadensis leaf juice": {
        "risk": "Safe", "ewg_score": 1, "category": "Soothing",
        "function": "Soothing / Humectant",
        "description": "Aloe vera gel – calming, anti-inflammatory, and lightly moisturizing. Excellent for sensitive skin.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Sensitive", "Acne-Prone"], "avoid_for": []
    },

    # ─── Actives ───────────────────────────────────────────────────────────────
    "niacinamide": {
        "risk": "Safe", "ewg_score": 1, "category": "Active",
        "function": "Brightening / Anti-aging / Pore-minimizing",
        "description": "Vitamin B3 – brightens skin, reduces pores, controls oil, and strengthens skin barrier. One of the best-studied skincare actives.",
        "concern": "Very high concentrations (>10%) may cause flushing.", "cosdna_score": 0,
        "good_for": ["All", "Oily", "Acne-Prone", "Combination", "Mature"], "avoid_for": []
    },
    "retinol": {
        "risk": "Moderate", "ewg_score": 5, "category": "Anti-aging",
        "function": "Anti-aging / Cell Renewal",
        "description": "Gold-standard anti-aging vitamin A derivative. Stimulates collagen and accelerates cell turnover.",
        "concern": "Can cause irritation, peeling, and photosensitivity. Not safe during pregnancy.", "cosdna_score": 3,
        "good_for": ["Mature", "Acne-Prone"], "avoid_for": ["Sensitive", "Pregnant"]
    },
    "retinyl palmitate": {
        "risk": "High", "ewg_score": 7, "category": "Anti-aging",
        "function": "Anti-aging / Skin Conditioner",
        "description": "Ester form of Vitamin A. Concerns exist about potential tumor promotion when used in sun-exposed products.",
        "concern": "May enhance skin tumors and lesions in the presence of sunlight. Avoid in daytime products.", "cosdna_score": 4,
        "good_for": ["Mature"], "avoid_for": ["Sensitive", "Pregnant"]
    },
    "salicylic acid": {
        "risk": "Low", "ewg_score": 3, "category": "Exfoliant",
        "function": "BHA Exfoliant / Anti-acne",
        "description": "Beta-hydroxy acid (BHA) that exfoliates inside pores. Excellent for acne and blackheads.",
        "concern": "Can cause irritation and photosensitivity. Use SPF when using BHAs.", "cosdna_score": 2,
        "good_for": ["Oily", "Acne-Prone", "Combination"], "avoid_for": ["Dry", "Sensitive", "Pregnant"]
    },
    "glycolic acid": {
        "risk": "Low", "ewg_score": 2, "category": "Exfoliant",
        "function": "AHA Exfoliant / Brightening",
        "description": "Most popular alpha-hydroxy acid. Exfoliates dead skin cells, brightens and smooths.",
        "concern": "Can cause irritation and sun sensitivity. Always use SPF.", "cosdna_score": 2,
        "good_for": ["Normal", "Oily", "Mature"], "avoid_for": ["Sensitive", "Dry"]
    },
    "lactic acid": {
        "risk": "Low", "ewg_score": 2, "category": "Exfoliant",
        "function": "AHA Exfoliant / Humectant",
        "description": "Gentler AHA that exfoliates while also moisturizing. Better tolerated than glycolic acid.",
        "concern": "Mild photosensitivity. Use SPF.", "cosdna_score": 2,
        "good_for": ["Normal", "Dry", "Sensitive"], "avoid_for": []
    },
    "vitamin c": {
        "risk": "Safe", "ewg_score": 1, "category": "Brightening",
        "function": "Antioxidant / Brightening / Anti-aging",
        "description": "Powerful antioxidant that brightens skin, reduces hyperpigmentation, and boosts collagen production.",
        "concern": "Pure vitamin C (L-ascorbic acid) can oxidize quickly and cause irritation at high concentrations.", "cosdna_score": 1,
        "good_for": ["All", "Mature", "Hyperpigmentation"], "avoid_for": []
    },
    "ascorbic acid": {
        "risk": "Low", "ewg_score": 1, "category": "Brightening",
        "function": "Antioxidant / Brightening",
        "description": "Pure vitamin C. Highly effective but unstable. Best at pH below 3.5.",
        "concern": "Irritating at high concentrations. Oxidizes rapidly.", "cosdna_score": 1,
        "good_for": ["Normal", "Mature"], "avoid_for": ["Sensitive"]
    },
    "kojic acid": {
        "risk": "Moderate", "ewg_score": 4, "category": "Brightening",
        "function": "Skin Brightener / Tyrosinase Inhibitor",
        "description": "Derived from fungi; inhibits melanin production. Used for hyperpigmentation.",
        "concern": "Can cause contact dermatitis and sensitization. Regulatory limits vary by country.", "cosdna_score": 3,
        "good_for": ["Hyperpigmentation"], "avoid_for": ["Sensitive"]
    },
    "hydroquinone": {
        "risk": "High", "ewg_score": 8, "category": "Brightening",
        "function": "Skin Bleaching Agent",
        "description": "Prescription-strength skin bleacher. Highly effective but with significant safety concerns.",
        "concern": "Linked to ochronosis (skin discoloration), potential carcinogen. Banned in EU cosmetics. Requires medical supervision.", "cosdna_score": 5,
        "good_for": [], "avoid_for": ["Sensitive", "All"]
    },
    "azelaic acid": {
        "risk": "Safe", "ewg_score": 1, "category": "Active",
        "function": "Anti-acne / Brightening / Anti-inflammatory",
        "description": "Naturally occurring acid that fights acne, reduces redness, and brightens skin gently.",
        "concern": "", "cosdna_score": 1,
        "good_for": ["Acne-Prone", "Sensitive", "Rosacea"], "avoid_for": []
    },

    # ─── Emollients & Oils ─────────────────────────────────────────────────────
    "dimethicone": {
        "risk": "Low", "ewg_score": 2, "category": "Emollient",
        "function": "Emollient / Skin Protectant",
        "description": "Silicone that creates a smooth, protective film on skin. Non-comedogenic at standard concentrations.",
        "concern": "May cause breakouts in very acne-prone skin. Environmental persistence concerns.", "cosdna_score": 1,
        "good_for": ["Dry", "Normal", "Mature"], "avoid_for": ["Acne-Prone"]
    },
    "cyclopentasiloxane": {
        "risk": "Moderate", "ewg_score": 4, "category": "Emollient",
        "function": "Emollient / Carrier",
        "description": "Volatile silicone used for silky texture. Evaporates after application.",
        "concern": "Endocrine disruption concerns. Restricted in wash-off products in EU.", "cosdna_score": 3,
        "good_for": [], "avoid_for": ["Sensitive"]
    },
    "cetyl alcohol": {
        "risk": "Low", "ewg_score": 1, "category": "Emollient",
        "function": "Emollient / Emulsifier / Thickener",
        "description": "Fatty alcohol (not drying). Conditions skin and helps formulas feel smooth.",
        "concern": "Rare sensitization in some individuals.", "cosdna_score": 1,
        "good_for": ["Dry", "Normal", "Mature"], "avoid_for": []
    },
    "stearic acid": {
        "risk": "Safe", "ewg_score": 1, "category": "Emollient",
        "function": "Emollient / Emulsifier",
        "description": "Fatty acid that softens skin and helps stabilize emulsions.",
        "concern": "Mildly comedogenic for acne-prone skin.", "cosdna_score": 2,
        "good_for": ["Dry", "Mature"], "avoid_for": ["Acne-Prone"]
    },
    "jojoba oil": {
        "risk": "Safe", "ewg_score": 1, "category": "Emollient",
        "function": "Emollient / Skin Conditioning",
        "description": "Technically a wax ester, very similar to skin's natural sebum. Non-comedogenic and balancing.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Oily", "Acne-Prone"], "avoid_for": []
    },
    "rosehip oil": {
        "risk": "Safe", "ewg_score": 1, "category": "Emollient",
        "function": "Emollient / Antioxidant / Anti-aging",
        "description": "Rich in linoleic acid and vitamin A precursors. Helps with scarring, aging, and dryness.",
        "concern": "May be comedogenic for some.", "cosdna_score": 1,
        "good_for": ["Dry", "Mature", "Normal"], "avoid_for": ["Acne-Prone"]
    },
    "squalane": {
        "risk": "Safe", "ewg_score": 1, "category": "Emollient",
        "function": "Emollient / Antioxidant",
        "description": "Plant-derived (olive/sugarcane) oil that mimics natural sebum. Lightweight, non-comedogenic, and excellent for all skin types.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All"], "avoid_for": []
    },
    "shea butter": {
        "risk": "Safe", "ewg_score": 1, "category": "Emollient",
        "function": "Emollient / Skin Conditioner",
        "description": "Rich nut butter with anti-inflammatory properties. Deeply moisturizing.",
        "concern": "May be comedogenic for some acne-prone skin.", "cosdna_score": 0,
        "good_for": ["Dry", "Mature", "Sensitive"], "avoid_for": ["Acne-Prone"]
    },
    "argan oil": {
        "risk": "Safe", "ewg_score": 1, "category": "Emollient",
        "function": "Emollient / Antioxidant",
        "description": "'Liquid gold' – rich in vitamin E and fatty acids. Anti-aging and nourishing.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["Dry", "Mature", "Normal"], "avoid_for": []
    },
    "mineral oil": {
        "risk": "Low", "ewg_score": 2, "category": "Emollient",
        "function": "Emollient / Occlusive",
        "description": "Petroleum-derived occlusive that locks in moisture. Generally safe but controversial.",
        "concern": "Concerns about comedogenicity and environmental impact. Refined grades are safe.", "cosdna_score": 1,
        "good_for": ["Dry"], "avoid_for": ["Acne-Prone"]
    },
    "petrolatum": {
        "risk": "Low", "ewg_score": 2, "category": "Emollient",
        "function": "Occlusive / Skin Protectant",
        "description": "Petroleum jelly. Highly effective occlusive barrier ingredient.",
        "concern": "If not fully refined, may contain PAH contaminants. Refined USP grade is safe.", "cosdna_score": 1,
        "good_for": ["Dry", "Sensitive", "Eczema"], "avoid_for": ["Acne-Prone"]
    },

    # ─── Preservatives ─────────────────────────────────────────────────────────
    "phenoxyethanol": {
        "risk": "Low", "ewg_score": 4, "category": "Preservative",
        "function": "Preservative / Antimicrobial",
        "description": "Common synthetic preservative. Effective against bacteria and fungi at typical concentrations (max 1%).",
        "concern": "Can irritate skin, eyes, and respiratory tract at high concentrations. Generally safe at EU-approved levels.", "cosdna_score": 2,
        "good_for": ["Normal", "Oily"], "avoid_for": ["Sensitive", "Infant"]
    },
    "parabens": {
        "risk": "High", "ewg_score": 7, "category": "Preservative",
        "function": "Preservative / Antimicrobial",
        "description": "Group of synthetic preservatives (methylparaben, ethylparaben, etc.). Effective but controversial.",
        "concern": "Endocrine disrupting properties. Found in breast tumor tissue. Banned for certain parabens in EU.", "cosdna_score": 4,
        "good_for": [], "avoid_for": ["Sensitive", "Pregnant", "All"]
    },
    "methylparaben": {
        "risk": "Moderate", "ewg_score": 4, "category": "Preservative",
        "function": "Preservative / Antimicrobial",
        "description": "Most common paraben preservative. Low toxicity among parabens.",
        "concern": "Weak estrogenic activity. Concerns during pregnancy. EWG rates as moderate concern.", "cosdna_score": 2,
        "good_for": [], "avoid_for": ["Sensitive", "Pregnant"]
    },
    "propylparaben": {
        "risk": "High", "ewg_score": 7, "category": "Preservative",
        "function": "Preservative / Antimicrobial",
        "description": "Paraben preservative with stronger estrogenic activity.",
        "concern": "Stronger endocrine disruptor than methylparaben. Banned in Denmark for children's products.", "cosdna_score": 4,
        "good_for": [], "avoid_for": ["Sensitive", "Pregnant", "All"]
    },
    "formaldehyde": {
        "risk": "Danger", "ewg_score": 10, "category": "Preservative",
        "function": "Preservative",
        "description": "Known human carcinogen. Banned in EU cosmetics at concentrations > 0.001%.",
        "concern": "CONFIRMED CARCINOGEN. Causes skin sensitization, allergic reactions, and cancer with chronic exposure.", "cosdna_score": 5,
        "good_for": [], "avoid_for": ["All"]
    },
    "imidazolidinyl urea": {
        "risk": "Moderate", "ewg_score": 5, "category": "Preservative",
        "function": "Formaldehyde Releaser / Preservative",
        "description": "Preservative that releases formaldehyde over time to kill bacteria.",
        "concern": "Formaldehyde-releasing preservative. Potential sensitizer. Avoid if formaldehyde-sensitive.", "cosdna_score": 3,
        "good_for": [], "avoid_for": ["Sensitive"]
    },
    "dmdm hydantoin": {
        "risk": "High", "ewg_score": 7, "category": "Preservative",
        "function": "Formaldehyde Releaser / Preservative",
        "description": "Commonly used formaldehyde-releasing preservative.",
        "concern": "Releases formaldehyde. Strong sensitizer. Subject of class action lawsuits in hair products.", "cosdna_score": 4,
        "good_for": [], "avoid_for": ["Sensitive", "All"]
    },
    "benzalkonium chloride": {
        "risk": "Moderate", "ewg_score": 5, "category": "Preservative",
        "function": "Antimicrobial / Preservative",
        "description": "Quaternary ammonium compound used as preservative and antimicrobial.",
        "concern": "Known irritant and possible allergen. Can damage skin barrier.", "cosdna_score": 3,
        "good_for": [], "avoid_for": ["Sensitive", "Eczema"]
    },
    "ethylhexylglycerin": {
        "risk": "Low", "ewg_score": 1, "category": "Preservative",
        "function": "Preservative Booster / Humectant",
        "description": "Used to boost preservative efficacy. Also acts as skin conditioner.",
        "concern": "Low irritation risk.", "cosdna_score": 1,
        "good_for": ["All"], "avoid_for": []
    },
    "sodium benzoate": {
        "risk": "Low", "ewg_score": 3, "category": "Preservative",
        "function": "Preservative / Antimicrobial",
        "description": "Used as preservative in acidic formulations.",
        "concern": "Can form benzene when combined with ascorbic acid. Mild irritant in some cases.", "cosdna_score": 2,
        "good_for": [], "avoid_for": ["Sensitive"]
    },

    # ─── Surfactants ───────────────────────────────────────────────────────────
    "sodium lauryl sulfate": {
        "risk": "High", "ewg_score": 7, "category": "Surfactant",
        "function": "Surfactant / Foaming Agent",
        "description": "Very aggressive cleansing surfactant. Strips skin's natural oils.",
        "concern": "Disrupts skin barrier, causes irritation, dehydration, and may trigger sensitization. Strong allergen.", "cosdna_score": 5,
        "good_for": [], "avoid_for": ["Sensitive", "Dry", "Eczema", "All"]
    },
    "sodium laureth sulfate": {
        "risk": "Moderate", "ewg_score": 4, "category": "Surfactant",
        "function": "Surfactant / Foaming Agent",
        "description": "Milder version of SLS, but still quite stripping. May contain 1,4-dioxane as contaminant.",
        "concern": "Potential 1,4-dioxane contamination (carcinogen). Skin irritant. Milder than SLS but still concerning.", "cosdna_score": 3,
        "good_for": [], "avoid_for": ["Sensitive", "Dry", "Eczema"]
    },
    "cocamidopropyl betaine": {
        "risk": "Low", "ewg_score": 3, "category": "Surfactant",
        "function": "Surfactant / Foam Booster",
        "description": "Amphoteric surfactant derived from coconut oil. Much gentler than SLS.",
        "concern": "Can cause skin sensitization in some individuals.", "cosdna_score": 2,
        "good_for": ["Normal", "Oily"], "avoid_for": ["Sensitive"]
    },
    "sodium cocoyl isethionate": {
        "risk": "Low", "ewg_score": 1, "category": "Surfactant",
        "function": "Gentle Surfactant / Skin Conditioner",
        "description": "Very gentle coconut-derived surfactant. Cleanses without stripping.",
        "concern": "", "cosdna_score": 1,
        "good_for": ["All", "Sensitive", "Dry"], "avoid_for": []
    },

    # ─── UV Filters ────────────────────────────────────────────────────────────
    "titanium dioxide": {
        "risk": "Low", "ewg_score": 2, "category": "UV Filter",
        "function": "Physical UV Filter / UVB",
        "description": "Mineral sunscreen ingredient. Provides broad-spectrum UV protection. Excellent safety profile.",
        "concern": "Inhalation risk with nano-particles in sprays. Generally safe in topical application.", "cosdna_score": 1,
        "good_for": ["All", "Sensitive"], "avoid_for": []
    },
    "zinc oxide": {
        "risk": "Low", "ewg_score": 2, "category": "UV Filter",
        "function": "Physical UV Filter / UVA+UVB",
        "description": "Broad-spectrum mineral UV filter. Also anti-inflammatory and soothing.",
        "concern": "May leave white cast at higher concentrations. Nano-form inhalation concerns.", "cosdna_score": 1,
        "good_for": ["All", "Sensitive", "Acne-Prone"], "avoid_for": []
    },
    "oxybenzone": {
        "risk": "High", "ewg_score": 8, "category": "UV Filter",
        "function": "Chemical UV Filter / UVA+UVB",
        "description": "Chemical UV filter. Very effective but significant safety concerns.",
        "concern": "Endocrine disruptor. Penetrates skin. Found in blood, urine, and breast milk. Coral reef damage. Banned in Hawaii.", "cosdna_score": 4,
        "good_for": [], "avoid_for": ["Sensitive", "Pregnant", "All"]
    },
    "avobenzone": {
        "risk": "Moderate", "ewg_score": 5, "category": "UV Filter",
        "function": "Chemical UV Filter / UVA",
        "description": "Chemical UVA filter. Can degrade in sunlight and produce free radicals.",
        "concern": "Degrades without photostabilizers. Possible hormone disruptor. Can irritate sensitive skin.", "cosdna_score": 3,
        "good_for": [], "avoid_for": ["Sensitive"]
    },
    "octinoxate": {
        "risk": "High", "ewg_score": 6, "category": "UV Filter",
        "function": "Chemical UV Filter / UVB",
        "description": "Chemical UVB filter.",
        "concern": "Endocrine disruptor. Detected in human blood and breast milk. Coral reef damage. Banned in some areas.", "cosdna_score": 3,
        "good_for": [], "avoid_for": ["Sensitive", "Pregnant"]
    },
    "octocrylene": {
        "risk": "Moderate", "ewg_score": 4, "category": "UV Filter",
        "function": "Chemical UV Filter / UVA+UVB",
        "description": "Photostabilizer and UV filter. Helps stabilize avobenzone.",
        "concern": "Accumulates in environment. Possible bioaccumulator. Skin sensitizer.", "cosdna_score": 2,
        "good_for": [], "avoid_for": ["Sensitive"]
    },

    # ─── Fragrances ────────────────────────────────────────────────────────────
    "fragrance": {
        "risk": "High", "ewg_score": 8, "category": "Fragrance",
        "function": "Fragrance / Masking",
        "description": "Generic term that can hide 3,000+ chemicals. Major allergen and irritant.",
        "concern": "Undisclosed mixture. Major allergen. Contains potential carcinogens, endocrine disruptors, and sensitizers. Avoid if sensitive.", "cosdna_score": 4,
        "good_for": [], "avoid_for": ["Sensitive", "Eczema", "Rosacea"]
    },
    "parfum": {
        "risk": "High", "ewg_score": 8, "category": "Fragrance",
        "function": "Fragrance / Masking",
        "description": "European INCI for 'fragrance.' Contains undisclosed mixture of chemicals.",
        "concern": "Same as 'fragrance' – undisclosed potentially harmful chemicals. Top allergen.", "cosdna_score": 4,
        "good_for": [], "avoid_for": ["Sensitive", "Eczema", "Rosacea"]
    },
    "linalool": {
        "risk": "Moderate", "ewg_score": 4, "category": "Fragrance",
        "function": "Fragrance Component",
        "description": "Natural fragrance component found in lavender. One of 26 designated EU allergens.",
        "concern": "EU required allergen disclosure. Sensitizer especially when oxidized.", "cosdna_score": 3,
        "good_for": [], "avoid_for": ["Sensitive"]
    },
    "limonene": {
        "risk": "Moderate", "ewg_score": 5, "category": "Fragrance",
        "function": "Fragrance Component",
        "description": "Citrus-derived fragrance. Strong sensitizer especially when oxidized.",
        "concern": "One of 26 EU-required fragrance allergens. Phototoxic potential. Avoid on sun-exposed skin.", "cosdna_score": 3,
        "good_for": [], "avoid_for": ["Sensitive"]
    },
    "citronellol": {
        "risk": "Moderate", "ewg_score": 4, "category": "Fragrance",
        "function": "Fragrance Component",
        "description": "Rose-like fragrance found in geranium and citronella.",
        "concern": "EU-designated allergen. Potential sensitizer.", "cosdna_score": 2,
        "good_for": [], "avoid_for": ["Sensitive"]
    },

    # ─── Antioxidants ──────────────────────────────────────────────────────────
    "tocopherol": {
        "risk": "Safe", "ewg_score": 1, "category": "Antioxidant",
        "function": "Antioxidant / Skin Conditioner",
        "description": "Vitamin E. Protects skin from free radicals and UV damage. Excellent skin conditioner.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Dry", "Mature"], "avoid_for": []
    },
    "tocopheryl acetate": {
        "risk": "Low", "ewg_score": 4, "category": "Antioxidant",
        "function": "Antioxidant / Skin Conditioner",
        "description": "Stable form of vitamin E. Less potent but more shelf-stable than tocopherol.",
        "concern": "Some studies suggest this form may not convert efficiently to active vitamin E on skin.", "cosdna_score": 1,
        "good_for": ["All"], "avoid_for": []
    },
    "resveratrol": {
        "risk": "Safe", "ewg_score": 1, "category": "Antioxidant",
        "function": "Antioxidant / Anti-aging",
        "description": "Potent polyphenol antioxidant from grape skins. Anti-aging and protective.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["Mature", "Normal", "Dry"], "avoid_for": []
    },
    "coenzyme q10": {
        "risk": "Safe", "ewg_score": 1, "category": "Antioxidant",
        "function": "Antioxidant / Anti-aging",
        "description": "Ubiquinone. Cellular energy antioxidant that declines with age. Anti-wrinkle.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["Mature", "Normal"], "avoid_for": []
    },
    "green tea extract": {
        "risk": "Safe", "ewg_score": 1, "category": "Antioxidant",
        "function": "Antioxidant / Soothing / Anti-aging",
        "description": "Rich in EGCG polyphenols. Powerful antioxidant and anti-inflammatory.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Acne-Prone", "Mature"], "avoid_for": []
    },
    "ferulic acid": {
        "risk": "Safe", "ewg_score": 1, "category": "Antioxidant",
        "function": "Antioxidant / UV Photoprotection",
        "description": "Plant-derived antioxidant that enhances stability and efficacy of vitamins C and E.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Mature"], "avoid_for": []
    },

    # ─── Thickeners & Emulsifiers ──────────────────────────────────────────────
    "carbomer": {
        "risk": "Low", "ewg_score": 1, "category": "Thickener",
        "function": "Thickener / Gel-forming Agent",
        "description": "Synthetic polymer used to create gel textures. Generally safe and inert.",
        "concern": "May cause eye irritation. Very rarely, mild skin irritation.", "cosdna_score": 1,
        "good_for": ["All", "Oily"], "avoid_for": []
    },
    "xanthan gum": {
        "risk": "Safe", "ewg_score": 1, "category": "Thickener",
        "function": "Thickener / Stabilizer",
        "description": "Natural thickener from bacterial fermentation. Completely safe.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All"], "avoid_for": []
    },
    "cetearyl alcohol": {
        "risk": "Low", "ewg_score": 1, "category": "Emulsifier",
        "function": "Emulsifier / Emollient",
        "description": "Fatty alcohol mixture. Emulsifies and conditions skin.",
        "concern": "Rare sensitization.", "cosdna_score": 1,
        "good_for": ["Dry", "Normal", "Mature"], "avoid_for": []
    },
    "polysorbate 20": {
        "risk": "Low", "ewg_score": 3, "category": "Emulsifier",
        "function": "Emulsifier / Solubilizer",
        "description": "PEG-derived emulsifier used to blend oil and water.",
        "concern": "PEG-compound may contain 1,4-dioxane contamination. Generally safe as used.", "cosdna_score": 2,
        "good_for": ["All"], "avoid_for": []
    },

    # ─── Problematic / Controversial ──────────────────────────────────────────
    "triclosan": {
        "risk": "Danger", "ewg_score": 7, "category": "Antimicrobial",
        "function": "Antimicrobial / Preservative",
        "description": "Synthetic antimicrobial agent. Banned from over-the-counter soaps by FDA (2016).",
        "concern": "Endocrine disruptor. Promotes antibiotic resistance. Aquatic toxicant. FDA banned from hand soaps.", "cosdna_score": 5,
        "good_for": [], "avoid_for": ["All"]
    },
    "phthalates": {
        "risk": "Danger", "ewg_score": 10, "category": "Fragrance",
        "function": "Plasticizer / Fragrance Carrier",
        "description": "Used in fragrances and plastics. Potent endocrine disruptors.",
        "concern": "Potent endocrine disruptors. Linked to reproductive issues, developmental problems. Banned in EU.", "cosdna_score": 5,
        "good_for": [], "avoid_for": ["All", "Pregnant"]
    },
    "bha": {
        "risk": "High", "ewg_score": 7, "category": "Antioxidant",
        "function": "Preservative / Antioxidant",
        "description": "Butylated hydroxyanisole – not to be confused with beta-hydroxy acid (salicylic acid).",
        "concern": "Possible endocrine disruptor and carcinogen. Listed as anticipated human carcinogen by NTP.", "cosdna_score": 4,
        "good_for": [], "avoid_for": ["All", "Sensitive"]
    },
    "coal tar": {
        "risk": "Danger", "ewg_score": 10, "category": "Active",
        "function": "Anti-dandruff / Anti-psoriasis",
        "description": "Used in dandruff/psoriasis treatments. Classified as carcinogen.",
        "concern": "Known human carcinogen (IARC Group 1). Banned in EU in cosmetics. May cause photosensitivity.", "cosdna_score": 5,
        "good_for": [], "avoid_for": ["All"]
    },
    "lead": {
        "risk": "Danger", "ewg_score": 10, "category": "Colorant",
        "function": "Impurity / Heavy Metal",
        "description": "Heavy metal found as contaminant in some lipsticks and cosmetics.",
        "concern": "Neurotoxin. No safe level of lead exposure. Accumulates in body.", "cosdna_score": 5,
        "good_for": [], "avoid_for": ["All"]
    },
    "mercury": {
        "risk": "Danger", "ewg_score": 10, "category": "Preservative",
        "function": "Preservative / Skin Lightener",
        "description": "Heavy metal used in some skin lightening products. Banned in most countries.",
        "concern": "Highly toxic. Causes kidney damage, neurological damage. Illegal in most cosmetics globally.", "cosdna_score": 5,
        "good_for": [], "avoid_for": ["All"]
    },
    "aluminum": {
        "risk": "Moderate", "ewg_score": 5, "category": "Active",
        "function": "Antiperspirant Active",
        "description": "Aluminum salts used in antiperspirants to block sweat.",
        "concern": "Possible links to breast cancer and Alzheimer's (under debate). Avoid applying to broken skin.", "cosdna_score": 3,
        "good_for": [], "avoid_for": ["Sensitive"]
    },

    # ─── Beneficial Additives ──────────────────────────────────────────────────
    "ceramide": {
        "risk": "Safe", "ewg_score": 1, "category": "Skin Conditioning",
        "function": "Barrier Repair / Skin Conditioning",
        "description": "Key lipid component of skin barrier. Restores and strengthens the skin's protective layer.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Dry", "Sensitive", "Eczema"], "avoid_for": []
    },
    "ceramide np": {
        "risk": "Safe", "ewg_score": 1, "category": "Skin Conditioning",
        "function": "Barrier Repair",
        "description": "Specific ceramide type most abundant in healthy skin. Essential for barrier function.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Dry", "Sensitive", "Eczema"], "avoid_for": []
    },
    "peptides": {
        "risk": "Safe", "ewg_score": 1, "category": "Anti-aging",
        "function": "Anti-aging / Collagen Stimulant",
        "description": "Short amino acid chains that signal skin to produce collagen and other proteins.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["Mature", "Normal", "Dry"], "avoid_for": []
    },
    "adenosine": {
        "risk": "Safe", "ewg_score": 1, "category": "Anti-aging",
        "function": "Anti-aging / Anti-wrinkle",
        "description": "Naturally occurring molecule that helps reduce wrinkle depth and improve skin elasticity.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["Mature", "Normal"], "avoid_for": []
    },
    "centella asiatica extract": {
        "risk": "Safe", "ewg_score": 1, "category": "Soothing",
        "function": "Soothing / Wound Healing / Anti-inflammatory",
        "description": "'Cica' herb with powerful skin-calming and barrier-repair properties. K-beauty staple.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Sensitive", "Acne-Prone", "Eczema"], "avoid_for": []
    },
    "madecassoside": {
        "risk": "Safe", "ewg_score": 1, "category": "Soothing",
        "function": "Anti-inflammatory / Wound Healing",
        "description": "Active compound from Centella Asiatica. Calms irritation and promotes healing.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Sensitive"], "avoid_for": []
    },
    "tranexamic acid": {
        "risk": "Safe", "ewg_score": 1, "category": "Brightening",
        "function": "Brightening / Hyperpigmentation",
        "description": "Newer brightening ingredient. Gentle alternative to kojic acid and hydroquinone.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Sensitive"], "avoid_for": []
    },
    "bakuchiol": {
        "risk": "Safe", "ewg_score": 1, "category": "Anti-aging",
        "function": "Natural Retinol Alternative / Anti-aging",
        "description": "Plant-derived ingredient with similar benefits to retinol but without the irritation.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Sensitive", "Pregnant"], "avoid_for": []
    },
    "allantoin": {
        "risk": "Safe", "ewg_score": 1, "category": "Soothing",
        "function": "Soothing / Skin Conditioner",
        "description": "Multi-tasking ingredient that soothes, heals, and keeps skin soft.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Sensitive", "Acne-Prone"], "avoid_for": []
    },
    "alpha arbutin": {
        "risk": "Low", "ewg_score": 1, "category": "Brightening",
        "function": "Skin Brightener / Tyrosinase Inhibitor",
        "description": "Stable, gentle brightening ingredient. Safer alternative to hydroquinone.",
        "concern": "At very high concentrations may hydrolyze to hydroquinone.", "cosdna_score": 1,
        "good_for": ["All", "Sensitive"], "avoid_for": []
    },
    "caffeine": {
        "risk": "Safe", "ewg_score": 1, "category": "Active",
        "function": "Antioxidant / De-puffing / Anti-cellulite",
        "description": "Tightens and de-puffs skin. Antioxidant benefits and reduces under-eye circles.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Oily"], "avoid_for": []
    },
    "sodium pca": {
        "risk": "Safe", "ewg_score": 1, "category": "Humectant",
        "function": "Humectant / Skin Conditioning",
        "description": "Component of skin's Natural Moisturizing Factor (NMF). Excellent moisture retention.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Dry"], "avoid_for": []
    },
    "bisabolol": {
        "risk": "Safe", "ewg_score": 1, "category": "Soothing",
        "function": "Anti-inflammatory / Soothing",
        "description": "From chamomile. Calms irritation, redness, and inflammation.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Sensitive", "Rosacea"], "avoid_for": []
    },
    "mandelic acid": {
        "risk": "Low", "ewg_score": 2, "category": "Exfoliant",
        "function": "AHA Exfoliant / Brightening",
        "description": "Gentler AHA suitable for sensitive skin. Also has some antibacterial properties.",
        "concern": "Mild photosensitivity.", "cosdna_score": 1,
        "good_for": ["Sensitive", "Acne-Prone", "Normal"], "avoid_for": []
    },
    "polyglutamic acid": {
        "risk": "Safe", "ewg_score": 1, "category": "Humectant",
        "function": "Humectant / Film-forming",
        "description": "Amino acid polymer that holds water even better than hyaluronic acid.",
        "concern": "", "cosdna_score": 0,
        "good_for": ["All", "Dry", "Mature"], "avoid_for": []
    },
    "snail secretion filtrate": {
        "risk": "Low", "ewg_score": 2, "category": "Skin Conditioning",
        "function": "Skin Repair / Hydration / Anti-aging",
        "description": "K-beauty hero ingredient. Promotes healing, hydration, and collagen production.",
        "concern": "Possible allergen for those with snail/shellfish sensitivities.", "cosdna_score": 1,
        "good_for": ["All", "Acne-Prone", "Mature"], "avoid_for": []
    },
}

# Alias mappings (alternate names → canonical)
INGREDIENT_ALIASES = {
    "aqua": "water",
    "vitamin e": "tocopherol",
    "vitamin b3": "niacinamide",
    "vitamin b5": "panthenol",
    "hyaluronic acid": "hyaluronic acid",
    "ha": "hyaluronic acid",
    "aha": "glycolic acid",
    "bha": "salicylic acid",
    "aloe vera": "aloe barbadensis leaf juice",
    "aloe": "aloe barbadensis leaf juice",
    "retinol a": "retinol",
    "sodium lauryl sulphate": "sodium lauryl sulfate",
    "sls": "sodium lauryl sulfate",
    "sles": "sodium laureth sulfate",
    "cica": "centella asiatica extract",
    "coq10": "coenzyme q10",
    "q10": "coenzyme q10",
    "vc": "vitamin c",
    "ascorbyl": "ascorbic acid",
    "shea": "shea butter",
    "jojoba": "jojoba oil",
    "argan": "argan oil",
    "rosehip": "rosehip oil",
    "green tea": "green tea extract",
    "ceramides": "ceramide",
    "glycerine": "glycerin",
    "glycerol": "glycerin",
    "petrolatum": "petrolatum",
    "vaseline": "petrolatum",
    "mineral oil": "mineral oil",
}
