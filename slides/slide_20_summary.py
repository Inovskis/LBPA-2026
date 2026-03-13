import streamlit as st
from components.navigation import slide_header
from components.media import show_image

try:
    import qrcode
    from io import BytesIO
    HAS_QRCODE = True
except ImportError:
    HAS_QRCODE = False


def render():
    slide_header("Noslēgums")

    st.markdown("""
    <p class="slide-text">
    Šī nav prezentācija par to, ka AI atrisinās visas problēmas.
    Tā ir par to, ka rīki ir mainījušies — un mēs varam izvēlēties,
    kā tos lietot.
    </p>

    <p class="slide-text">
    Skepse ir veselīga. Inženierija ir konservatīva disciplīna, un tam ir iemesls —
    mēs projektējam lietas, uz kurām stāv cilvēki. Bet konservatīvisms nenozīmē
    stagnāciju. Tas nozīmē — eksperimentēt apdomīgi.
    </p>

    <p class="slide-text">
    Inženieru vidē nereti ierasts klusēt un visu pieturēt pie sevis, uztverot citus
    par konkurentiem. Bet globālā mērogā mēs esam mazi un visi vienā laivā.
    Augt varam tikai kopā. Zināšanas ir lieta, ar kurām daloties tam, kas to dara,
    mazāk nepaliek.
    </p>

    <p class="slide-text">
    Ja kaut kas no šodienas stāstītā licis aizdomāties — tas ir pietiekami.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown("""
        <div class="accent-box">
            Ja interesē apskatīt piemēru, par kuru runāju —
            <strong>design.kforma.lv</strong><br>
            <span style="color:#7f8c8d;">Nav komercprodukts. Vienkārši eksperiments, ko var apskatīt.</span><br>
            <span style="color:#7f8c8d;">nauris@kforma.lv</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if HAS_QRCODE:
            qr = qrcode.make("https://design.kforma.lv")
            buf = BytesIO()
            qr.save(buf, format="PNG")
            st.image(buf.getvalue(), caption="piemērs: design.kforma.lv", width=160)

    show_image("kforma_logo.png", width=120)
