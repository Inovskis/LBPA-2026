import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Paradigmas maiņa", "Nevis revolūcija — vienkārši citas iespējas")

    st.markdown("""
    <p class="slide-text">
    Pirms dažiem gadiem, lai izveidotu specializētu aprēķinu platformu, bija nepieciešama
    programmētāju komanda, budžets un laiks. Šodien tehnoloģiskā ainava ir mainījusies —
    rīki, bibliotēkas un AI asistenti ļauj vienam inženierim paveikt to,
    kas agrāk prasīja komandu.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="slide-text">
    Tas nenozīmē, ka viss kļūst vienkāršāk vai labāk. Tas nozīmē, ka <strong>iespējas
    ir mainījušās</strong> — un katram ir jāizlemj, ko ar tām darīt.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="accent-box">
        <strong>design.kforma.lv</strong> — 31 aprēķinu modulis, ~148,000 koda rindas.
        Nav komanda. Nav budžets. Vienkārši inženieris, kurš mēģina lietas darīt citādi.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="slide-text" style="color:#7f8c8d; margin-top:2rem;">
    Šī nav panaceja un nav komercprodukts. Tas ir eksperiments — kas notiek,
    ja inženieris izmanto šodienas rīkus pilnā apjomā.
    </p>
    """, unsafe_allow_html=True)
