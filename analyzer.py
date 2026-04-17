"""
DermaScan Analyzer Module
Core logic for analyzing ingredients and generating insights.
"""

import numpy as np
from ingredient_database import INGREDIENT_DATABASE, INGREDIENT_ALIASES

RISK_WEIGHTS = {
    "Safe": 0,
    "Low": 2,
    "Moderate": 5,
    "High": 8,
    "Danger": 10,
}

GRADE_MAP = [
    (1.5, "A+"), (2.5, "A"), (3.5, "A−"),
    (4.5, "B+"), (5.5, "B"), (6.0, "B−"),
    (7.0, "C+"), (7.5, "C"), (8.5, "D"),
    (float("inf"), "F"),
]

SKIN_TYPE_GOOD = {
    "Dry": ["Humectant", "Emollient", "Skin Conditioning", "Anti-aging"],
    "Oily": ["Active", "Exfoliant", "Surfactant"],
    "Combination": ["Humectant", "Active", "Brightening"],
    "Sensitive": ["Soothing", "Humectant", "Skin Conditioning"],
    "Normal": ["Humectant", "Active", "Anti-aging", "Antioxidant"],
    "Acne-Prone": ["Active", "Exfoliant", "Antimicrobial", "Soothing"],
    "Mature": ["Anti-aging", "Humectant", "Antioxidant", "Emollient"],
}

SKIN_TYPE_BAD = {
    "Sensitive": ["Fragrance", "Surfactant", "Exfoliant", "Preservative"],
    "Acne-Prone": ["Emollient", "Fragrance"],
    "Dry": ["Surfactant", "Exfoliant"],
    "Oily": ["Emollient"],
}

CONCERN_INGREDIENT_MAP = {
    "Acne": {"good": ["salicylic acid", "niacinamide", "azelaic acid", "benzoyl peroxide", "tea tree oil"],
             "avoid": ["coconut oil", "cocoa butter", "shea butter", "mineral oil"]},
    "Hyperpigmentation": {"good": ["niacinamide", "vitamin c", "alpha arbutin", "tranexamic acid", "kojic acid", "glycolic acid"],
                          "avoid": ["fragrance", "parfum"]},
    "Anti-aging": {"good": ["retinol", "peptides", "vitamin c", "hyaluronic acid", "coenzyme q10", "resveratrol", "adenosine"],
                   "avoid": ["sodium lauryl sulfate"]},
    "Redness": {"good": ["azelaic acid", "centella asiatica extract", "allantoin", "bisabolol", "green tea extract"],
                "avoid": ["fragrance", "alcohol denat", "retinol", "salicylic acid"]},
    "Dryness": {"good": ["hyaluronic acid", "glycerin", "ceramide", "squalane", "shea butter", "panthenol"],
                "avoid": ["sodium lauryl sulfate", "alcohol denat", "salicylic acid"]},
}

RADAR_INGREDIENT_MAP = {
    "Hydration": ["hyaluronic acid", "glycerin", "sodium hyaluronate", "panthenol", "aloe barbadensis leaf juice",
                  "polyglutamic acid", "sodium pca", "urea", "sorbitol", "ceramide"],
    "Brightening": ["vitamin c", "ascorbic acid", "niacinamide", "alpha arbutin", "tranexamic acid",
                    "kojic acid", "glycolic acid", "lactic acid", "mandelic acid"],
    "Anti-aging": ["retinol", "peptides", "adenosine", "coenzyme q10", "resveratrol", "ferulic acid",
                   "bakuchiol", "vitamin c"],
    "Sun Protection": ["titanium dioxide", "zinc oxide", "oxybenzone", "avobenzone", "octinoxate", "octocrylene"],
    "Soothing": ["centella asiatica extract", "allantoin", "bisabolol", "aloe barbadensis leaf juice",
                 "green tea extract", "madecassoside", "azelaic acid"],
    "Exfoliation": ["glycolic acid", "salicylic acid", "lactic acid", "mandelic acid", "urea",
                    "retinol", "polyhydroxy acid"],
}


