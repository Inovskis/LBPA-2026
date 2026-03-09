import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Kā tas sākās", "No matemātiskā neirona līdz pirmajam strupceļam")

    # ── 4-column horizontal timeline ──────────────────────────────
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div style="background:#f0fafa; border-radius:8px; padding:1rem 1.2rem; height:100%;
                    border-top:4px solid #00BCD4;">
            <div style="font-size:1.6rem; font-weight:700; color:#00BCD4;">1943</div>
            <div style="font-size:1.05rem; font-weight:600; color:#2c3e50; margin:0.4rem 0 0.3rem;">
                McCulloch & Pitts</div>
            <div style="font-size:0.92rem; color:#5d6d7e; line-height:1.5;">
                Pirmais matemātiskais neirona modelis — vienkārša funkcija
                ar ieejas signāliem un sliekšņa vērtību.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div style="background:#f0fafa; border-radius:8px; padding:1rem 1.2rem; height:100%;
                    border-top:4px solid #00BCD4;">
            <div style="font-size:1.6rem; font-weight:700; color:#00BCD4;">1958</div>
            <div style="font-size:1.05rem; font-weight:600; color:#2c3e50; margin:0.4rem 0 0.3rem;">
                Rosenblatt — Perceptrons</div>
            <div style="font-size:0.92rem; color:#5d6d7e; line-height:1.5;">
                Pirmais mācīšanās algoritms. Mašīna, kas pati maina svarus,
                lai atpazītu vienkāršus attēlus. Tolaik šķita — vēl desmit
                gadi un mēs atrisināsim intelektu.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div style="background:#fdf2f2; border-radius:8px; padding:1rem 1.2rem; height:100%;
                    border-top:4px solid #c0392b;">
            <div style="font-size:1.6rem; font-weight:700; color:#c0392b;">1969</div>
            <div style="font-size:1.05rem; font-weight:600; color:#2c3e50; margin:0.4rem 0 0.3rem;">
                Minsky & Papert — strupceļš</div>
            <div style="font-size:0.92rem; color:#5d6d7e; line-height:1.5;">
                Grāmata pierāda: viens neironu slānis nevar atrisināt pat
                vienkāršu XOR problēmu. Finansējums apstājas, interese apsīkst.
                Sākas pirmais "aukstais periods" — gandrīz 15 gadu pauze.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div style="background:#f0fafa; border-radius:8px; padding:1rem 1.2rem; height:100%;
                    border-top:4px solid #00BCD4;">
            <div style="font-size:1.6rem; font-weight:700; color:#00BCD4;">1974</div>
            <div style="font-size:1.05rem; font-weight:600; color:#2c3e50; margin:0.4rem 0 0.3rem;">
                Werbos — Backpropagation</div>
            <div style="font-size:0.92rem; color:#5d6d7e; line-height:1.5;">
                Doktora darbā apraksta kļūdas atpakaļizplatīšanos caur slāņiem.
                Akadēmiskā pasaule to gandrīz neievēro — ideja guļ vēl 12 gadus.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Context box — explain the pattern ─────────────────────────
    st.markdown("""
    <div style="background:#fff8e1; border-left:4px solid #f9a825; border-radius:4px;
                padding:1rem 1.5rem; margin-top:1.5rem;">
        <div style="font-size:1rem; color:#2c3e50; line-height:1.7;">
            <strong>Mācība:</strong> AI vēsturē šādi cikli atkārtojās vairākkārt —
            lielas cerības, pēc tam vilšanās un klusuma periods, tad atkal jauns vilnis.
            Katru reizi iemesls bija viens: idejas apsteidza sava laika aparatūru.
            Koncepti bija pareizi — trūka datoru jaudas un datu apjoma, lai tos realizētu.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Perceptron diagram — HTML/CSS (no SVG — Streamlit Cloud strips it)
    st.markdown("""
    <div style="background:#f5f7fa; border-radius:8px; padding:1.2rem; margin-top:1rem;">
        <div style="font-size:0.8rem; font-weight:600; color:#7f8c8d; text-transform:uppercase;
                    letter-spacing:1px; margin-bottom:0.8rem; text-align:center;">
            Perceptrons — vienkāršākais neironu tīkla elements
        </div>
        <div style="display:flex; align-items:center; justify-content:center; gap:0.4rem; flex-wrap:wrap;">
            <div style="display:flex; flex-direction:column; gap:0.4rem; align-items:center;">
                <div style="width:44px; height:44px; border-radius:50%; background:#e0f7fa;
                            border:2px solid #00BCD4; display:flex; align-items:center; justify-content:center;
                            font-weight:600; font-size:0.9rem; color:#2c3e50;">x₁</div>
                <div style="width:44px; height:44px; border-radius:50%; background:#e0f7fa;
                            border:2px solid #00BCD4; display:flex; align-items:center; justify-content:center;
                            font-weight:600; font-size:0.9rem; color:#2c3e50;">x₂</div>
                <div style="width:44px; height:44px; border-radius:50%; background:#e0f7fa;
                            border:2px solid #00BCD4; display:flex; align-items:center; justify-content:center;
                            font-weight:600; font-size:0.9rem; color:#2c3e50;">x₃</div>
                <div style="font-size:0.75rem; color:#7f8c8d;">Ieejas</div>
            </div>
            <div style="display:flex; flex-direction:column; align-items:center; color:#00838F;
                        font-size:0.85rem; font-weight:600; gap:0.3rem; padding:0 0.3rem;">
                <span>w₁ →</span><span>w₂ →</span><span>w₃ →</span>
                <div style="font-size:0.75rem; color:#7f8c8d;">Svari</div>
            </div>
            <div style="display:flex; flex-direction:column; align-items:center;">
                <div style="width:56px; height:56px; border-radius:50%; background:#00BCD4;
                            border:2px solid #00838F; display:flex; align-items:center; justify-content:center;
                            font-weight:700; font-size:1.2rem; color:#fff;">Σ</div>
                <div style="font-size:0.75rem; color:#7f8c8d; margin-top:0.2rem;">Summa</div>
            </div>
            <span style="font-size:1.5rem; color:#90a4ae; padding:0 0.3rem;">→</span>
            <div style="display:flex; flex-direction:column; align-items:center;">
                <div style="padding:0.6rem 1rem; background:#f0fafa; border:2px solid #00BCD4;
                            border-radius:6px; font-weight:600; font-size:1rem; color:#2c3e50;">f(Σ)</div>
                <div style="font-size:0.75rem; color:#7f8c8d; margin-top:0.2rem;">Aktivācija</div>
            </div>
            <span style="font-size:1.5rem; color:#90a4ae; padding:0 0.3rem;">→</span>
            <div style="display:flex; flex-direction:column; align-items:center;">
                <div style="width:48px; height:48px; border-radius:50%; background:#e8f5e9;
                            border:2px solid #27ae60; display:flex; align-items:center; justify-content:center;
                            font-weight:600; font-size:1rem; color:#2c3e50;">ŷ</div>
                <div style="font-size:0.75rem; color:#7f8c8d; margin-top:0.2rem;">Izeja</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
