import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("PyRevit", "Python Revit vidē — bez Visual Studio")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <p class="slide-text">
        <strong>PyRevit</strong> ir bezmaksas Revit add-in, kas ļauj rakstīt
        automatizācijas skriptus Python valodā. Nav nepieciešams Visual Studio,
        nav nepieciešams C#.
        </p>

        <p class="slide-text">
        Piemēri, ko var automatizēt:
        </p>

        <ul class="slide-text">
            <li>Elementu datu eksports uz Excel</li>
            <li>Parametru masu atjaunināšana</li>
            <li>Šķērsgriezumu batch maiņa</li>
            <li>Stiegrojuma marķēšana</li>
        </ul>

        <p class="slide-text">
        Ikdienā nenormāli daudz laika aizņem BIM parametru kārtošana, palīgelementu
        modelēšana, marķēšana — bet maz laika paliek būtiskajam. Šeit apskatītie
        aprēķinu piemēri to tieši nerisina, bet līdzīgi var automatizēt arī šādus
        uzdevumus. PyRevit ir viens no vienkāršāk realizējamiem variantiem.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.code("""
# PyRevit — eksportē siju datus
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
    ).AsDouble() * 304.8  # feet > mm

    print(f"{mark}: {length:.0f} mm")
        """, language="python")

        st.markdown('<p style="color:#7f8c8d; font-size:0.9rem;">docs.pyrevitlabs.io</p>', unsafe_allow_html=True)
