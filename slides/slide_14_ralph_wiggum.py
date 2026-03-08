import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Ralph Wiggum metode",
                 "Kad AI strādā naktī, kamēr tu guli")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        <p class="slide-text">
        2025. gadā izstrādātājs Geoffrey Huntley publicēja 5 rindu Bash skriptu,
        kas automātiski baro AI ar tā paša ģenerētā koda kļūdām — atkal un atkal,
        līdz programma sāk darboties.
        </p>
        """, unsafe_allow_html=True)

        st.code("""
while true; do
    claude --prompt "Build program X" \\
           --context "$(cat output.log)" \\
           | tee output.log
done
        """, language="bash")

        st.markdown("""
        <p class="slide-text">
        Ar šo pieeju cilvēkiem ir izdevies rekonstruēt komerciālas programmatūras
        funkcionalitāti. Metode ir nosaukta Ralph Wiggum vārdā —
        naivais puisītis, kurš vienkārši mēģina un mēģina.
        </p>

        <p class="slide-text" style="color:#7f8c8d;">
        Tas, protams, rada jautājumus par intelektuālo īpašumu un ētiku.
        Bet tehniski — tas strādā. Un tas maina priekšstatu par to,
        kas ir iespējams.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background:#f5f7fa; border:1px solid #e0e6ed; border-radius:8px;
                    padding:1.5rem; text-align:center;">
            <p style="font-size:1rem; color:#00838F; margin-bottom:1rem;">Iteratīvā cilpa</p>
            <div style="background:#fff; padding:0.7rem; border-radius:6px; margin:0.4rem 0; border:1px solid #e0e6ed;">
                <p style="color:#2c3e50; margin:0; font-size:0.9rem;">AI ģenerē kodu</p>
            </div>
            <p style="color:#95a5a6; margin:0.2rem 0;">&darr;</p>
            <div style="background:#fff; padding:0.7rem; border-radius:6px; margin:0.4rem 0; border:1px solid #e0e6ed;">
                <p style="color:#2c3e50; margin:0; font-size:0.9rem;">Izpilda, kļūdas</p>
            </div>
            <p style="color:#95a5a6; margin:0.2rem 0;">&darr;</p>
            <div style="background:#fff; padding:0.7rem; border-radius:6px; margin:0.4rem 0; border:1px solid #e0e6ed;">
                <p style="color:#2c3e50; margin:0; font-size:0.9rem;">Kļūdas atpakaļ AI</p>
            </div>
            <p style="color:#95a5a6; margin:0.2rem 0;">&darr;</p>
            <div style="background:#f0fafa; padding:0.7rem; border-radius:6px; margin:0.4rem 0; border:1px solid #00BCD4;">
                <p style="color:#00838F; margin:0; font-size:0.9rem;">Atkārto līdz darbojas</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
