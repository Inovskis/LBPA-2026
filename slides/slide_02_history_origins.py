import streamlit as st
from components.navigation import slide_header
from components.media import show_image


def render():
    slide_header("Sākums", "No matemātiskā neirona līdz pirmajam strupceļam")

    tab1, tab2, tab3, tab4 = st.tabs(["1943", "1958", "1969", "Neironu tīkls"])

    with tab1:
        col_img, col_txt = st.columns([1, 1.5])
        with col_img:
            show_image("mcculloch_pitts.png", caption="Warren McCulloch un Walter Pitts")
        with col_txt:
            st.markdown("""
            <div style="padding:0.5rem 0;">
                <div style="font-size:1.8rem; font-weight:700; color:#00BCD4;">1943</div>
                <div style="font-size:1.3rem; font-weight:600; color:#2c3e50; margin:0.5rem 0;">
                    Pirmais matemātiskais neirona modelis</div>
                <div style="font-size:1.05rem; color:#5d6d7e; line-height:1.7;">
                    McCulloch (neirofiziologs) un Pitts (matemātiķis) publicē darbu
                    "A Logical Calculus of Ideas Immanent in Nervous Activity" —
                    vienkārša funkcija ar ieejas signāliem un sliekšņa vērtību.
                    <br><br>
                    Nevis smadzenes, bet loģikas vārti. Ideja par mākslīgo neironu
                    ir vecāka nekā datori paši.
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        col_img, col_txt = st.columns([1.5, 1])
        with col_img:
            show_image("rosenblatt.jpg", caption="Frank Rosenblatt pie Mark I Perceptron mašīnas")
        with col_txt:
            st.markdown("""
            <div style="padding:0.5rem 0;">
                <div style="font-size:1.8rem; font-weight:700; color:#00BCD4;">1958</div>
                <div style="font-size:1.3rem; font-weight:600; color:#2c3e50; margin:0.5rem 0;">
                    Perceptrons — mašīna mācās</div>
                <div style="font-size:1.05rem; color:#5d6d7e; line-height:1.7;">
                    Frank Rosenblatt izveido pirmo mācīšanās algoritmu.
                    Mark I Perceptron — mašīna, kas pati maina savus svarus,
                    lai atpazītu vienkāršus attēlus.
                    <br><br>
                    Tolaik šķita — vēl desmit gadi un mēs atrisināsim intelektu.
                    New York Times rakstīja par "mašīnu, kas domā".
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        col_img, col_mid, col_right = st.columns([1, 1, 1])
        with col_img:
            show_image("minsky_papert.jpg", caption="Marvin Minsky un Seymour Papert")
        with col_mid:
            show_image("perceptron_xor.png", caption="Perceptrons can't do XOR")
        with col_right:
            show_image("ai_winter.png", caption="AI Winter 1969–1990")

        st.markdown("""
        <div style="background:#fdf2f2; border-left:4px solid #c0392b; border-radius:4px;
                    padding:1rem 1.5rem; margin-top:0.8rem;">
            <div style="font-size:1.3rem; font-weight:700; color:#c0392b; margin-bottom:0.3rem;">
                1969 — Strupceļš</div>
            <div style="font-size:1.05rem; color:#5d6d7e; line-height:1.7;">
                Minsky un Papert publicē grāmatu "Perceptrons", kurā matemātiski pierāda:
                viens neironu slānis nevar atrisināt pat vienkāršu XOR problēmu.
                Finansējums apstājas, interese apsīkst. Sākas gandrīz 15 gadu klusuma periods —
                idejas bija pareizas, bet aparatūra nebija gatava.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        col_img, col_txt = st.columns([1, 1.5])
        with col_img:
            show_image("neural_network.png", caption="Daudzslāņu neironu tīkls: Input → Hidden → Output")
        with col_txt:
            st.markdown("""
            <div style="padding:0.5rem 0;">
                <div style="font-size:1.3rem; font-weight:600; color:#2c3e50; margin-bottom:0.5rem;">
                    No viena slāņa līdz dziļajiem tīkliem</div>
                <div style="font-size:1.05rem; color:#5d6d7e; line-height:1.7;">
                    Minsky un Papert bija pareizi par vienu slāni — bet ne par vairākiem.
                    Kad 1986. gadā Hinton pierādīja, ka backpropagation strādā caur daudziem
                    slāņiem, neironu tīkli atdzima.
                    <br><br>
                    Šī diagramma parāda to, ko Rosenblatt nevarēja uzbūvēt 1958. gadā —
                    slēpto slāni (Hidden), kas ļauj tīklam mācīties sarežģītas sakarības.
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#fff8e1; border-left:4px solid #f9a825; border-radius:4px;
                        padding:0.8rem 1.2rem; margin-top:1rem;">
                <strong>Mācība:</strong> AI vēsturē cikli atkārtojās — lielas cerības, vilšanās,
                klusums, tad atkal jauns vilnis. Katru reizi iemesls bija viens:
                idejas apsteidza sava laika aparatūru.
            </div>
            """, unsafe_allow_html=True)
