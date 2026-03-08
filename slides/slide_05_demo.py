import streamlit as st
from components.navigation import slide_header
from components.media import show_image, show_video


def render():
    slide_header("Demo", "Platformas labākie moduļi")

    tab1, tab2, tab3, tab4 = st.tabs([
        "KF3D FEM",
        "Pāļi (CPT)",
        "Liece",
        "Caurspiešana"
    ])

    with tab1:
        st.markdown("""
        <div class="stat-card">
            <h4>KF3D — 3D Strukturālā Analīze</h4>
            <p class="slide-text">
            11,000+ koda rindas &bull; Three.js 3D vizualizācija &bull; PyNite FEM backend<br>
            Mezgli, stieņi, čaulas, balsti, slodzes — pilna 3D analīze pārlūkā
            </p>
        </div>
        """, unsafe_allow_html=True)
        show_video("demo_kf3d.mp4")
        show_image("demo_kf3d.png", caption="KF3D FEM modulis")

    with tab2:
        st.markdown("""
        <div class="stat-card">
            <h4>Pāļu Projektēšana (CPT)</h4>
            <p class="slide-text">
            2,789 koda rindas &bull; CPT datu analīze &bull; Vairāku profilu salīdzinājums<br>
            Aksiālā nestspēja no CPT datiem ar detalizētu vizualizāciju
            </p>
        </div>
        """, unsafe_allow_html=True)
        show_video("demo_pile.mp4")
        show_image("demo_pile.png", caption="Pāļu CPT modulis")

    with tab3:
        st.markdown("""
        <div class="stat-card">
            <h4>Lieces Aprēķins</h4>
            <p class="slide-text">
            1,953 koda rindas &bull; EC2 / GEM / Mander betona modeļi<br>
            M-N diagrammas, plaisu kontrole, deformācijas
            </p>
        </div>
        """, unsafe_allow_html=True)
        show_video("demo_bending.mp4")
        show_image("demo_bending.png", caption="Lieces modulis")

    with tab4:
        st.markdown("""
        <div class="stat-card">
            <h4>Caurspiešanas Aprēķins</h4>
            <p class="slide-text">
            Interaktīvs SVG plānskats &bull; EC2 un MC2010 salīdzinājums<br>
            Automātiska kritiskā perimetra vizualizācija
            </p>
        </div>
        """, unsafe_allow_html=True)
        show_video("demo_punching.mp4")
        show_image("demo_punching.png", caption="Caurspiešanas modulis")

    st.info("Video ieraksti — ja nav pievienoti, sagatavot ekrāna ierakstus no design.kforma.lv")
