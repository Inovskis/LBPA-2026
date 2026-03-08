import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Infrastruktūra", "No koda līdz pieejamībai")

    st.markdown("""
    <p class="slide-text">
    Vēl viens aspekts, kas mainījies — publicēt web aplikāciju šodien
    ir vienkāršāk nekā jebkad. Nav nepieciešams savs serveris.
    </p>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="stat-card">
            <h4 style="color:#00838F;">Railway</h4>
            <p style="font-size:0.9rem; color:#5d6d7e;">
            Cloud hosting. Auto-deploy no GitHub.
            Piemēram, šāds projekts var darboties mākonī par dažiem eiro mēnesī.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stat-card">
            <h4 style="color:#00838F;">GitHub</h4>
            <p style="font-size:0.9rem; color:#5d6d7e;">
            Versiju kontrole. Kods ir pieejams, izsekojams, atjaunojams.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="stat-card">
            <h4 style="color:#00838F;">Streamlit</h4>
            <p style="font-size:0.9rem; color:#5d6d7e;">
            Python kods kļūst par web app.
            Šī prezentācija ir Streamlit app.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="stat-card">
            <h4 style="color:#00838F;">Docker</h4>
            <p style="font-size:0.9rem; color:#5d6d7e;">
            Reproducējama vide. Strādā visur vienādi.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <p class="slide-text" style="color:#7f8c8d; margin-top:1.5rem;">
    Push kodu &rarr; Railway uzbūvē &rarr; Cloudflare nodrošina SSL &rarr; gatavs.
    Divas minūtes.
    </p>
    """, unsafe_allow_html=True)
