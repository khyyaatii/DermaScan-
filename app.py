import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image

from ingredient_database import INGREDIENT_DATABASE, CATEGORIES, RISK_LEVELS
from analyzer import analyze_ingredients, get_skin_type_recommendation
from utils import extract_text_from_image, parse_ingredients_text

# Mobile-first page config
st.set_page_config(
    page_title="DermaScan",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── CSS Styling (Mobile Friendly Updated) ─────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

/* ── Root Variables ── */
:root{
  --bg-primary:#0d0f14;
  --bg-secondary:#13161e;
  --bg-card:#1a1d28;
  --bg-card-hover:#1f2333;
  --accent-gold:#c9a96e;
  --accent-gold-light:#e8c99a;
  --accent-rose:#c97e8a;
  --accent-sage:#7aab8e;
  --accent-blue:#6e8ec9;
  --text-primary:#f0ece4;
  --text-secondary:#b8b0a4;
  --text-muted:#7a756e;
  --border:rgba(201,169,110,0.15);
  --border-strong:rgba(201,169,110,0.35);
  --shadow:0 8px 32px rgba(0,0,0,0.35);
  --risk-safe:#5da882;
  --risk-low:#8eb85a;
  --risk-moderate:#d4a843;
  --risk-high:#d4733a;
  --risk-danger:#c94f4f;
}

/* ── Global ── */
html,body,.stApp{
  background:var(--bg-primary)!important;
  color:var(--text-primary)!important;
  font-family:'DM Sans',sans-serif!important;
}

/* ── Hide Streamlit Chrome ── */
#MainMenu,header,footer{visibility:hidden;}
.stDeployButton{display:none;}

/* ── Main Container ── */
.block-container{
  max-width:1100px!important;
  padding:1rem 1rem 3rem!important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"]{
  background:var(--bg-secondary)!important;
  border-right:1px solid var(--border)!important;
}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span{
  color:var(--text-secondary)!important;
}

/* ── Typography ── */
h1,h2{
  font-family:'Cormorant Garamond',serif!important;
  color:var(--text-primary)!important;
  line-height:1.15!important;
}
h1{font-size:2.6rem!important;font-weight:400!important;}
h2{font-size:2rem!important;font-weight:400!important;}
h3{
  font-family:'DM Sans',sans-serif!important;
  font-weight:600!important;
  color:var(--text-primary)!important;
}
p,li,span{
  color:var(--text-primary)!important;
}

/* ── Hero Banner ── */
.hero-banner{
  background:linear-gradient(135deg,#0d0f14 0%,#1a1420 40%,#0f1a18 100%);
  border:1px solid var(--border-strong);
  border-radius:20px;
  padding:2rem 1.4rem;
  margin:1rem 0 1.4rem;
  position:relative;
  overflow:hidden;
}

.hero-banner::before{
  content:'';
  position:absolute;
  top:-50px;
  right:-50px;
  width:180px;
  height:180px;
  background:radial-gradient(circle,rgba(201,169,110,0.08) 0%,transparent 70%);
  border-radius:50%;
}

.hero-banner::after{
  content:'';
  position:absolute;
  bottom:-45px;
  left:20%;
  width:150px;
  height:150px;
  background:radial-gradient(circle,rgba(122,171,142,0.07) 0%,transparent 70%);
  border-radius:50%;
}

/* ── Mobile Responsive ── */
@media (max-width: 768px){

  .block-container{
    padding:.7rem .75rem 2rem!important;
    max-width:100%!important;
  }

  h1{
    font-size:1.9rem!important;
    line-height:1.1!important;
  }

  h2{
    font-size:1.5rem!important;
  }

  h3{
    font-size:1rem!important;
  }

  .hero-banner{
    padding:1.2rem 1rem!important;
    border-radius:16px!important;
    margin:.6rem 0 1rem!important;
  }

  .hero-banner::before{
    width:110px;
    height:110px;
    top:-25px;
    right:-25px;
  }

  .hero-banner::after{
    width:90px;
    height:90px;
    bottom:-20px;
  }

  [data-testid="stSidebar"]{
    width:100%!important;
  }

  button{
    min-height:46px!important;
  }

  input,textarea,select{
    font-size:16px!important;
  }
}

/* ── Small Phones ── */
@media (max-width:480px){

  .block-container{
    padding:.55rem .6rem 1.5rem!important;
  }

  h1{font-size:1.65rem!important;}
  h2{font-size:1.35rem!important;}

  .hero-banner{
    padding:1rem .85rem!important;
  }
}

.hero-banner::after{
  content:'';
  position:absolute;
  bottom:-35px;
  left:22%;
  width:150px;
  height:150px;
  background:radial-gradient(circle, rgba(122,171,142,0.06) 0%, transparent 70%);
  border-radius:50%;
}

/* ── Hero Text ── */
.hero-title{
  font-family:'Cormorant Garamond', serif;
  font-size:3.2rem;
  font-weight:300;
  letter-spacing:.04em;
  color:var(--text-primary)!important;
  margin:0;
  line-height:1.08;
}

.hero-title span{
  color:var(--accent-gold)!important;
  font-style:italic;
}

.hero-tagline{
  font-family:'DM Sans', sans-serif;
  font-size:.88rem;
  color:var(--text-secondary)!important;
  letter-spacing:.18em;
  text-transform:uppercase;
  margin-top:.65rem;
}

.hero-desc{
  font-family:'DM Sans', sans-serif;
  font-size:1rem;
  color:var(--text-secondary)!important;
  margin-top:1rem;
  max-width:620px;
  line-height:1.65;
}

/* ── Cards ── */
.ds-card{
  background:var(--bg-card);
  border:1px solid var(--border);
  border-radius:16px;
  padding:1.2rem 1rem;
  margin-bottom:1rem;
  transition:.25s ease;
}

.ds-card:hover{
  border-color:var(--border-strong);
  box-shadow:var(--shadow);
}

.ds-card-title{
  font-family:'Cormorant Garamond', serif;
  font-size:1.35rem;
  font-weight:500;
  color:var(--accent-gold)!important;
  margin-bottom:.8rem;
  display:flex;
  align-items:center;
  gap:.45rem;
}

/* ── Metric Cards ── */
.metric-grid{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:.8rem;
  margin:1rem 0;
}

.metric-card{
  background:var(--bg-card);
  border:1px solid var(--border);
  border-radius:14px;
  padding:1rem .75rem;
  text-align:center;
  transition:.25s ease;
}

.metric-card:hover{
  border-color:var(--border-strong);
  transform:translateY(-2px);
  box-shadow:var(--shadow);
}

.metric-value{
  font-family:'Cormorant Garamond', serif;
  font-size:2.2rem;
  font-weight:400;
  line-height:1;
  margin-bottom:.2rem;
}

.metric-label{
  font-family:'DM Sans', sans-serif;
  font-size:.72rem;
  letter-spacing:.12em;
  text-transform:uppercase;
  color:var(--text-muted)!important;
}

/* ── Score Section ── */
.score-section{
  display:flex;
  align-items:center;
  gap:1.2rem;
  background:var(--bg-card);
  border:1px solid var(--border);
  border-radius:16px;
  padding:1.2rem 1rem;
  margin-bottom:1rem;
}

/* ── Mobile Responsive ── */
@media (max-width:768px){

  .hero-banner::after{
    width:90px;
    height:90px;
    left:18%;
    bottom:-18px;
  }

  .hero-title{
    font-size:2rem!important;
    line-height:1.08;
  }

  .hero-tagline{
    font-size:.72rem!important;
    letter-spacing:.10em!important;
    margin-top:.45rem;
  }

  .hero-desc{
    font-size:.92rem!important;
    line-height:1.55!important;
    margin-top:.75rem;
  }

  .ds-card{
    padding:1rem .9rem!important;
    border-radius:14px!important;
  }

  .ds-card-title{
    font-size:1.15rem!important;
  }

  .metric-grid{
    grid-template-columns:1fr 1fr!important;
    gap:.65rem!important;
  }

  .metric-card{
    padding:.85rem .6rem!important;
  }

  .metric-value{
    font-size:1.8rem!important;
  }

  .metric-label{
    font-size:.64rem!important;
    letter-spacing:.08em!important;
  }

  .score-section{
    display:block!important;
    padding:1rem .9rem!important;
  }
}

/* ── Extra Small Phones ── */
@media (max-width:480px){

  .hero-title{font-size:1.7rem!important;}
  .metric-grid{grid-template-columns:1fr!important;}
  .hero-desc{font-size:.88rem!important;}
}
.score-label{
  font-family:'DM Sans',sans-serif;
  font-size:.74rem;
  letter-spacing:.14em;
  text-transform:uppercase;
  color:var(--text-muted)!important;
  margin-bottom:.3rem;
}

.score-value{
  font-family:'Cormorant Garamond',serif;
  font-size:4rem;
  font-weight:400;
  line-height:1;
}

.score-verdict{
  font-family:'DM Sans',sans-serif;
  font-size:.92rem;
  color:var(--text-secondary)!important;
  max-width:100%;
  line-height:1.55;
}

/* ── Risk Badges ── */
.badge{
  display:inline-block;
  padding:.28rem .65rem;
  border-radius:20px;
  font-size:.68rem;
  font-weight:700;
  letter-spacing:.08em;
  text-transform:uppercase;
  white-space:nowrap;
}

.badge-safe{
  background:rgba(93,168,130,.15);
  color:#5da882!important;
  border:1px solid rgba(93,168,130,.35);
}
.badge-low{
  background:rgba(142,184,90,.15);
  color:#8eb85a!important;
  border:1px solid rgba(142,184,90,.35);
}
.badge-moderate{
  background:rgba(212,168,67,.15);
  color:#d4a843!important;
  border:1px solid rgba(212,168,67,.35);
}
.badge-high{
  background:rgba(212,115,58,.15);
  color:#d4733a!important;
  border:1px solid rgba(212,115,58,.35);
}
.badge-danger{
  background:rgba(201,79,79,.15);
  color:#c94f4f!important;
  border:1px solid rgba(201,79,79,.35);
}

/* ── Ingredient Table ── */
.ing-row{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:.8rem;
  padding:.85rem 0;
  border-bottom:1px solid var(--border);
}

.ing-row:last-child{
  border-bottom:none;
}

.ing-name{
  font-family:'DM Mono',monospace;
  font-size:.86rem;
  color:var(--text-primary)!important;
  flex:1.2;
  word-break:break-word;
}

.ing-category{
  font-size:.76rem;
  color:var(--text-muted)!important;
  flex:1;
  text-align:center;
}

.ing-function{
  font-size:.76rem;
  color:var(--text-secondary)!important;
  flex:1.4;
  text-align:right;
}

/* ── Progress Bars ── */
.progress-bar-outer{
  background:rgba(255,255,255,.06);
  border-radius:10px;
  height:8px;
  width:100%;
  overflow:hidden;
  margin-top:.35rem;
}

.progress-bar-inner{
  height:100%;
  border-radius:10px;
  transition:width .8s ease;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"]{
  background:var(--bg-secondary)!important;
  border-radius:12px!important;
  padding:4px!important;
  gap:4px!important;
  border:1px solid var(--border)!important;
  overflow-x:auto!important;
}

.stTabs [data-baseweb="tab"]{
  background:transparent!important;
  color:var(--text-muted)!important;
  border-radius:8px!important;
  font-family:'DM Sans',sans-serif!important;
  font-size:.82rem!important;
  letter-spacing:.03em!important;
  padding:.45rem .9rem!important;
  white-space:nowrap!important;
}

.stTabs [aria-selected="true"]{
  background:var(--bg-card)!important;
  color:var(--accent-gold)!important;
  border:1px solid var(--border-strong)!important;
}

/* ── Mobile Responsive ── */
@media (max-width:768px){

  .score-label{
    font-size:.68rem!important;
    letter-spacing:.10em!important;
  }

  .score-value{
    font-size:2.9rem!important;
  }

  .score-verdict{
    font-size:.88rem!important;
    margin-top:.35rem;
  }

  .badge{
    font-size:.62rem!important;
    padding:.24rem .55rem!important;
  }

  .ing-row{
    display:block!important;
    padding:.75rem 0!important;
  }

  .ing-name{
    display:block;
    margin-bottom:.2rem;
    font-size:.82rem!important;
  }

  .ing-category,
  .ing-function{
    display:block;
    text-align:left!important;
    margin-top:.12rem;
    font-size:.72rem!important;
  }

  .stTabs [data-baseweb="tab"]{
    font-size:.74rem!important;
    padding:.42rem .7rem!important;
  }
}

/* ── Extra Small Phones ── */
@media (max-width:480px){

  .score-value{font-size:2.45rem!important;}
  .score-verdict{font-size:.84rem!important;}
}
/* ── Inputs ── */
.stTextArea textarea{
  background:var(--bg-card)!important;
  border:1px solid var(--border)!important;
  color:var(--text-primary)!important;
  border-radius:12px!important;
  font-family:'DM Mono',monospace!important;
  font-size:.84rem!important;
  padding:.8rem!important;
  line-height:1.5!important;
}

.stTextArea textarea:focus{
  border-color:var(--accent-gold)!important;
  box-shadow:0 0 0 2px rgba(201,169,110,.14)!important;
}

/* ── File Uploader ── */
.stFileUploader{
  background:var(--bg-card)!important;
  border:2px dashed var(--border-strong)!important;
  border-radius:16px!important;
  padding:1rem!important;
}

.stFileUploader label,
.stFileUploader small,
.stFileUploader div,
.stFileUploader span,
[data-testid="stFileUploader"] *{
  color:#a9a39a!important;
}

[data-testid="stFileUploader"] button{
  color:#222!important;
  background:#c9a96e!important;
  border:none!important;
  border-radius:10px!important;
}

/* ── Selectbox ── */
.stSelectbox [data-baseweb="select"]{
  background:var(--bg-card)!important;
  border-color:var(--border)!important;
  border-radius:12px!important;
}

.stSelectbox [data-baseweb="select"] *{
  color:#b8b0a4!important;
  background:var(--bg-card)!important;
}

/* ── MultiSelect ── */
.stMultiSelect [data-baseweb="select"]{
  background:var(--bg-card)!important;
  border-color:var(--border)!important;
  border-radius:12px!important;
}

.stMultiSelect [data-baseweb="select"] *{
  color:#f0ece4!important;
  background:var(--bg-card)!important;
}

/* popup options */
[data-baseweb="popover"] li,
[data-baseweb="popover"] div,
[data-baseweb="popover"] span{
  color:#444!important;
  background:#fff!important;
}

[data-baseweb="popover"] li:hover{
  background:#f2f2f2!important;
}

/* ── Buttons ── */
.stButton button{
  background:linear-gradient(135deg,#c9a96e,#a8824a)!important;
  color:#0d0f14!important;
  border:none!important;
  border-radius:12px!important;
  font-family:'DM Sans',sans-serif!important;
  font-weight:700!important;
  letter-spacing:.08em!important;
  padding:.72rem 1rem!important;
  min-height:48px!important;
  width:100%!important;
  transition:.25s ease!important;
}

.stButton button:hover{
  transform:translateY(-1px)!important;
  box-shadow:0 6px 18px rgba(201,169,110,.32)!important;
}

/* ── Info Boxes ── */
.tip-box{
  background:rgba(122,171,142,.08);
  border:1px solid rgba(122,171,142,.24);
  border-left:3px solid var(--accent-sage);
  border-radius:10px;
  padding:.95rem 1rem;
  margin:.8rem 0;
  font-size:.9rem;
  line-height:1.5;
  color:var(--text-secondary)!important;
}

.warn-box{
  background:rgba(212,115,58,.08);
  border:1px solid rgba(212,115,58,.24);
  border-left:3px solid var(--risk-high);
  border-radius:10px;
  padding:.95rem 1rem;
  margin:.8rem 0;
  font-size:.9rem;
  line-height:1.5;
  color:var(--text-secondary)!important;
}

/* ── Divider ── */
.gold-divider{
  height:1px;
  background:linear-gradient(90deg,transparent,var(--accent-gold),transparent);
  margin:1.25rem 0;
  opacity:.45;
}

/* ── Mobile Responsive ── */
@media (max-width:768px){

  .stTextArea textarea{
    font-size:16px!important;
    min-height:180px!important;
  }

  .stFileUploader{
    padding:.8rem!important;
    border-radius:14px!important;
  }

  .stButton button{
    min-height:50px!important;
    font-size:.95rem!important;
  }

  .tip-box,
  .warn-box{
    font-size:.84rem!important;
    padding:.8rem .9rem!important;
  }

  .gold-divider{
    margin:1rem 0!important;
  }
}

/* ── Extra Small Phones ── */
@media (max-width:480px){

  .stButton button{
    font-size:.9rem!important;
    letter-spacing:.04em!important;
  }

  .tip-box,
  .warn-box{
    font-size:.8rem!important;
  }
}
/* ── Ingredient Chips ── */
.chip-container{
  display:flex;
  flex-wrap:wrap;
  gap:.45rem;
  margin:.8rem 0;
}

.chip{
  background:var(--bg-card);
  border:1px solid var(--border);
  border-radius:20px;
  padding:.34rem .75rem;
  font-size:.78rem;
  color:var(--text-secondary)!important;
  font-family:'DM Mono',monospace;
  white-space:nowrap;
}

/* ── Plotly Charts ── */
.js-plotly-plot .plotly{
  border-radius:12px;
  overflow:hidden;
}

/* ── Scrollbar ── */
::-webkit-scrollbar{
  width:6px;
  height:6px;
}

::-webkit-scrollbar-track{
  background:var(--bg-primary);
}

::-webkit-scrollbar-thumb{
  background:var(--border-strong);
  border-radius:4px;
}

/* ── Radio ── */
.stRadio [data-testid="stMarkdownContainer"] p{
  color:var(--text-secondary)!important;
}

.stRadio label{
  color:var(--text-primary)!important;
}

/* ── Expander ── */
.streamlit-expanderHeader{
  background:var(--bg-card)!important;
  border:1px solid var(--border)!important;
  border-radius:10px!important;
  color:var(--text-primary)!important;
  padding:.75rem 1rem!important;
}

details{
  background:var(--bg-card)!important;
  border-radius:10px!important;
  overflow:hidden;
}

/* ── Alerts ── */
.stAlert{
  border-radius:10px!important;
}

/* ── Multiselect Popup ── */
[data-baseweb="popover"] li,
[data-baseweb="popover"] div,
[data-baseweb="popover"] span{
  color:#555!important;
  background:#fff!important;
}

[data-baseweb="popover"] li:hover{
  background:#f2f2f2!important;
  color:#222!important;
}

/* Selected values text */
.stMultiSelect [data-baseweb="select"] span{
  color:#f0ece4!important;
}

/* ── Mobile Responsive ── */
@media (max-width:768px){

  .chip-container{
    gap:.35rem!important;
    margin:.65rem 0!important;
  }

  .chip{
    font-size:.72rem!important;
    padding:.3rem .6rem!important;
    max-width:100%;
    white-space:normal!important;
    word-break:break-word;
  }

  .streamlit-expanderHeader{
    padding:.65rem .85rem!important;
    font-size:.92rem!important;
  }

  .stAlert{
    font-size:.9rem!important;
  }

  ::-webkit-scrollbar{
    width:4px;
    height:4px;
  }
}

/* ── Extra Small Phones ── */
@media (max-width:480px){

  .chip{
    font-size:.68rem!important;
    padding:.26rem .52rem!important;
  }

  .streamlit-expanderHeader{
    font-size:.86rem!important;
  }
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:1rem 0 .7rem;">
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.55rem;font-weight:400;color:#c9a96e;letter-spacing:.10em;">DERMA</div>
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.55rem;font-weight:400;color:#f0ece4;letter-spacing:.10em;margin-top:-6px;">SCAN</div>
        <div style="font-size:.62rem;letter-spacing:.22em;color:#7a756e;text-transform:uppercase;margin-top:.35rem;">
            Ingredient Intelligence
        </div>
    </div>
    <hr style="border-color:rgba(201,169,110,.18); margin:.4rem 0 1rem;">
    """, unsafe_allow_html=True)

    st.markdown("### Skin Profile")
    
    skin_type = st.selectbox(
        "Skin Type",
        ["Normal", "Dry", "Oily", "Combination", "Sensitive", "Acne-Prone", "Mature"]
    )

    skin_concerns = st.multiselect(
        "Skin Concerns",
        [
            "Acne", "Hyperpigmentation", "Anti-aging", "Redness",
            "Dryness", "Oiliness", "Dark circles", "Pores",
            "Eczema", "Rosacea"
        ]
    )

    allergies = st.text_input(
        "Known Allergies",
        placeholder="e.g. fragrance, lanolin"
    )

    st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

    st.markdown("### Analysis Settings")

    strictness = st.select_slider(
        "Strictness",
        options=["Lenient", "Balanced", "Strict"],
        value="Balanced"
    )

    show_cosdna = st.toggle("Show CosDNA Functions", value=True)

    st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size:.72rem;color:#7a756e;text-align:center;line-height:1.7;">
        🧬 DermaScan v2.0<br>
        <span style="color:#c9a96e;">AI-powered skincare analysis</span><br>
        Based on EWG · INCI · CosDNA
    </div>
    """, unsafe_allow_html=True)


# ── Hero Banner ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">Derma<span>Scan</span></div>
    <div class="hero-tagline">Advanced Skincare Ingredient Intelligence</div>
    <div class="hero-desc">
        Decode what's really in your skincare. Upload a product image or paste ingredients for toxicity analysis, safety rating and personalized skin compatibility insights.
    </div>
</div>
""", unsafe_allow_html=True)


# ── Input Section ────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "Upload",
    "Paste",
    "Explorer"
])

ingredients_text = ""


# ── Tab 1 Upload ─────────────────────────────────────────────────────────────
with tab1:

    st.markdown(
        '<div class="ds-card-title">Upload Product Label</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tip-box">📌 Upload a clear image of the ingredient label. Good lighting improves OCR accuracy.</div>',
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "",
        type=["jpg", "jpeg", "png", "webp", "bmp"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Product Label",
            use_container_width=True
        )

        with st.spinner("Extracting ingredients..."):
            extracted = extract_text_from_image(image)

        st.markdown("**Extracted Text**")

        ingredients_text = st.text_area(
            "Edit if needed:",
            value=extracted,
            height=220,
            key="ocr_text"
        )


# ── Tab 2 Paste ──────────────────────────────────────────────────────────────
with tab2:

    st.markdown(
        '<div class="ds-card-title">Paste Ingredients List</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tip-box">📌 Paste full INCI list from packaging or website.</div>',
        unsafe_allow_html=True
    )

    sample_ingredients = """
Water, Glycerin, Niacinamide, Dimethicone, Phenoxyethanol,
Fragrance, Retinol, Salicylic Acid, Titanium Dioxide,
Zinc Oxide, Parabens, Hyaluronic Acid, Vitamin C
"""

    manual_text = st.text_area(
        "",
        placeholder=f"Example:\n{sample_ingredients}",
        height=220,
        key="manual_text",
        label_visibility="collapsed"
    )

    if manual_text:
        ingredients_text = manual_text


# ── Tab 3 Explorer ───────────────────────────────────────────────────────────
with tab3:

    st.markdown(
        '<div class="ds-card-title">🔎 Single Ingredient Lookup</div>',
        unsafe_allow_html=True
    )

    search_term = st.text_input(
        "Search Ingredient",
        placeholder="e.g. retinol, niacinamide, parabens"
    )

    if search_term:

        results = [
            (k, v)
            for k, v in INGREDIENT_DATABASE.items()
            if search_term.lower() in k.lower()
        ]

        if results:

            for name, data in results[:8]:

                risk_color = {
                    "Safe": "#5da882",
                    "Low": "#8eb85a",
                    "Moderate": "#d4a843",
                    "High": "#d4733a",
                    "Danger": "#c94f4f"
                }.get(data["risk"], "#7a756e")

                st.markdown(f"""
                <div style="
                    background:var(--bg-secondary);
                    border:1px solid var(--border);
                    border-radius:12px;
                    padding:.9rem 1rem;
                    margin-bottom:.7rem;
                ">
                    <div style="display:flex;justify-content:space-between;gap:.5rem;">
                        <span style="font-family:'DM Mono',monospace;color:#f0ece4;font-size:.88rem;">
                            {name.title()}
                        </span>

                        <span style="color:{risk_color};font-size:.72rem;font-weight:700;">
                            ⬤ {data['risk']}
                        </span>
                    </div>

                    <div style="color:#b8b0a4;font-size:.78rem;margin-top:.35rem;">
                        {data.get('function','—')} · EWG: {data.get('ewg_score','N/A')}
                    </div>

                    <div style="color:#7a756e;font-size:.76rem;margin-top:.3rem;">
                        {data.get('description','')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.markdown(
                '<div class="warn-box">No matching ingredients found in database.</div>',
                unsafe_allow_html=True
            )

# ── Analyze Button ────────────────────────────────────────────────────────────
st.divider()

analyze_clicked = st.button(
    "🔬 ANALYZE INGREDIENTS",
    use_container_width=True,
    type="primary"
)

if analyze_clicked:

    if not ingredients_text.strip():
        st.warning("Please enter or upload ingredients to analyze.")

    else:
        with st.spinner("Analyzing ingredients..."):

            parsed = parse_ingredients_text(ingredients_text)

            results = analyze_ingredients(
                parsed,
                skin_type,
                skin_concerns,
                allergies,
                strictness
            )

        if not results.get("found"):
            st.error(
                "Could not identify any known ingredients. "
                "Please check the input."
            )

        else:

               # ── Overview Score ────────────────────────────────────────────────
       # ── Overview Score TEST ─────────────────────────

            score = results["toxicity_score"]

            verdict = (
                "Excellent – Clean & Safe Formula" if score <= 2 else
                "Good – Mostly Safe with Minor Concerns" if score <= 4 else
                "Moderate – Some Ingredients Need Attention" if score <= 6 else
                "High Concern – Contains Problematic Ingredients" if score <= 8 else
                "Danger – Contains Harmful Substances"
            )

            st.subheader("Toxicity Score")
            st.metric("Score", f"{score}/10")
            st.success(verdict)
            st.write(results["verdict_detail"])
            st.write(f"Grade: {results['grade']}")
                # ── Metrics ───────────────────────────────────────────────────────
        total = len(results["found"])

        safe_n = sum(
            1 for i in results["found"]
            if i["risk"] in ["Safe", "Low"]
        )

        concern_n = sum(
            1 for i in results["found"]
            if i["risk"] in ["Moderate", "High", "Danger"]
        )

        unknown_n = len(results["unknown"])

        st.markdown("### 📊 Quick Summary")

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        with col1:
            st.metric("Total", total)

        with col2:
            st.metric("Safe", safe_n)

        with col3:
            st.metric("Concern", concern_n)

        with col4:
            st.metric("Unknown", unknown_n)

               # ── Skin Compatibility ────────────────────────────────────────────
        compat = results.get("skin_compatibility", {})

        if compat:

            st.markdown(f"### 💆 Compatibility for {skin_type} Skin")

            for attr, val in compat.items():

                if val >= 70:
                    bar_color = "🟢"
                elif val >= 40:
                    bar_color = "🟡"
                else:
                    bar_color = "🔴"

                col1, col2 = st.columns([3, 1])

                with col1:
                    st.write(f"{bar_color} {attr}")

                with col2:
                    st.write(f"**{val}%**")

                st.progress(val / 100)

        # ── Charts (Stacked for Mobile) ───────────────────────────────────
        risk_counts = {
            "Safe": 0,
            "Low": 0,
            "Moderate": 0,
            "High": 0,
            "Danger": 0
        }

        for ing in results["found"]:
            risk_counts[ing["risk"]] += 1

        fig_donut = go.Figure(go.Pie(
            labels=list(risk_counts.keys()),
            values=list(risk_counts.values()),
            hole=0.62,
            marker_colors=[
                "#5da882",
                "#8eb85a",
                "#d4a843",
                "#d4733a",
                "#c94f4f"
            ],
            textinfo="none",
            hovertemplate="<b>%{label}</b><br>%{value} ingredients<extra></extra>"
        ))

        fig_donut.update_layout(
            title="Risk Distribution",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#b8b0a4"),
            margin=dict(t=45, b=15, l=15, r=15),
            height=300,
            annotations=[dict(
                text=f"<b>{total}</b><br>Total",
                x=0.5,
                y=0.5,
                showarrow=False,
                font=dict(size=16, color="#f0ece4")
            )]
        )

        st.plotly_chart(
            fig_donut,
            use_container_width=True,
            config={"displayModeBar": False}
        )

        # ── Category Chart ────────────────────────────────────────────────
        cat_counts = {}

        for ing in results["found"]:
            cat = ing.get("category", "Other")
            cat_counts[cat] = cat_counts.get(cat, 0) + 1

        sorted_cats = sorted(
            cat_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        fig_bar = go.Figure(go.Bar(
            x=[x[1] for x in sorted_cats],
            y=[x[0] for x in sorted_cats],
            orientation="h",
            marker_color="#c9a96e",
            text=[x[1] for x in sorted_cats],
            textposition="outside"
        ))

        fig_bar.update_layout(
            title="By Function Category",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(showgrid=False, visible=False),
            yaxis=dict(color="#b8b0a4"),
            font=dict(color="#b8b0a4"),
            margin=dict(t=45, b=15, l=15, r=35),
            height=320
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True,
            config={"displayModeBar": False}
        )

# ── EWG Score Distribution ────────────────────────────────────────
ewg_scores = [
    i.get("ewg_score", 0)
    for i in results["found"]
    if i.get("ewg_score") is not None
]

if ewg_scores:

    fig_hist = go.Figure(go.Histogram(
        x=ewg_scores,
        nbinsx=10,
        marker=dict(
            color=ewg_scores,
            colorscale=[
                [0, "#5da882"],
                [0.35, "#8eb85a"],
                [0.55, "#d4a843"],
                [0.75, "#d4733a"],
                [1, "#c94f4f"]
            ],
            line=dict(color="rgba(0,0,0,.25)", width=1)
        ),
        hovertemplate="EWG Score %{x}<br>Count %{y}<extra></extra>"
    ))

    fig_hist.update_layout(
        title="EWG Hazard Distribution",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#b8b0a4"),
        xaxis=dict(
            title="EWG Score",
            gridcolor="rgba(255,255,255,.04)"
        ),
        yaxis=dict(
            title="Ingredients",
            gridcolor="rgba(255,255,255,.04)"
        ),
        margin=dict(t=45, b=20, l=20, r=10),
        height=280
    )

    st.plotly_chart(
        fig_hist,
        use_container_width=True,
        config={
            "displayModeBar": False,
            "scrollZoom": False,
            "doubleClick": False,
            "responsive": True
        }
    )

# ── Allergen Alerts ───────────────────────────────────────────────
if results.get("allergen_alerts"):

    alerts = " · ".join(results["allergen_alerts"])

    st.warning(f"⚠️ Allergen Alerts: {alerts}")

       # ── Flagged Ingredients ───────────────────────────────────────────
flagged = [
    i for i in results["found"]
    if i["risk"] in ["High", "Danger"]
]

if flagged:

    st.subheader("🚨 High-Concern Ingredients")

    for ing in flagged:

        risk_text = ing["risk"]
        risk_icon = "🔴" if risk_text == "Danger" else "🟠"

        with st.container(border=True):

            st.markdown(
                f"**{risk_icon} {ing['name'].title()}**  \n"
                f"Risk Level: **{risk_text}**"
            )

            if ing.get("function"):
                st.caption(f"Function: {ing['function']}")

            if ing.get("description"):
                st.write(ing["description"])

            if ing.get("concern"):
                st.error(f"Concern: {ing['concern']}")

# ── Full Ingredient Table ────────────────────────────────────────
with st.expander("📋 Full Ingredient Analysis Table", expanded=False):

    df = pd.DataFrame(results["found"])

    display_cols = [
        c for c in [
            "name",
            "risk",
            "category",
            "function",
            "ewg_score",
            "description"
        ]
        if c in df.columns
    ]

    df_display = df[display_cols].copy()

    df_display.columns = [
        c.replace("_", " ").title()
        for c in display_cols
    ]

    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True
    )

    # ── CSV Export (WebView Safe) ────────────────────────────────
    csv_text = df_display.to_csv(index=False)

    st.text_area(
        "📄 Copy / Save CSV Report",
        value=csv_text,
        height=220
    )

    st.info(
        "In Android APK/WebView, downloads may fail. "
        "Use this CSV text to copy, share, or save manually."
    )
# ── Recommendations ───────────────────────────────────────────────
recs = get_skin_type_recommendation(
    skin_type,
    results,
    skin_concerns
)

if recs:
    st.subheader("💡 Personalized Recommendations")

    for r in recs:
        st.success(r)

# ── Radar Chart ──────────────────────────────────────────────────
radar_cats = [
    "Hydration",
    "Brightening",
    "Anti-aging",
    "Sun Protection",
    "Soothing",
    "Exfoliation"
]

radar_vals = [
    results.get("radar", {}).get(c, np.random.randint(20, 80))
    for c in radar_cats
]

radar_vals += [radar_vals[0]]
radar_cats_full = radar_cats + [radar_cats[0]]

fig_radar = go.Figure(go.Scatterpolar(
    r=radar_vals,
    theta=radar_cats_full,
    fill="toself",
    fillcolor="rgba(201,169,110,.10)",
    line=dict(color="#c9a96e", width=2),
    marker=dict(size=5, color="#c9a96e")
))

fig_radar.update_layout(
    polar=dict(
        bgcolor="rgba(0,0,0,0)",
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    title="Formula Benefit Profile",
    height=340
)

st.plotly_chart(
    fig_radar,
    use_container_width=True,
    config={
        "displayModeBar": False,
        "scrollZoom": False,
        "doubleClick": False,
        "responsive": True
    }
)
# ── Unknown Ingredients ─────────────────────────────────────────
if results["unknown"]:

    with st.expander(
        f"❓ {len(results['unknown'])} Unrecognized Ingredients",
        expanded=False
    ):

        st.info(
            "These ingredients were not found in our database. "
            "They may be trademarked names, INCI variants, "
            "spelling variants, or newer compounds."
        )

        unknown_text = " • ".join(results["unknown"])

        st.write(unknown_text)

# ── Footer ───────────────────────────────────────────────────────────
st.markdown("""
<div class="gold-divider"></div>

<div style='text-align:center;
padding:24px 10px;
color:#7a756e;
font-size:13px;
line-height:1.7;'>

<div style='font-family:Cormorant Garamond,serif;
font-size:24px;
color:#c9a96e;
margin-bottom:8px;'>
DERMASCAN
</div>

For educational & informational purposes only.<br>
Always consult a dermatologist for medical advice.<br><br>

Decode every formula. Choose skincare with confidence.

</div>
""", unsafe_allow_html=True)
