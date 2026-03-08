import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Piemērs: ko var uzbūvēt viens cilvēks", "Nav par platformu — par iespēju")

    st.markdown("""
    <p class="slide-text">
    Lai ilustrētu šo paradigmas maiņu — es vairāku gadu garumā izveidoju web bāzētu
    aprēķinu rīku kopu būvkonstrukcijām. Tas nav komercprodukts un nav paredzēts
    tirgum — tas ir eksperiments, kas parāda, ko šodien var izdarīt viens inženieris.
    </p>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="stat-card"><p class="stat-number">31</p><p class="stat-label">aprēķinu modulis</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><p class="stat-number">148K</p><p class="stat-label">koda rindas</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><p class="stat-number">5</p><p class="stat-label">Eirokodeksi</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="stat-card"><p class="stat-number">1</p><p class="stat-label">izstrādātājs</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <p class="slide-text">
    Tajā ir Eirokodeksu aprēķini ar Latvijas nacionālajiem pielikumiem —
    EN 1992, EN 1993, EN 1995, EN 1997, EN 1991. Katra formula ir izsekojama.
    </p>

    <p class="slide-text" style="color:#7f8c8d;">
    Šis ir nepilnīgs, nepārtraukti mainīgs eksperiments — nevis gatavs produkts.
    Būtiskais nav pati platforma, bet gan tas, ka šāda apjoma lieta
    vispār ir iespējama bez komandas un budžeta. Tas ir laikmeta raksturojums.
    </p>
    """, unsafe_allow_html=True)
