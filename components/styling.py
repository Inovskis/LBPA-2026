import streamlit as st


def apply_theme():
    """Apply custom CSS theme for the LBPA 2026 presentation."""
    st.markdown(
        """
        <style>
        /* ── Hide Streamlit chrome ── */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* ── Core colours ── */
        :root {
            --lbpa-dark: #32373c;
            --kforma-cyan: #00BCD4;
            --bg-primary: #1a1f2e;
            --bg-deep: #151a28;
            --text-primary: #ffffff;
            --text-muted: #b0b8c8;
        }

        /* ── Slide container ── */
        .slide-container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 1.5rem 2rem 2rem 2rem;
        }

        /* ── Typography ── */
        .slide-title {
            font-size: 2.6rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 0.2rem;
            border-bottom: 3px solid var(--kforma-cyan);
            padding-bottom: 0.5rem;
        }

        .slide-subtitle {
            font-size: 1.3rem;
            color: var(--kforma-cyan);
            margin-bottom: 1.5rem;
            font-weight: 400;
        }

        .slide-text {
            font-size: 1.1rem;
            line-height: 1.7;
            color: var(--text-primary);
        }

        /* ── Accent box ── */
        .accent-box {
            background: linear-gradient(135deg, var(--bg-deep), var(--lbpa-dark));
            border-left: 4px solid var(--kforma-cyan);
            border-radius: 0 8px 8px 0;
            padding: 1.2rem 1.5rem;
            margin: 1rem 0;
        }

        /* ── Stat cards ── */
        .stat-card {
            background: linear-gradient(135deg, var(--bg-deep), var(--lbpa-dark));
            border: 1px solid rgba(0, 188, 212, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }
        .stat-card:hover {
            transform: translateY(-2px);
            border-color: var(--kforma-cyan);
        }
        .stat-number {
            font-size: 2.4rem;
            font-weight: 700;
            color: var(--kforma-cyan);
            margin-bottom: 0.2rem;
        }
        .stat-label {
            font-size: 0.95rem;
            color: var(--text-muted);
        }

        /* ── Navigation ── */
        .nav-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: var(--bg-deep);
            border-top: 1px solid rgba(0, 188, 212, 0.2);
            padding: 0.5rem 2rem;
            z-index: 999;
        }

        /* ── Progress bar ── */
        .progress-bar-bg {
            width: 100%;
            height: 4px;
            background: var(--lbpa-dark);
            border-radius: 2px;
            margin-bottom: 0.4rem;
        }
        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--kforma-cyan), #4dd0e1);
            border-radius: 2px;
            transition: width 0.35s ease;
        }

        /* ── Comparison blocks ── */
        .compare-old {
            background: rgba(244, 67, 54, 0.12);
            border-left: 4px solid #f44336;
            border-radius: 0 8px 8px 0;
            padding: 1rem 1.2rem;
            margin: 0.5rem 0;
        }
        .compare-new {
            background: rgba(0, 188, 212, 0.12);
            border-left: 4px solid var(--kforma-cyan);
            border-radius: 0 8px 8px 0;
            padding: 1rem 1.2rem;
            margin: 0.5rem 0;
        }

        /* ── Fade-in animation ── */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(12px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .fade-in {
            animation: fadeIn 0.5s ease-out forwards;
        }

        /* ── Code block overrides ── */
        .stCodeBlock {
            border: 1px solid rgba(0, 188, 212, 0.25) !important;
            border-radius: 8px !important;
        }

        /* ── Bottom padding so content doesn't hide behind nav ── */
        .main .block-container {
            padding-bottom: 5rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
