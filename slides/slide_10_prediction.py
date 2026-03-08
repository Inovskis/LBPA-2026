import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("AI Prognozes vs Determinisms",
                 "Kāpēc AI nevar aizstāt inženieri, bet var palīdzēt")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="compare-old">
            <h3 style="color:#ef5350;">AI (LLM) Prognozes</h3>
            <ul class="slide-text">
                <li>Statistiski modeļi — <strong>var kļūdīties</strong></li>
                <li>Halucinācijas — izdomā formulas</li>
                <li>Nav garantijas par pareizību</li>
                <li>Atkarīgi no apmācības datiem</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="compare-new">
            <h3 style="color:#66bb6a;">Python Bibliotēkas</h3>
            <ul class="slide-text">
                <li><strong>Determinēts</strong> rezultāts</li>
                <li>Validētas pret standartiem</li>
                <li>Vienāda ievade = vienāds rezultāts</li>
                <li>Atvērtā pirmkods — auditējams</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="accent-box">
        <p style="font-size:1.3rem; margin:0; text-align:center;">
            <strong>AI raksta kodu</strong> &rarr; <strong>Python bibliotēkas nodrošina pareizību</strong> &rarr; <strong>Inženieris verificē</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Piemērs:** AI palīdz uzrakstīt `structuralcodes` izsaukumu, bet formula pati nāk no
    validētas bibliotēkas — rezultāts vienmēr ir determinēts un pareizs.
    """)
