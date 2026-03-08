import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Citi rīki", "Es neesmu vienīgais — šī ir ekosistēma")

    st.markdown("""
    <p class="slide-text">
    Arvien vairāk platformu un rīku parādās tieši inženieriem.
    Šeit daži, ko esmu novērojis.
    </p>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "Viktor.AI",
        "CalcTree",
        "Calcpad",
        "GPAI"
    ])

    with tab1:
        st.markdown("""
        <p class="slide-text">
        <strong>Viktor.AI</strong> — platforma, kurā inženieri veido web aplikācijas
        ar Python. Integrējas ar SAP2000, ETABS. Nesen pievienoti AI aģenti.
        </p>
        <p style="color:#7f8c8d;">viktor.ai</p>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <p class="slide-text">
        <strong>CalcTree</strong> — mākoņa aprēķinu platforma ar Python un MathJS dzinēju.
        Integrējas ar Excel un Grasshopper. Lietotāji: Arup, Jacobs, WSP.
        </p>
        <p style="color:#7f8c8d;">calctree.com</p>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <p class="slide-text">
        <strong>Calcpad</strong> — bezmaksas open-source kalkulators ar 100+ Eirokodeksu
        šabloniem. Ģenerē HTML atskaites. Nav nepieciešamas programmēšanas prasmes.
        </p>
        <p style="color:#7f8c8d;">calcpad.eu</p>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("""
        <p class="slide-text">
        <strong>GPAI</strong> — AI risinātājs STEM uzdevumiem. Nofotografē uzdevumu,
        saņem soli-pa-solim risinājumu. Pārbauda ar vairākiem AI modeļiem.
        </p>
        <p style="color:#7f8c8d;">gpai.app</p>
        """, unsafe_allow_html=True)
