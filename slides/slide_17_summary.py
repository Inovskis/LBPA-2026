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
    slide_header("Kopsavilkums")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="stat-card" style="text-align:center; min-height:200px;">
            <p style="font-size:2.5rem;">&#128013;</p>
            <h4 style="color:#00BCD4;">Python</h4>
            <p class="slide-text">Spēcīgs bezmaksas rīks inženieriem ar validētām bibliotēkām</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stat-card" style="text-align:center; min-height:200px;">
            <p style="font-size:2.5rem;">&#129302;</p>
            <h4 style="color:#00BCD4;">AI</h4>
            <p class="slide-text">Paātrina izstrādi ~5x, bet vienmēr jāverificē rezultāts</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="stat-card" style="text-align:center; min-height:200px;">
            <p style="font-size:2.5rem;">&#128640;</p>
            <h4 style="color:#00BCD4;">Jaunā Ēra</h4>
            <p class="slide-text">Katrs indivīds var radīt profesionālus rīkus</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="accent-box">
            <h3 style="margin-top:0;">Izmēģini pats!</h3>
            <p style="font-size:1.4rem;">
                <strong>design.kforma.lv</strong><br>
                Bezmaksas reģistrācija &bull; 31 aprēķinu modulis
            </p>
            <p style="font-size:1rem; margin-bottom:0;">
                nauris@kforma.lv
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Jautājumi?")

    with col2:
        if HAS_QRCODE:
            qr = qrcode.make("https://design.kforma.lv")
            buf = BytesIO()
            qr.save(buf, format="PNG")
            st.image(buf.getvalue(), caption="design.kforma.lv", width=200)
        else:
            st.info("QR kods: design.kforma.lv")

    show_image("kforma_logo.png", width=150)
