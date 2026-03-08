import streamlit as st
from components.navigation import slide_header
from components.media import show_image


def render():
    slide_header("Problēma", "Tradicionālo rīku ierobežojumi")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        <div class="stat-card">
            <h4 style="color:#ef5350;">Excel</h4>
            <p class="slide-text">Grūti izsekot formulas &bull; Nav versiju kontroles &bull; Kļūdas kopējot</p>
        </div>
        <div class="stat-card">
            <h4 style="color:#ef5350;">MathCAD</h4>
            <p class="slide-text">Dārga licence &bull; Ierobežotas vizualizācijas &bull; Nav web pieejamības</p>
        </div>
        <div class="stat-card">
            <h4 style="color:#ef5350;">Komerciālā programmatūra</h4>
            <p class="slide-text">"Black box" aprēķini &bull; Augsta cena &bull; Nav pielāgojama</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        show_image("btf_screenshot.jpg", caption="BTF Digital — tipisks komerciāls rīks")
