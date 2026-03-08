import streamlit as st

from components.styling import apply_theme
from components.navigation import init_navigation, render_navigation, inject_keyboard_nav
from slides import get_slide

st.set_page_config(
    page_title="AI un Python Būvkonstrukciju Projektēšanā",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_theme()
init_navigation()

# Presenter notes in sidebar
PRESENTER_NOTES = {
    1: "Sveicināt auditoriju. Iepazīstināt ar tēmu.",
    2: "Uzsvērt: tas nav nākotne — tas ir TAGAD.",
    3: "Pajautāt: cik lietojat Excel aprēķiniem?",
    4: "Parādīt design.kforma.lv pārlūkā.",
    5: "Demonstrēt 2-3 moduļus live vai video.",
    6: "Koda piemērs — uzsvērt lasāmību.",
    7: "Ātri pārskaitīt, neiedziļinoties katrā.",
    8: "Parādīt Claude Code termināli ja iespējams.",
    9: "Konkrēti skaitļi — 30 min vs 6h.",
    10: "SVARĪGI: AI nav burvju nūjiņa, jāverificē!",
    11: "Aizraujoša tēma — pieminēt ka tas ir legāls.",
    12: "Parādīt Railway dashboard ja ir laiks.",
    13: "Ātri pārskaitīt, GPAI piemērs live.",
    14: "Ja auditorijā ir Revit lietotāji — uzsvērt.",
    15: "Ieteikt Flocode kā pirmo resursu.",
    16: "Aicinājums — Latvija nedrīkst atpalikt.",
    17: "Paldies! QR kods uz ekrāna.",
}

with st.sidebar:
    st.markdown("### Prezentētāja Piezīmes")
    slide = st.session_state.current_slide
    st.info(PRESENTER_NOTES.get(slide, ""))
    st.markdown("---")
    st.markdown(f"**Laiks:** ~{slide * 1.5:.0f} / 25 min")

# Render the current slide
slide_render = get_slide(st.session_state.current_slide)
slide_render()

# Render bottom navigation + keyboard support
render_navigation()
inject_keyboard_nav()
