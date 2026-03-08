import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("AI izstrādē", "Kā es to lietoju ikdienā")

    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown("""
        <p class="slide-text">
        Man ir atsevišķa Linux mašīna, uz kuras darbojas
        <strong>Claude Code</strong> — AI asistents terminālī.
        Tas lasa projekta failus, raksta kodu, izpilda komandas.
        </p>

        <p class="slide-text">
        Tas nav burvju nūjiņa. Bieži rezultāts ir nepareizs
        un jālabo. Bet iteratīvā pieeja — pajautāt, pārbaudīt,
        koriģēt — ietaupa laiku uzdevumos, kas citādi prasītu
        stundas manuāla darba.
        </p>

        <p class="slide-text" style="color:#7f8c8d;">
        Svarīgi: AI neizprot inženierijas būtību.
        Tas ģenerē kodu. Verifikācija ir inženiera atbildība.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.code("""
$ claude

> Pievieno SVG vizualizāciju caurspiešanas modulim

Claude: Izveidošu trīs komponentus...
        [Raksta ~400 rindas JavaScript]
        [Testē, atrod kļūdu, labo]

# Rezultāts: 30 minūtes.
# Manuāli tas pats: 4-6 stundas.
# Bet — manuāli es zinātu katru rindu.
# Ar AI man tā ir jāpārbauda.
        """, language="text")
