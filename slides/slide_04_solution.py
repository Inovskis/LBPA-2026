import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("design.kforma.lv", "Kas tas ir un kas tas nav")

    st.markdown("""
    <p class="slide-text">
    Tā ir web platforma būvkonstrukciju aprēķiniem, kuru es izveidoju savām vajadzībām.
    Tā nav komerciāla programmatūra un nav domāta kā aizstājējs esošajiem rīkiem.
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
    Platformā ir Eirokodeksu aprēķini ar Latvijas nacionālajiem pielikumiem —
    EN 1992, EN 1993, EN 1995, EN 1997, EN 1991. Katra formula ir izsekojama.
    Nekas nav paslēpts.
    </p>

    <p class="slide-text" style="color:#7f8c8d;">
    Tas, ka viens cilvēks var izveidot šādu platformu, nav sasniegums —
    tas ir laikmeta raksturojums.
    </p>
    """, unsafe_allow_html=True)
