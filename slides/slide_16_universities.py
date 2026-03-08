import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Universitātes", "Python inženieru izglītībā")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Pasaulē
        """)

        st.markdown("""
        <div class="stat-card">
            <h4 style="color:#00BCD4;">NTNU (Norvēģija)</h4>
            <p class="slide-text">
            Kurss <strong>"Python for Structural Engineering"</strong> (KT6198)<br>
            2026. gada pavasaris — pirmais gadagājums<br>
            Tēmas: drošums, optimizācija, ML, dinamika
            </p>
        </div>

        <div class="stat-card">
            <h4 style="color:#00BCD4;">Cal Poly (ASV)</h4>
            <p class="slide-text">
            Architectural Engineering Computing<br>
            Python manuālis studentiem
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        ### Latvijā
        """)

        st.markdown("""
        <div class="accent-box">
            <h4 style="margin-top:0;">Ko darīt?</h4>
            <ul>
                <li>Integrēt Python RTU/LLU inženieru programmās</li>
                <li>Izveidot specializētu kursu (pēc NTNU parauga)</li>
                <li>Semināri praktizējošiem inženieriem</li>
                <li>LBPA kā iniciatīvas virzītājs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        > *Ja Norvēģija var — mēs arī varam.*
        """)
