import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Ralph Wiggum Metode",
                 "Iteratīvā AI cilpa — reverse engineering")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        ### Kā tas darbojas?

        **Geoffrey Huntley** (2025) izveidoja 5 rindu Bash skriptu:
        """)

        st.code("""
while true; do
    claude --prompt "Build program X" \\
           --context "$(cat output.log)" \\
           | tee output.log
done
        """, language="bash")

        st.markdown("""
        ### Princips
        1. AI ģenerē kodu
        2. Kods tiek izpildīts
        3. Kļūdas un rezultāti atgriežas AI
        4. AI labo un uzlabo
        5. **Atkārto līdz darbojas!**

        ### Rezultāts
        - Komerciālas programmatūras klonēšana
        - Piemērs: grāmatvedības programma rekonstruēta pilnībā
        - Claude Code plugin pieejams oficiāli
        """)

    with col2:
        st.markdown("""
        <div style="background:#1a1f2e; border:2px solid #00BCD4; border-radius:12px;
                    padding:2rem; text-align:center;">
            <p style="font-size:1.2rem; color:#00BCD4; margin-bottom:1rem;">CILPA</p>
            <div style="background:#32373c; padding:0.8rem; border-radius:8px; margin:0.5rem 0;">
                <p style="color:#66bb6a; margin:0;">AI ģenerē kodu</p>
            </div>
            <p style="color:#fff; margin:0.3rem 0;">&#8595;</p>
            <div style="background:#32373c; padding:0.8rem; border-radius:8px; margin:0.5rem 0;">
                <p style="color:#ef5350; margin:0;">Kļūdas / rezultāti</p>
            </div>
            <p style="color:#fff; margin:0.3rem 0;">&#8595;</p>
            <div style="background:#32373c; padding:0.8rem; border-radius:8px; margin:0.5rem 0;">
                <p style="color:#ffb74d; margin:0;">Atgriež AI kā kontekstu</p>
            </div>
            <p style="color:#fff; margin:0.3rem 0;">&#8595;</p>
            <div style="background:#32373c; padding:0.8rem; border-radius:8px; margin:0.5rem 0;">
                <p style="color:#00BCD4; margin:0;">Atkārto līdz &#10003;</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    > *"Kontekstuālais spiediena katls" — katrs cikls pievieno zināšanas
    > līdz AI saprot visu sistēmu.*
    """)
