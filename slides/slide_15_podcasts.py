import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Podkāsti un Resursi", "Kur mācīties tālāk")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Flocode Podcast
        **James O'Reilly** — Python + Inženierija

        Ieteicamās epizodes:
        - **#058** Morten Engen — *Structuralcodes* bibliotēka
        - **#042** Craig Brinck — *PyNite* FEM analīze
        - **#048** Connor Ferster — Automatizācija
        - **#039** Dr. MZ Naser — ML konstrukcijās

        flocode.substack.com
        """)

    with col2:
        st.markdown("""
        ### Mācību Resursi

        | Resurss | Apraksts |
        |---------|----------|
        | **StructuralPython** | structuralpython.com |
        | **EngineeringSkills** | engineeringskills.com |
        | **civils.ai** | Python kurss inženieriem |
        | **Udemy** | Programming for Structural Engineers |

        ### Zinātniskie raksti
        - Gustafsson & McBain (2020) — *scikit-fem* (JOSS)
        """)
