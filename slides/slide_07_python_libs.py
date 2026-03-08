import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Python Bibliotēkas", "Specializēti rīki konstrukcijām")

    libs = [
        ("structuralcodes", "Validētas Eirokodeksu formulas",
         "from structuralcodes.codes.ec2_2004 import v_rdc_punching\nresult = v_rdc_punching(d_eff=200, f_ck=30, rho_l=0.015, gamma_c=1.5)"),
        ("concreteproperties", "Dzelzsbetona šķērsgriezumu analīze, M-N diagrammas",
         "from concreteproperties.material import Concrete, SteelBar\nanalysis = ConcreteAnalysis(section)\ndiagram = analysis.moment_interaction_diagram()"),
        ("sectionproperties", "Ģeometriskās īpašības jebkuram šķērsgriezumam",
         "from sectionproperties.pre.geometry import Geometry\nsection = Section(geometry)\nsection.calculate_geometric_properties()"),
        ("scikit-fem + gmsh", "FEM analīze — režģi un risinātājs",
         "import gmsh\nfrom skfem import *\nmesh = MeshTri.load('model.msh')\nK = stiffness.assemble(basis)\nu = solve(K, f)"),
        ("PyNite", "3D frame/shell analīze",
         "from PyNite import FEModel3D\nmodel = FEModel3D()\nmodel.add_node('N1', 0, 0, 0)\nmodel.analyze()"),
    ]

    for name, desc, code in libs:
        with st.expander(f"**{name}** — {desc}", expanded=False):
            st.code(code, language="python")

    st.markdown("""
    <div class="accent-box" style="text-align:center;">
        Visas bibliotēkas ir <strong>bezmaksas</strong> un <strong>open-source</strong>!
    </div>
    """, unsafe_allow_html=True)
