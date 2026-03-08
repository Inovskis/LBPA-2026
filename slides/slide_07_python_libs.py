import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Bibliotēkas", "Tas, ko citi jau ir izdarījuši")

    st.markdown("""
    <p class="slide-text">
    Viena no Python lielākajām priekšrocībām — specializētas open-source bibliotēkas,
    ko uztur inženieri un zinātnieki visā pasaulē.
    </p>
    """, unsafe_allow_html=True)

    libs = [
        ("structuralcodes", "Eirokodeksu formulas, validētas un testētas",
         "from structuralcodes.codes.ec2_2004 import v_rdc_punching\nresult = v_rdc_punching(d_eff=200, f_ck=30, rho_l=0.015, gamma_c=1.5)"),
        ("concreteproperties", "Dzelzsbetona šķērsgriezumu analīze",
         "from concreteproperties.material import Concrete, SteelBar\ndiagram = analysis.moment_interaction_diagram()"),
        ("sectionproperties", "Ģeometriskās īpašības jebkuram šķērsgriezumam",
         "section = Section(geometry)\nsection.calculate_geometric_properties()"),
        ("scikit-fem + gmsh", "FEM režģu ģenerēšana un risinātājs",
         "mesh = MeshTri.load('model.msh')\nK = stiffness.assemble(basis)\nu = solve(K, f)"),
        ("PyNite", "3D rāmju un čaulu analīze",
         "model = FEModel3D()\nmodel.add_node('N1', 0, 0, 0)\nmodel.analyze()"),
    ]

    for name, desc, code in libs:
        with st.expander(f"**{name}** — {desc}"):
            st.code(code, language="python")

    st.markdown("""
    <p class="slide-text" style="color:#7f8c8d; margin-top:1rem;">
    Visas ir bezmaksas. Visas ir atvērtā pirmkoda. Formulas var pārbaudīt.
    </p>
    """, unsafe_allow_html=True)