def normalize_name(name: str) -> str:
    """Normalize ingredient name for matching."""
    clean = name.strip().lower()
    clean = clean.replace("-", " ").replace("_", " ")
    # Check aliases
    if clean in INGREDIENT_ALIASES:
        return INGREDIENT_ALIASES[clean]
    return clean


def analyze_ingredients(parsed_list: list, skin_type: str, skin_concerns: list,
                        allergies: str, strictness: str) -> dict:
    """Main analysis function."""

    found = []
    unknown = []

    for ing in parsed_list:
        norm = normalize_name(ing)
        if norm in INGREDIENT_DATABASE:
            data = INGREDIENT_DATABASE[norm].copy()
            data["name"] = norm
            data["original_name"] = ing.strip()
            found.append(data)
        else:
            # fuzzy partial match
            matched = False
            for db_key, db_val in INGREDIENT_DATABASE.items():
                if norm in db_key or db_key in norm:
                    data = db_val.copy()
                    data["name"] = db_key
                    data["original_name"] = ing.strip()
                    found.append(data)
                    matched = True
                    break
            if not matched:
                unknown.append(ing.strip())

    if not found:
        return {"found": [], "unknown": unknown, "toxicity_score": 0, "grade": "N/A",
                "verdict_detail": "", "allergen_alerts": [], "radar": {}}

    # ── Toxicity Score ──────────────────────────────────────────────────────
    strictness_multiplier = {"Lenient": 0.8, "Balanced": 1.0, "Strict": 1.2}[strictness]
    raw_weights = [RISK_WEIGHTS[i["risk"]] for i in found]

    # Weighted score: top-3 worst ingredients count more
    sorted_weights = sorted(raw_weights, reverse=True)
    top_contribution = np.mean(sorted_weights[:3]) if len(sorted_weights) >= 3 else np.mean(sorted_weights)
    overall_avg = np.mean(raw_weights)
    raw_score = (top_contribution * 0.6 + overall_avg * 0.4) * strictness_multiplier
    toxicity_score = round(min(10, max(0, raw_score)), 1)

    # ── Grade ───────────────────────────────────────────────────────────────
    grade = "F"
    for threshold, g in GRADE_MAP:
        if toxicity_score <= threshold:
            grade = g
            break

    # ── Verdict ─────────────────────────────────────────────────────────────
    high_risk = [i["name"] for i in found if i["risk"] in ["High", "Danger"]]
    moderate = [i["name"] for i in found if i["risk"] == "Moderate"]
    safe_count = sum(1 for i in found if i["risk"] in ["Safe", "Low"])

    verdict_parts = []
    if high_risk:
        verdict_parts.append(f"Contains {len(high_risk)} high-concern ingredient(s): {', '.join(high_risk[:3])}.")
    if moderate:
        verdict_parts.append(f"{len(moderate)} ingredient(s) warrant moderate caution.")
    verdict_parts.append(f"{safe_count} of {len(found)} identified ingredients are considered safe.")
    verdict_detail = " ".join(verdict_parts)

    # ── Allergen Alerts ─────────────────────────────────────────────────────
    allergen_alerts = []
    if allergies:
        user_allergens = [a.strip().lower() for a in allergies.split(",")]
        for ing in found:
            for allergen in user_allergens:
                if allergen and allergen in ing["name"].lower():
                    allergen_alerts.append(f"⚠️ {ing['name'].title()} matches your allergy to '{allergen}'")

    # ── Skin Compatibility ──────────────────────────────────────────────────
    skin_compat = {}
    good_cats = SKIN_TYPE_GOOD.get(skin_type, [])
    bad_cats = SKIN_TYPE_BAD.get(skin_type, [])

    if skin_type:
        # Barrier score
        barrier_ingredients = ["ceramide", "ceramide np", "glycerin", "hyaluronic acid", "squalane", "petrolatum", "shea butter"]
        barrier_count = sum(1 for i in found if i["name"] in barrier_ingredients)
        skin_compat["Barrier Support"] = min(100, barrier_count * 25 + 30)

        # Compatibility score
        compat_score = 70
        for ing in found:
            if ing.get("category") in good_cats:
                compat_score += 3
            if ing.get("category") in bad_cats:
                compat_score -= 8
            if skin_type in ing.get("good_for", []):
                compat_score += 5
            if skin_type in ing.get("avoid_for", []):
                compat_score -= 10
        skin_compat["Overall Compatibility"] = max(0, min(100, compat_score))

        # Irritation risk
        irritants = [i for i in found if i["risk"] in ["High", "Danger"]]
        irritation_risk = max(0, 100 - len(irritants) * 20 - toxicity_score * 5)
        skin_compat["Low Irritation Risk"] = round(irritation_risk)

        # Moisturization
        humectants = [i for i in found if i.get("category") == "Humectant"]
        emollients = [i for i in found if i.get("category") == "Emollient"]
        moist_score = min(100, (len(humectants) + len(emollients)) * 15 + 20)
        skin_compat["Moisturization Potential"] = moist_score

    # ── Radar Values ────────────────────────────────────────────────────────
    found_names = [i["name"] for i in found]
    radar = {}
    for benefit, ingredients in RADAR_INGREDIENT_MAP.items():
        count = sum(1 for ing in ingredients if ing in found_names)
        radar[benefit] = min(100, count * 30 + 10)

    # ── Concern-specific recommendations ───────────────────────────────────
    concern_recs = []
    for concern in (skin_concerns or []):
        if concern in CONCERN_INGREDIENT_MAP:
            missing_good = [g for g in CONCERN_INGREDIENT_MAP[concern]["good"]
                           if g not in found_names][:2]
            present_bad = [b for b in CONCERN_INGREDIENT_MAP[concern]["avoid"]
                          if b in found_names]
            if missing_good:
                concern_recs.append(f"For {concern}: consider adding {', '.join(missing_good)}")
            if present_bad:
                concern_recs.append(f"For {concern}: watch out for {', '.join(present_bad)} in this formula")

    return {
        "found": found,
        "unknown": unknown,
        "toxicity_score": toxicity_score,
        "grade": grade,
        "verdict_detail": verdict_detail,
        "allergen_alerts": allergen_alerts,
        "skin_compatibility": skin_compat,
        "radar": radar,
        "concern_recs": concern_recs,
    }


