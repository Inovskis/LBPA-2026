import streamlit as st
from components.navigation import slide_header
from components.media import show_image


def render():
    slide_header("Ikdienas realitāte", "Rīki, ar kuriem strādājam")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        <p class="slide-text">
        Lielākā daļa inženieru-konstruktoru ikdienā izmanto kombināciju no Excel,
        specializētas programmatūras un savstarpēji nesaistītiem rīkiem. Tas darbojas —
        un tam ir savi iemesli.
        </p>

        <p class="slide-text">
        Bet ir lietas, kas atkārtojas. Formulas, kuras kopējam no vienas darba
        lapas uz citu. Aprēķini, kurus pārbaudām manuāli. Rezultāti, kurus
        pārformatējam atskaitēm. Šīs rutīnas patērē laiku, ko varētu veltīt
        inženiertehniskajiem lēmumiem.
        </p>

        <p class="slide-text">
        Jautājums nav par to, vai esošie rīki ir slikti. Tie nav.
        Jautājums ir — <strong>vai mēs varam atbrīvot laiku būtiskajam?</strong>
        </p>

        <p class="slide-text">
        Ir ļoti daudz Latvijas inženieru, kas ir ieguldījuši milzīgu darbu Excel darba lapu
        izstrādē — un protams tās automātiski nav jāmet ārā. Es šādus Excel failus sākotnēji
        izmantoju kā datu avotus un validācijas rīkus jaunu Python aprēķinu moduļu izstrādei.
        Jebkurā gadījumā sākotnējā periodā jebkuram aprēķinam ir lietderīgi veidot spoguli
        ar kādu citu metodi.
        </p>

        <p class="slide-text" style="color:#7f8c8d;">
        Ja to resursu, kas gadu gaitā ieguldīts dažādu Excel darba lapu izstrādē,
        konvertētu un ieguldītu aprēķinu izstrādē ar aktuālajām tehniskajām iespējām —
        mums varētu būt pilns spektrs ar dažādiem rīkiem un datiem, ar citu ražīgumu
        pret cilvēkstundu.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        show_image("btf_screenshot.jpg", caption="Tipisks aprēķinu rīks")
