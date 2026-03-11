import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Kāpēc Python", "Ne tāpēc ka modīgi — tāpēc ka praktiski")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <p class="slide-text">
        Python nav vienīgā iespēja. Bet tas ir valoda, kurā inženieru formulas
        izskatās kā formulas — nevis kā programmēšana.
        </p>

        <p class="slide-text">
        Bibliotēku ekosistēma ir tāda, ka daudz ko nevajag rakstīt no nulles.
        Kāds jau ir implementējis EC2 formulas. Kāds jau ir uztaisījis FEM risinātāju.
        Mūsu darbs ir salikt kopā.
        </p>

        <p class="slide-text">
        Un vēl viens aspekts, kas kļūst arvien svarīgāks: Python pamatā tiek rakstīts
        kā teksts — lasāms visā garumā, bez slēptiem slāņiem. Protams, kods var būt garš,
        bet AI to var izlasīt brīvi. Tas padara Python par ideālu valodu darbam
        kopā ar lielajiem valodu modeļiem.
        </p>

        <p class="slide-text" style="color:#7f8c8d;">
        Nav licences maksu. Nav vendor lock-in. Kods ir tavs.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.code("""
# EC2 §6.2.2 — bīdes izturība
import math

k = min(1 + math.sqrt(200 / d), 2.0)
rho_l = min(As / (b * d), 0.02)

v_Rd_c = (0.18 / gamma_c) \\
       * k * (100 * rho_l * fck) ** (1/3) \\
       * b * d

# Lasāms. Izsekojams. Pārbaudāms.
        """, language="python")
