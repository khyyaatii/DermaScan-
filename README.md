# 🧬 DermaScan — Skincare Ingredient Intelligence Platform

> Advanced AI-powered cosmetic ingredient analyzer for safer skincare choices.

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. (Optional) Install Tesseract for Image OCR
- **Linux:** `sudo apt-get install tesseract-ocr`
- **macOS:** `brew install tesseract`
- **Windows:** Download from https://github.com/UB-Mannheim/tesseract/wiki

### 3. Run the app
```bash
streamlit run app.py
```

The app opens at **http://localhost:8501**

---

## ✨ Features

| Feature | Description |
|---|---|
| 📷 Image Upload & OCR | Upload product label photos; auto-extracts ingredient text |
| ✍️ Manual Input | Paste any INCI ingredient list |
| 🔬 Deep Analysis | Risk scoring, EWG ratings, CosDNA functions |
| 📊 Toxicity Score | 0–10 scale with letter grade (A+ to F) |
| 💆 Skin Compatibility | Personalized scores for your skin type |
| 🚨 Allergen Alerts | Cross-checks your known allergies |
| 📈 Interactive Dashboards | Donut chart, bar chart, EWG histogram, radar chart |
| 🔎 Ingredient Explorer | Search single ingredients in our database |
| ⬇️ CSV Export | Download full analysis report |
| 💡 Recommendations | Personalized skincare advice |
| 🌐 Pregnancy Safety | Flags ingredients unsafe during pregnancy |

---

## 📦 Project Structure

```
dermascan/
├── app.py                  # Main Streamlit application
├── ingredient_database.py  # 10,000+ ingredient database
├── analyzer.py             # Core analysis engine
├── utils.py                # OCR & text parsing utilities
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🎓 Academic Notes (Final Year Project)

This project demonstrates:
- **Data Analysis**: Risk categorization, EWG scoring, statistical aggregation
- **Machine Learning adjacent**: Pattern matching, NLP text parsing, fuzzy ingredient matching
- **Data Visualization**: Interactive Plotly charts (donut, bar, histogram, radar)
- **Computer Vision**: OCR integration via Tesseract
- **Database Design**: Structured ingredient knowledge base
- **UI/UX**: Professional Streamlit interface with custom CSS

### Data Sources
- EWG Skin Deep® Database
- CosDNA Ingredient Analysis
- INCI (International Nomenclature of Cosmetic Ingredients)
- PubChem Chemical Database
- EU Cosmetics Regulation Banned/Restricted substances list

---

## ⚠️ Disclaimer

DermaScan is for **educational and informational purposes only**. Always consult a licensed dermatologist for medical skincare advice. The ingredient risk assessments are based on publicly available scientific data and may not reflect the most current research.

---

Made with ❤️ for skin safety | DermaScan v2.0
