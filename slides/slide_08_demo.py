import streamlit as st
from components.navigation import slide_header
from components.media import show_image, show_video


def render():
    slide_header("Daži piemēri", "Ko Python ļauj izveidot inženierim")

    tab1, tab2, tab3, tab4 = st.tabs([
        "3D FEM",
        "Pāļi (CPT)",
        "Liece",
        "Caurspiešana"
    ])

    with tab1:
        st.markdown("""
        <p class="slide-text">
        <strong>3D rāmja un čaulu analīze</strong> tieši pārlūkā —
        Three.js vizualizācija, PyNite risinātājs. Nekas nav jāinstalē.
        ~11,000 koda rindas — piemērs tam, cik sarežģītus rīkus var izveidot ar Python un atvērtā koda bibliotēkām.
        </p>
        """, unsafe_allow_html=True)
        show_video("demo_kf3d.mp4")
        show_image("demo_kf3d.png")

    with tab2:
        st.markdown("""
        <p class="slide-text">
        <strong>Pāļu projektēšana no CPT datiem</strong> — aksiālās nestspējas
        aprēķins ar detalizētu profilu vizualizāciju. Piemērs ģeotehniskā moduļa
        iespējām, ko nodrošina NumPy un Matplotlib.
        </p>
        """, unsafe_allow_html=True)
        show_video("demo_pile.mp4")
        show_image("demo_pile.png")

    with tab3:
        st.markdown("""
        <p class="slide-text">
        <strong>Lieces aprēķins</strong> — EC2 ar vairākiem betona modeļiem
        (Eirokodekss, GEM, Mander). M-N diagrammas, plaisu kontrole.
        Bibliotēkas concreteproperties un structuralcodes darbībā.
        </p>
        """, unsafe_allow_html=True)
        show_video("demo_bending.mp4")
        show_image("demo_bending.png")

    with tab4:
        st.markdown("""
        <p class="slide-text">
        <strong>Caurspiešana</strong> — interaktīvs SVG plānskats, EC2 un MC2010
        salīdzinājums. Vizualizācija, ko AI palīdzēja izveidot 30 minūtēs —
        piemērs tam, kā AI paātrina izstrādi.
        </p>
        """, unsafe_allow_html=True)
        show_video("demo_punching.mp4")
        show_image("demo_punching.png")
