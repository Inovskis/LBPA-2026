import streamlit as st


def apply_theme():
    """Inject custom CSS for light presentation theme matching kforma.lv."""
    st.markdown("""
    <style>
    /* Hide Streamlit chrome for presentation */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Typography */
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

    /* Accent elements */
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

    /* Progress bar */
    .progress-bar-bg {
        background: #e8ecf1;
        border-radius: 3px;
        height: 4px;
        width: 100%;
        margin-bottom: 0.5rem;
    }

    .progress-bar-fill {
        background: #00BCD4;
        border-radius: 3px;
        height: 4px;
        transition: width 0.3s ease;
    }

    /* Code blocks */
    .stCodeBlock {
        border: 1px solid #e0e6ed;
        border-radius: 6px;
    }

    /* Comparison columns */
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

    /* Fade in animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }

    /* Bottom padding for nav bar */
    .block-container {
        padding-bottom: 80px !important;
        max-width: 1000px;
    }

    /* Quote style */
    blockquote {
        border-left: 3px solid #00BCD4;
        padding-left: 1rem;
        color: #5d6d7e;
        font-style: italic;
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        font-size: 1rem;
        color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)
