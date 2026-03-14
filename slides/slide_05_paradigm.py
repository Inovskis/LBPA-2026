import streamlit as st
from components.navigation import slide_header
from components.media import show_image


def render():
    slide_header("Paradigmas maiņa", "Nevis revolūcija — vienkārši citas iespējas")

    col_img, col_txt = st.columns([1.3, 1])

    with col_img:
        show_image("paradigm_shift.png",
                   caption="Komanda ar rasējamiem galdiem → viens inženieris ar datoru", width=550)

    with col_txt:
        st.markdown("""
        <div style="padding:0.5rem 0;">
            <p class="slide-text">
            Pirms dažiem gadiem, lai izveidotu specializētu aprēķinu platformu, bija nepieciešama
            programmētāju komanda, budžets un laiks.
            </p>
            <p class="slide-text">
            Šodien tehnoloģiskā ainava ir mainījusies —
            rīki, bibliotēkas un AI asistenti ļauj vienam inženierim paveikt to,
            kas agrāk prasīja komandu.
            </p>
            <p class="slide-text">
            Tas nenozīmē, ka viss kļūst vienkāršāk vai labāk. Tas nozīmē, ka <strong>iespējas
            ir mainījušās</strong> — un katram ir jāizlemj, ko ar tām darīt.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="accent-box">
        Es uzbūvēju aprēķinu rīku kopu — 31 modulis, ~148,000 koda rindas.
        Nav komanda, nav budžets. Es neesmu nekāds guru — un tieši tāpēc šis piemērs
        ir zīmīgs. Tā ir AI revolūcija komplektā ar servisu attīstību — lietas,
        kas kopā maina to, ko viens cilvēks spēj paveikt.
    </div>
    """, unsafe_allow_html=True)