def get_skin_type_recommendation(skin_type: str, results: dict, skin_concerns: list) -> list:
    """Generate personalized recommendations."""
    recs = []
    found_names = [i["name"] for i in results["found"]]
    score = results["toxicity_score"]

    # General score recommendation
    if score <= 3:
        recs.append("This formula scores well on safety. It appears to be a clean, well-formulated product.")
    elif score <= 6:
        recs.append("This product has moderate concerns. Consider if the flagged ingredients are deal-breakers for you.")
    else:
        recs.append("This product has significant concerns. We recommend looking for an alternative formula.")

    # Skin type specific
    skin_recs = {
        "Sensitive": "Look for fragrance-free, alcohol-free formulas. This product's suitability for sensitive skin depends on the flagged ingredients.",
        "Acne-Prone": "Ensure any oils or heavy emollients in this product are non-comedogenic. Niacinamide and salicylic acid are beneficial here.",
        "Dry": "Prioritize products rich in humectants (hyaluronic acid, glycerin) and emollients (ceramides, fatty acids).",
        "Oily": "Lightweight, non-comedogenic formulas work best. Look for gel textures and BHA exfoliants.",
        "Mature": "This skin type benefits from retinoids, peptides, and antioxidants like vitamin C and CoQ10.",
    }
    if skin_type in skin_recs:
        recs.append(skin_recs[skin_type])

    # Concern-specific
    recs.extend(results.get("concern_recs", []))

    # Pregnancy warning
    if any(i["name"] in ["retinol", "retinyl palmitate", "salicylic acid", "hydroquinone"]
           for i in results["found"]):
        recs.append("⚠️ Pregnancy Note: This product contains ingredients not recommended during pregnancy (retinoids, high-dose salicylic acid, or hydroquinone). Consult your doctor.")

    # EWG advice
    high_ewg = [i for i in results["found"] if i.get("ewg_score", 0) >= 7]
    if high_ewg:
        recs.append(f"High EWG Score Alert: {', '.join(i['name'].title() for i in high_ewg[:3])} score 7+ on the EWG hazard scale. Consider EWG-verified alternatives.")

    return recs
