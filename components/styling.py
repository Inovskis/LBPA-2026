import streamlit as st


def apply_theme():
    """Inject custom CSS for light presentation theme matching kforma.lv."""
    st.markdown("""
    <style>
    /* ===== Fullscreen / Presentation Mode ===== */
    /* Hide ALL Streamlit chrome */
    header[data-testid="stHeader"] { display: none !important; }
    footer { display: none !important; }
    .stDeployButton { display: none !important; }
    #MainMenu { display: none !important; }
    div[data-testid="stToolbar"] { display: none !important; }
    div[data-testid="stDecoration"] { display: none !important; }
    .stApp > header { display: none !important; }

    /* Reduce top padding — content starts higher */
    .stApp > div:first-child {
        padding-top: 0 !important;
    }
    section[data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem !important;
    }

    /* Maximise content area */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 80px !important;
        max-width: 1100px;
    }

    /* ===== Typography ===== */
    .slide-title {
        font-size: 2.4rem;
        font-weight: 300;
        color: #2c3e50;
        margin-bottom: 1rem;
        border-bottom: 3px solid #00BCD4;
        padding-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }

    .slide-subtitle {
        font-size: 1.2rem;
        color: #7f8c8d;
        margin-bottom: 1.5rem;
        font-weight: 300;
        font-style: italic;
    }

    .slide-text {
        font-size: 1.05rem;
        line-height: 1.8;
        color: #34495e;
    }

    /* ===== Accent elements ===== */
    .accent-box {
        background: #f0fafa;
        border-left: 4px solid #00BCD4;
        border-radius: 4px;
        padding: 1.2rem 1.5rem;
        color: #2c3e50;
        margin: 1rem 0;
        font-size: 1.05rem;
    }

    .stat-card {
        background: #ffffff;
        border: 1px solid #e0e6ed;
        border-top: 3px solid #00BCD4;
        border-radius: 6px;
        padding: 1.2rem 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .stat-number {
        font-size: 2.2rem;
        font-weight: 300;
        color: #00BCD4;
    }

    .stat-label {
        font-size: 0.95rem;
        color: #7f8c8d;
    }

    /* ===== Progress bar (thin & subtle) ===== */
    .progress-bar-bg {
        background: #e8ecf1;
        border-radius: 2px;
        height: 2px;
        width: 100%;
        margin-bottom: 0.2rem;
    }

    .progress-bar-fill {
        background: #00BCD4;
        border-radius: 2px;
        height: 2px;
        transition: width 0.3s ease;
    }

    /* ===== Slide counter ===== */
    .slide-counter {
        text-align: center;
        color: #5d6d7e;
        font-size: 0.95rem;
        font-weight: 500;
        margin-bottom: 0.3rem;
        letter-spacing: 1px;
    }

    /* ===== Navigation buttons — large & touch-friendly ===== */
    div[data-testid="stHorizontalBlock"] button {
        font-size: 1.15rem !important;
        padding: 0.7rem 1.5rem !important;
        min-height: 52px !important;
        border-radius: 8px !important;
    }

    /* ===== Code blocks ===== */
    .stCodeBlock {
        border: 1px solid #e0e6ed;
        border-radius: 6px;
    }

    /* ===== Comparison columns ===== */
    .compare-old {
        background: #fdf2f2;
        border-radius: 6px;
        padding: 1.2rem;
        border-left: 4px solid #e74c3c;
    }

    .compare-new {
        background: #f0faf0;
        border-radius: 6px;
        padding: 1.2rem;
        border-left: 4px solid #27ae60;
    }

    /* ===== Fade in animation ===== */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }

    /* ===== Quote style ===== */
    blockquote {
        border-left: 3px solid #00BCD4;
        padding-left: 1rem;
        color: #5d6d7e;
        font-style: italic;
    }

    /* ===== Expander styling ===== */
    .streamlit-expanderHeader {
        font-size: 1rem;
        color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)
