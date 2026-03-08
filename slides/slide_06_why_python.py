import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Kāpēc Python?", "Inženieru izvēle Nr. 1")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Bezmaksas un atvērts
        - Nav licences maksu
        - Liela kopiena (>10M izstrādātāju)

        ### Bagāta bibliotēku ekosistēma
        - 500,000+ pakotnes PyPI
        - Specializētas inženieru bibliotēkas

        ### Lasāms kods
        - Kods lasa kā formula
        - Viegli auditējams
        """)

    with col2:
        st.markdown("### EC2 formula Python kodā:")
        st.code("""
# EC2 §6.2.2 — Bīdes izturība bez šķērsstiegrojuma
import math

k = min(1 + math.sqrt(200 / d), 2.0)
rho_l = min(As / (b * d), 0.02)

v_Rd_c = (0.18 / gamma_c) * k * (100 * rho_l * fck) ** (1/3) * b * d

# Rezultāts uzreiz saprotams!
        """, language="python")

        st.markdown("""
        <div class="accent-box">
            Kods = Dokumentācija = Aprēķins
        </div>
        """, unsafe_allow_html=True)
