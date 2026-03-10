import streamlit as st
from components.navigation import slide_header
from components.media import show_image


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

    # ── FIN plate example — analytical vs FEM ──────────────────────
    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        show_image("kforma_fin_analytical.png",
                   caption="EN 1993 — analītiskais aprēķins (pretestības pārbaudes)", width=450)
    with col2:
        show_image("kforma_fin_fem.png",
                   caption="FEM — Von Mises spriegumu sadalījums", width=450)

    st.markdown("""
    <p class="slide-text" style="color:#7f8c8d;">
    Šis ir nepilnīgs, nepārtraukti mainīgs eksperiments — nevis gatavs produkts.
    Ja kāds bez padziļinātām programmēšanas un matemātikas zināšanām
    var nonākt līdz šādam rezultātam — iedomājieties, ko var paveikt
    cilvēks ar šīm zināšanām. Iespējams, kāds no klātesošajiem
    ar šādām lietām jau nodarbojas daudz nopietnākā līmenī.
    </p>
    """, unsafe_allow_html=True)
