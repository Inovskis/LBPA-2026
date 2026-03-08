import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Praktiski piemēri", "Kas izdevās un kas gandrīz neizdevās")

    st.markdown("""
    | Uzdevums | Tradicionāli | Ar AI | Piezīme |
    |----------|:---:|:---:|---------|
    | SVG vizualizācija | 4-6 h | 30 min | Darbojās uzreiz |
    | MC2010 integrācija | 2-3 h | 20 min | AI atrada vienību kļūdu |
    | Deployment kļūda | 1-2 h | 15 min | 2 rindu labojums |
    | Jauna funkcionalitāte | 2-4 h | 45 min | Vajadzēja korekcijas |
    """)

    tab1, tab2 = st.tabs(["Kad AI palīdzēja", "Kad AI kļūdījās"])

    with tab1:
        st.markdown("""
        <p class="slide-text">
        <strong>MC2010 integrācija:</strong> Bibliotēkas funkcija atgrieza spēku (N),
        nevis spriegumu (MPa). Rezultāts bija 271,562 MPa — acīmredzami absurds.
        AI identificēja vienību nesaderību ātrāk nekā es to būtu pamanījis
        dokumentācijā.
        </p>
        """, unsafe_allow_html=True)

        st.code("# AI risinājums:\nv_rdc = k_psi * sqrt(fck) / gamma_c  # MPa, nevis N", language="python")

    with tab2:
        st.markdown("""
        <p class="slide-text">
        AI regulāri pieļauj kļūdas aprēķinu loģikā — piemēram, sajaucot
        koordinātu sistēmas, nepareizi pārveidojot vienības, vai vienkārši
        izdomājot formulu, kas izskatās pareiza, bet tāda nav.
        </p>

        <p class="slide-text">
        Tieši tāpēc vienmēr jālieto <strong>validētas bibliotēkas</strong>,
        nevis AI ģenerētas formulas.
        </p>
        """, unsafe_allow_html=True)
