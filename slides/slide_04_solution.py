import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Risinājums", "design.kforma.lv — atvērta web platforma")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="stat-card"><p class="stat-number">31</p><p class="stat-label">Aprēķinu moduļi</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><p class="stat-number">148K</p><p class="stat-label">Koda rindas</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><p class="stat-number">5</p><p class="stat-label">Eirokodeksi</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="stat-card"><p class="stat-number">0€</p><p class="stat-label">Cena lietotājam</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Atbalstītie standarti:**
        - EN 1992 (Dzelzbetona konstrukcijas) + LV NA
        - EN 1993 (Tērauda konstrukcijas)
        - EN 1995 (Koka konstrukcijas)
        - EN 1997 (Ģeotehnika)
        - EN 1991 (Slodzes) + LV NA
        """)
    with col2:
        st.markdown("""
        **Platformas priekšrocības:**
        - Web-bāzēta — pieejama jebkurā ierīcē
        - Atvērts kods — pārredzamas formulas
        - Validēta pret standartiem
        - Regulāri atjauninājumi
        """)
