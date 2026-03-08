import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Resursi", "Kur iesākt un ko klausīties")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <p class="slide-text"><strong>Flocode Podcast</strong></p>
        <p class="slide-text">
        James O'Reilly vada podkāstu par Python inženierijā.
        Sarunas ar cilvēkiem, kas veido šīs bibliotēkas un rīkus.
        </p>

        <p class="slide-text">Ieteicamās epizodes:</p>
        <ul class="slide-text">
            <li>Morten Engen — <em>structuralcodes</em> bibliotēka</li>
            <li>Craig Brinck — <em>PyNite</em> FEM</li>
            <li>Connor Ferster — automatizācija</li>
        </ul>

        <p style="color:#7f8c8d;">flocode.substack.com</p>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <p class="slide-text"><strong>Mācību resursi</strong></p>

        | Resurss | Kas tas ir |
        |---------|------------|
        | StructuralPython | Kursi inženieriem |
        | EngineeringSkills | Pamācības ar kodu |
        | civils.ai | Python sertifikācija |

        <p class="slide-text" style="margin-top:1rem;">
        <strong>Zinātniskā bāze:</strong><br>
        Gustafsson & McBain (2020) — <em>scikit-fem</em>, JOSS
        </p>
        """, unsafe_allow_html=True)
