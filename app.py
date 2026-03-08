import streamlit as st

from components.styling import apply_theme
from components.navigation import init_navigation, render_navigation, inject_keyboard_nav
from slides import get_slide

st.set_page_config(
    page_title="Mākslīgo neironu tīklu lietošana būvkonstrukciju projektēšanā",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_theme()
init_navigation()

# Presenter notes in sidebar
PRESENTER_NOTES = {
    1: "Sveicināt auditoriju. Iepazīstināt ar tēmu.",
    2: "Vēsturiskais konteksts. 80+ gadi kopš pirmā neirona modeļa.",
    3: "Katrs solis bija atkarīgs no skaitļošanas jaudas pieauguma.",
    4: "ChatGPT bija lēciens. 100M lietotāju 2 mēnešos.",
    5: "Uzsvērt: tas nav nākotne — tas ir TAGAD.",
    6: "Pajautāt: cik lietojat Excel aprēķiniem?",
    7: "Parādīt piemēru pārlūkā — nav produkts, ir eksperiments.",
    8: "Demonstrēt 2-3 moduļus live vai video.",
    9: "Koda piemērs — uzsvērt lasāmību.",
    10: "Ātri pārskaitīt, neiedziļinoties katrā.",
    11: "Parādīt Claude Code termināli ja iespējams.",
    12: "Konkrēti skaitļi — 30 min vs 6h.",
    13: "SVARĪGI: AI nav burvju nūjiņa, jāverificē!",
    14: "Aizraujoša tēma — pieminēt ka tas ir legāls.",
    15: "Parādīt Railway dashboard ja ir laiks.",
    16: "Ātri pārskaitīt, GPAI piemērs live.",
    17: "Ja auditorijā ir Revit lietotāji — uzsvērt.",
    18: "Ieteikt Flocode kā pirmo resursu.",
    19: "Aicinājums — Latvija nedrīkst atpalikt.",
    20: "Paldies! QR kods uz ekrāna.",
}

with st.sidebar:
    st.markdown("### Prezentētāja Piezīmes")
    slide = st.session_state.current_slide
    st.info(PRESENTER_NOTES.get(slide, ""))
    st.markdown("---")
    st.markdown(f"**Laiks:** ~{slide * 1.25:.0f} / 25 min")

# Render the current slide
slide_render = get_slide(st.session_state.current_slide)
slide_render()

# Render bottom navigation + keyboard support
render_navigation()
inject_keyboard_nav()
