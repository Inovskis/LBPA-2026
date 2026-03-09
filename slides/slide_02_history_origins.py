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
                lai atpazītu vienkāršus attēlus.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div style="background:#fdf2f2; border-radius:8px; padding:1rem 1.2rem; height:100%;
                    border-top:4px solid #90a4ae;">
            <div style="font-size:1.6rem; font-weight:700; color:#90a4ae;">1969</div>
            <div style="font-size:1.05rem; font-weight:600; color:#2c3e50; margin:0.4rem 0 0.3rem;">
                Minsky & Papert — strupceļš</div>
            <div style="font-size:0.92rem; color:#5d6d7e; line-height:1.5;">
                Grāmata pierāda: viens slānis nevar atrisināt pat XOR.
                Finansējums apstājas. Interese par neironu tīkliem apsīkst uz gadiem.
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
                Akadēmiskā pasaule to gandrīz neievēro.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Perceptron diagram — full width ────────────────────────────
    st.markdown("""
    <div style="background:#f5f7fa; border-radius:8px; padding:1.2rem; margin-top:1.5rem;">
        <div style="font-size:0.8rem; font-weight:600; color:#7f8c8d; text-transform:uppercase;
                    letter-spacing:1px; margin-bottom:0.6rem; text-align:center;">
            Perceptrons — vienkāršākais neironu tīkla elements
        </div>
        <svg viewBox="0 0 800 160" width="100%" height="140"
             xmlns="http://www.w3.org/2000/svg" style="display:block; margin:0 auto;">

            <!-- input nodes -->
            <circle cx="80" cy="30"  r="22" fill="#e0f7fa" stroke="#00BCD4" stroke-width="2"/>
            <text x="80"  y="35"  text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="600">x₁</text>
            <circle cx="80" cy="80"  r="22" fill="#e0f7fa" stroke="#00BCD4" stroke-width="2"/>
            <text x="80"  y="85"  text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="600">x₂</text>
            <circle cx="80" cy="130" r="22" fill="#e0f7fa" stroke="#00BCD4" stroke-width="2"/>
            <text x="80"  y="135" text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="600">x₃</text>

            <!-- weight lines -->
            <line x1="102" y1="30"  x2="278" y2="72" stroke="#00BCD4" stroke-width="2" opacity="0.5"/>
            <text x="185" y="42" font-size="12" fill="#00838F" font-weight="600">w₁</text>
            <line x1="102" y1="80"  x2="278" y2="80" stroke="#00BCD4" stroke-width="2" opacity="0.5"/>
            <text x="185" y="73" font-size="12" fill="#00838F" font-weight="600">w₂</text>
            <line x1="102" y1="130" x2="278" y2="88" stroke="#00BCD4" stroke-width="2" opacity="0.5"/>
            <text x="185" y="120" font-size="12" fill="#00838F" font-weight="600">w₃</text>

            <!-- sum node -->
            <circle cx="300" cy="80" r="28" fill="#00BCD4" stroke="#00838F" stroke-width="2"/>
            <text x="300" y="86" text-anchor="middle" font-size="16" fill="#fff" font-weight="700">Σ</text>

            <!-- arrow -->
            <line x1="328" y1="80" x2="418" y2="80" stroke="#2c3e50" stroke-width="2"
                  marker-end="url(#arr2)"/>
            <defs><marker id="arr2" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto">
                <path d="M0,0 L8,4 L0,8" fill="#2c3e50"/></marker></defs>

            <!-- activation -->
            <rect x="420" y="54" width="100" height="52" rx="6" fill="#f0fafa" stroke="#00BCD4" stroke-width="2"/>
            <text x="470" y="84" text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="600">f(Σ)</text>

            <!-- arrow to output -->
            <line x1="520" y1="80" x2="600" y2="80" stroke="#2c3e50" stroke-width="2"
                  marker-end="url(#arr2)"/>

            <!-- output -->
            <circle cx="630" cy="80" r="24" fill="#e8f5e9" stroke="#27ae60" stroke-width="2"/>
            <text x="630" y="86" text-anchor="middle" font-size="14" fill="#2c3e50" font-weight="600">ŷ</text>

            <!-- labels -->
            <text x="80"  y="157" text-anchor="middle" font-size="11" fill="#7f8c8d">Ieejas</text>
            <text x="300" y="118" text-anchor="middle" font-size="11" fill="#7f8c8d">Summa</text>
            <text x="470" y="118" text-anchor="middle" font-size="11" fill="#7f8c8d">Aktivācija</text>
            <text x="630" y="114" text-anchor="middle" font-size="11" fill="#7f8c8d">Izeja</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="color:#7f8c8d; margin-top:0.8rem; font-size:0.95rem; text-align:center;">
    Ideja par mākslīgo neironu ir vecāka nekā datori paši. Tik vienkārša shēma —
    un tomēr no tās izauga viss, ko šodien saucam par neironu tīkliem.
    </p>
    """, unsafe_allow_html=True)
