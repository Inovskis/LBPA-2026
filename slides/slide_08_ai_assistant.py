import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("AI Kā Izstrādes Palīgs", "Claude Code uz atsevišķas Linux mašīnas")

    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown("""
        ### Kas tas ir?

        **Claude Code** — AI asistents komandrindā:
        - Lasa un raksta kodu
        - Izpilda komandas
        - Saprot projekta kontekstu
        - Meklē dokumentāciju

        ### Kāpēc atsevišķa Linux mašīna?
        - Izolēta vide
        - Nepārtraukta pieejamība
        - Paralēla izstrāde
        """)

    with col2:
        st.markdown("### Tipiska sesija:")
        st.code("""
$ claude

> Pievieno SVG vizualizāciju caurspiešanas modulim
  ar kolonnas skatu no augšas un kritisko perimetru

Claude: Es izveidošu vizualizācijas sistēmu ar trim
        komponentiem: PunchingViz, SectionViz,
        PunchingResultsViz...

        [Izveido ~400 rindas JavaScript]
        [Testē ar reāliem datiem]
        [Labo layout problēmas]

Rezultāts: Pilna funkcionalitāte 30 minūtēs
        """, language="text")
