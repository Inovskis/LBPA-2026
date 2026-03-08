import streamlit as st
from components.media import logo_header


def render():
    logo_header()

    st.markdown("""
    <div style="text-align:center; margin-top:3rem;" class="fade-in">
        <h1 style="font-size:3.2rem; font-weight:700; color:#ffffff; margin-bottom:0.5rem;">
            AI un Python
        </h1>
        <h1 style="font-size:3.2rem; font-weight:700; color:#00BCD4; margin-bottom:2rem;">
            Būvkonstrukciju Projektēšanā
        </h1>
        <p style="font-size:1.4rem; color:#b0bec5;">
            Nauris — KFORMA SIA
        </p>
        <p style="font-size:1.1rem; color:#78909c;">
            LBPA Kongress 2026
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-top:4rem;">
        <p style="font-size:1rem; color:#546e7a;">
            design.kforma.lv
        </p>
    </div>
    """, unsafe_allow_html=True)
