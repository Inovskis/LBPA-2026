import streamlit as st
from components.navigation import slide_header
from components.media import show_image


def render():
    slide_header("Ikdienas realitāte", "Rīki, ar kuriem strādājam")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        <p class="slide-text">
        Ikdienā — Excel, specializēta programmatūra, nesaistīti rīki. Tas darbojas.
        Bet formulas kopējam, aprēķinus pārbaudām manuāli, rezultātus pārformatējam.
        Jautājums ir — <strong>vai varam atbrīvot laiku būtiskajam?</strong>
        </p>

        <p class="slide-text">
        Daudzi inženieri ir ieguldījuši milzīgu darbu Excel darba lapās — un tās nav
        jāmet ārā. Labs piemērs: HCS plātņu aprēķinu salīdzinājums, kur dažādi biroji
        no vienādiem izejas datiem ieguva atšķirīgus rezultātus. Mēģinot saprast
        atšķirības, nonācu pie specializētām bibliotēkām niansētākai šķērsgriezuma
        analīzei. Jebkuram aprēķinam ir lietderīgi veidot spoguli ar citu metodi.
        </p>

        <p class="slide-text" style="color:#7f8c8d;">
        Ja to resursu, kas ieguldīts Excel darba lapās, konvertētu ar aktuālajām
        iespējām — mums varētu būt pilns rīku spektrs un cits ražīgums pret cilvēkstundu.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        show_image("btf_screenshot.jpg", caption="Tipisks aprēķinu rīks")
