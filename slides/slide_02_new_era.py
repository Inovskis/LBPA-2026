import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Jaunā Ēra", "Indivīds var radīt to, kam agrāk vajadzēja veselu komandu")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="compare-old">
            <h3 style="color:#ef5350;">Agrāk</h3>
            <ul class="slide-text">
                <li>Lielas programmētāju komandas</li>
                <li>Milzīgi budžeti</li>
                <li>Gadi izstrādē</li>
                <li>Dārgas licences</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="compare-new">
            <h3 style="color:#66bb6a;">Tagad</h3>
            <ul class="slide-text">
                <li>Viens inženieris + AI</li>
                <li>Bezmaksas rīki</li>
                <li>Nedēļas, ne gadi</li>
                <li>Open-source bibliotēkas</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="accent-box" style="text-align:center; margin-top:2rem;">
        <p style="font-size:1.4rem; margin:0;">
            <strong>design.kforma.lv</strong> — 31 modulis, ~148,000 koda rindas<br>
            Izstrādāts viena inženiera spēkiem ar AI palīdzību
        </p>
    </div>
    """, unsafe_allow_html=True)
