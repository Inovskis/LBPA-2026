import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("PyRevit", "Revit Add-ins ar Python")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Kas ir PyRevit?
        - **Bezmaksas** open-source Revit add-in
        - Python skripti — **bez Visual Studio**
        - Automatizē atkārtojošos uzdevumus
        - Pilna Revit API pieejamība

        ### Piemēri
        - Batch šķērsgriezumu maiņa
        - Automātiska stiegrojuma marķēšana
        - Excel &rarr; Revit datu imports
        - Parametru masu atjaunināšana
        """)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="compare-old" style="padding:0.8rem;">
                <p style="margin:0;"><strong>C# Add-in:</strong><br>Visual Studio, .NET, kompilēšana</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="compare-new" style="padding:0.8rem;">
                <p style="margin:0;"><strong>PyRevit:</strong><br>Teksta redaktors + Python</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.code("""
# PyRevit skripts — eksportē elementu datus
from pyrevit import revit, DB

doc = revit.doc
collector = DB.FilteredElementCollector(doc)
beams = collector.OfCategory(
    DB.BuiltInCategory.OST_StructuralFraming
).WhereElementIsNotElementType()

for beam in beams:
    mark = beam.get_Parameter(
        DB.BuiltInParameter.ALL_MODEL_MARK
    ).AsString()
    length = beam.get_Parameter(
        DB.BuiltInParameter.INSTANCE_LENGTH
    ).AsDouble() * 304.8  # feet to mm

    print(f"{mark}: {length:.0f} mm")
        """, language="python")

        st.caption("docs.pyrevitlabs.io")
