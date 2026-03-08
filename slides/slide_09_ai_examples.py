import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("AI Piemēri", "Reāli gadījumi no design.kforma.lv izstrādes")

    st.markdown("""
    | Uzdevums | Bez AI | Ar AI | Ietaupījums |
    |----------|--------|-------|-------------|
    | SVG vizualizācija | 4-6 h | 30 min | **~10x** |
    | MC2010 integrācija | 2-3 h | 20 min | **~8x** |
    | Railway deployment fix | 1-2 h | 15 min | **~6x** |
    | Jauna funkcionalitāte | 2-4 h | 45 min | **~4x** |
    """)

    tab1, tab2, tab3 = st.tabs(["SVG Izveide", "Kļūdu Diagnostika", "Deployment"])

    with tab1:
        st.markdown("""
        **Uzdevums:** Interaktīvs caurspiešanas plānskats ar kolonnu un kritisko perimetru

        **AI izveidoja:** 3 JavaScript objektus (~400 rindas), interaktīva vizualizācija kas atjaunojas reāllaikā

        **Laiks:** 30 minūtes (tradicionāli 4-6 stundas)
        """)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.error("MC2010 v_Rd,c = 271,562 MPa ???")
            st.caption("Jābūt ~0.5-1.5 MPa")
        with col2:
            st.success("AI diagnostika: Funkcija atgriež SPĒKU (N), nevis SPRIEGUMU (MPa)")
            st.code("# Risinājums:\nv_rdc = k_psi * sqrt(fck) / gamma_c  # MPa", language="python")

    with tab3:
        st.markdown("""
        **Problēma:** "Bad Gateway" pēc Railway redeploy

        **AI atklājums:** Hardkodēts ports `app.run(port=5000)`
        """)
        st.code("# Fix (2 rindas):\nport = int(os.environ.get('PORT', 5000))\napp.run(port=port, host='0.0.0.0')", language="python")

    st.markdown("""
    <div class="accent-box" style="text-align:center;">
        Vidēji <strong>~5x ātrāk</strong> ar AI palīdzību
    </div>
    """, unsafe_allow_html=True)
