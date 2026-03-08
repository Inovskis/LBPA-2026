import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Izglītība", "Kas notiek pasaulē un kas — Latvijā")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="stat-card">
            <h4 style="color:#00838F;">NTNU, Norvēģija</h4>
            <p class="slide-text">
            Kurss "Python for Structural Engineering" — pirmais gadagājums 2026. gadā.
            Tēmas: drošums, optimizācija, mašīnmācīšanās, dinamika.
            </p>
        </div>

        <div class="stat-card">
            <h4 style="color:#00838F;">Cal Poly, ASV</h4>
            <p class="slide-text">
            Architectural Engineering Computing — Python kā daļa no inženieru programmas.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="accent-box">
            <p class="slide-text"><strong>Latvijā</strong></p>
            <p class="slide-text">
            Šobrīd Python nav integrēts RTU vai LLU būvniecības programmās
            kā projektēšanas rīks.
            </p>
            <p class="slide-text">
            Vai LBPA varētu būt vieta, kur sākt šo sarunu?
            Nevis obligāts kurss — bet seminārs, eksperiments, iespēja.
            </p>
        </div>
        """, unsafe_allow_html=True)
