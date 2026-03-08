import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Prognozes un determinisms",
                 "Kāpēc AI nedrīkst rēķināt konstrukcijas")

    st.markdown("""
    <p class="slide-text">
    AI valodas modeļi ir statistiskas prognozes mašīnas. Tie ģenerē tekstu
    un kodu, balstoties uz varbūtībām — nevis uz fiziku vai standartiem.
    Tie var kļūdīties. Un tie kļūdīsies.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="compare-old">
            <h4 style="color:#c0392b;">AI prognoze</h4>
            <p class="slide-text">Statistisks modelis — var kļūdīties<br>
            Halucinācijas — izdomā formulas<br>
            Nav garantijas<br>
            Katru reizi var dot citu rezultātu</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="compare-new">
            <h4 style="color:#27ae60;">Python bibliotēka</h4>
            <p class="slide-text">Determinēts rezultāts<br>
            Validēta pret standartu<br>
            Atvērtā pirmkoda — auditējama<br>
            Vienāda ievade = vienāds rezultāts</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="accent-box">
        Pieeja, ko es lietoju: <strong>AI raksta kodu</strong>, bet formulas nāk no
        <strong>validētām bibliotēkām</strong>. Rezultāts ir determinēts.
        Inženieris pārbauda.
    </div>
    """, unsafe_allow_html=True)
