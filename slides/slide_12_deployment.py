import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Deployment Resursi", "No koda līdz produkcijai")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="stat-card" style="text-align:center;">
            <p style="font-size:2rem;">&#128642;</p>
            <h4 style="color:#00BCD4;">Railway</h4>
            <p class="slide-text" style="font-size:0.9rem;">
            Cloud hosting<br>Auto-deploy no GitHub<br>PostgreSQL iekļauts<br>
            <strong>design.kforma.lv</strong> darbojas šeit
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stat-card" style="text-align:center;">
            <p style="font-size:2rem;">&#128025;</p>
            <h4 style="color:#00BCD4;">GitHub</h4>
            <p class="slide-text" style="font-size:0.9rem;">
            Versiju kontrole<br>Sadarbības platforma<br>CI/CD pipelines<br>
            Bezmaksas privātie repo
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="stat-card" style="text-align:center;">
            <p style="font-size:2rem;">&#127880;</p>
            <h4 style="color:#00BCD4;">Streamlit</h4>
            <p class="slide-text" style="font-size:0.9rem;">
            Python &rarr; Web app<br>Bezmaksas hosting<br>
            <strong>Šī prezentācija</strong><br>ir Streamlit app!
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="stat-card" style="text-align:center;">
            <p style="font-size:2rem;">&#128051;</p>
            <h4 style="color:#00BCD4;">Docker</h4>
            <p class="slide-text" style="font-size:0.9rem;">
            Reproducējama vide<br>Viena komanda deploy<br>Izolēta sistēma
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### design.kforma.lv deployment plūsma:")
    st.code("""
git push origin main          # 1. Push kodu
# Railway automātiski:
#   2. Build Docker image
#   3. Deploy jaunas versijas
#   4. Cloudflare nodrošina SSL
# Gatavs ~2 minūtēs!
    """, language="bash")
