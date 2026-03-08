import streamlit as st
from components.media import logo_header


def render():
    logo_header()

    st.markdown("""
    <div style="text-align:center; margin-top:4rem;" class="fade-in">
        <h1 style="font-size:2.8rem; font-weight:300; color:#2c3e50; margin-bottom:0.5rem;">
            Mākslīgo neironu tīklu lietošana
        </h1>
        <h1 style="font-size:2.8rem; font-weight:300; color:#00838F; margin-bottom:2rem;">
            Būvkonstrukciju Projektēšanā
        </h1>
        <p style="font-size:1.1rem; color:#7f8c8d; font-weight:300;">
            Personīgā pieredze, eksperimenti un novērojumi
        </p>
        <p style="font-size:1rem; color:#95a5a6; margin-top:2rem;">
            Nauris &middot; KFORMA SIA
        </p>
    </div>
    """, unsafe_allow_html=True)
