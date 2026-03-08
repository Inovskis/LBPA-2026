import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Citi Labi Rīki", "Ekosistēma inženieriem")

    tab1, tab2, tab3, tab4 = st.tabs([
        "Viktor.AI",
        "CalcTree",
        "Calcpad",
        "GPAI"
    ])

    with tab1:
        st.markdown("""
        ### Viktor.AI — Low-Code Inženieru Platforma
        - Veido web apps ar dažām Python rindām
        - Integrējas ar SAP2000, ETABS, Excel
        - 2026 roadmap: AI agents + automatizētas darbplūsmas
        - **viktor.ai**
        """)

    with tab2:
        st.markdown("""
        ### CalcTree — Cloud Aprēķinu Platforma
        - Python & MathJS dzinējs
        - Integrējas ar Excel, Grasshopper, ETABS
        - Investīcijas no Foundamental VC
        - Lietotāji: Arup, Jacobs, WSP
        - **calctree.com**
        """)

    with tab3:
        st.markdown("""
        ### Calcpad — Bezmaksas Open-Source
        - Programmējams kalkulators inženieriem
        - 100+ Eirokodeksu šablonu
        - HTML atskaites ar formulām
        - Nav nepieciešamas programmēšanas prasmes
        - **calcpad.eu**
        """)

    with tab4:
        st.markdown("""
        ### GPAI — AI STEM Solver
        - Foto/PDF &rarr; risinājums ar vizualizāciju
        - Triple-verified (vairāki AI modeļi)
        - Soli-pa-solim skaidrojumi
        - **gpai.app**
        """)

        st.markdown("### Piemērs — vienkāršs prompts:")
        st.code("""
Prompt: "Calculate the bending capacity of a
        300x600mm RC beam, C30/37, 4x25 bottom"

GPAI: Provides step-by-step EC2 solution with
      diagrams and verification
        """, language="text")
