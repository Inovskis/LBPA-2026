import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Kā tas sākās", "No matemātiskā neirona līdz pirmajai ziemas iemigšanai")

    st.markdown("""
    <p class="slide-text">
    Ideja par mākslīgo neironu ir vecāka nekā datori paši. Pirms kāds uzrakstīja
    pirmo programmu, matemātiķi jau mēģināja saprast — vai domāšanu var reducēt
    līdz skaitļiem un svariem?
    </p>
    """, unsafe_allow_html=True)

    # ── CSS timeline ──────────────────────────────────────────────
    st.markdown("""
    <style>
    .tl-origins {
        position: relative;
        margin: 2rem 0 1.5rem 0;
        padding-left: 2.2rem;
    }
    .tl-origins::before {
        content: '';
        position: absolute;
        left: 0.55rem;
        top: 0;
        bottom: 0;
        width: 3px;
        background: linear-gradient(180deg, #00BCD4 0%, #b2ebf2 100%);
        border-radius: 2px;
    }
    .tl-origins .tl-item {
        position: relative;
        margin-bottom: 1.6rem;
        padding-left: 1.4rem;
        animation: fadeIn 0.5s ease-out both;
    }
    .tl-origins .tl-item:nth-child(1) { animation-delay: 0.1s; }
    .tl-origins .tl-item:nth-child(2) { animation-delay: 0.25s; }
    .tl-origins .tl-item:nth-child(3) { animation-delay: 0.4s; }
    .tl-origins .tl-item:nth-child(4) { animation-delay: 0.55s; }
    .tl-origins .tl-item::before {
        content: '';
        position: absolute;
        left: -1.82rem;
        top: 0.35rem;
        width: 13px;
        height: 13px;
        background: #00BCD4;
        border: 3px solid #ffffff;
        border-radius: 50%;
        box-shadow: 0 0 0 2px #00BCD4;
        z-index: 1;
    }
    .tl-origins .tl-item.winter::before {
        background: #90a4ae;
        box-shadow: 0 0 0 2px #90a4ae;
    }
    .tl-origins .tl-year {
        display: inline-block;
        font-size: 0.85rem;
        font-weight: 600;
        color: #ffffff;
        background: #00BCD4;
        padding: 0.15rem 0.6rem;
        border-radius: 3px;
        margin-bottom: 0.3rem;
    }
    .tl-origins .tl-item.winter .tl-year {
        background: #90a4ae;
    }
    .tl-origins .tl-heading {
        font-size: 1.05rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 0.2rem 0 0.15rem 0;
    }
    .tl-origins .tl-desc {
        font-size: 0.95rem;
        color: #5d6d7e;
        line-height: 1.5;
    }
    </style>

    <div class="tl-origins fade-in">

        <div class="tl-item">
            <span class="tl-year">1943</span>
            <div class="tl-heading">McCulloch &amp; Pitts</div>
            <div class="tl-desc">
                Pirmais matemātiskais neirona modelis — vienkārša funkcija ar ieejas
                signāliem un sliekšņa vērtību. Nevis smadzenes, bet loģikas vārti.
            </div>
        </div>

        <div class="tl-item">
            <span class="tl-year">1958</span>
            <div class="tl-heading">Frank Rosenblatt — Perceptrons</div>
            <div class="tl-desc">
                Pirmais mācīšanās algoritms. Mašīna, kas pati maina savus svarus,
                lai atpazītu vienkāršus attēlus. Tolaik šķita — vēl desmit gadi un
                mēs atrisināsim intelektu.
            </div>
        </div>

        <div class="tl-item winter">
            <span class="tl-year">1969</span>
            <div class="tl-heading">Minsky &amp; Papert — "Perceptrons"</div>
            <div class="tl-desc">
                Grāmata, kas stingri matemātiski parāda: viens slānis nevar atrisināt
                pat vienkāršu XOR problēmu. Finansējums apstājas. Sākas pirmā
                <em>AI ziema</em>.
            </div>
        </div>

        <div class="tl-item">
            <span class="tl-year">1974</span>
            <div class="tl-heading">Paul Werbos — backpropagation</div>
            <div class="tl-desc">
                Doktora darbā apraksta ideju par kļūdas atpakaļizplatīšanos
                caur vairākiem slāņiem. Akadēmiskā pasaule to gandrīz neievēro.
                Ideja guļ pusotra gadu desmitu.
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ── Perceptron diagram ────────────────────────────────────────
    st.markdown("""
    <style>
    .perceptron-wrap {
        background: #f5f7fa;
        border-radius: 8px;
        padding: 1.5rem 1rem 1.2rem 1rem;
        margin-top: 1.5rem;
        overflow-x: auto;
    }
    .perceptron-wrap .diagram-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #7f8c8d;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.8rem;
    }
    .perceptron-svg { display: block; margin: 0 auto; }
    </style>

    <div class="perceptron-wrap fade-in">
        <div class="diagram-label">Perceptrons — vienkāršākais neironu tīkla elements</div>
        <svg class="perceptron-svg" viewBox="0 0 620 200" width="100%" height="200"
             xmlns="http://www.w3.org/2000/svg" style="max-width:620px;">

            <!-- input nodes -->
            <circle cx="60" cy="40"  r="22" fill="#e0f7fa" stroke="#00BCD4" stroke-width="2"/>
            <text x="60"  y="45"  text-anchor="middle" font-size="13" fill="#2c3e50" font-weight="600">x₁</text>

            <circle cx="60" cy="100" r="22" fill="#e0f7fa" stroke="#00BCD4" stroke-width="2"/>
            <text x="60"  y="105" text-anchor="middle" font-size="13" fill="#2c3e50" font-weight="600">x₂</text>

            <circle cx="60" cy="160" r="22" fill="#e0f7fa" stroke="#00BCD4" stroke-width="2"/>
            <text x="60"  y="165" text-anchor="middle" font-size="13" fill="#2c3e50" font-weight="600">x₃</text>

            <!-- weight labels -->
            <line x1="82" y1="40"  x2="228" y2="90"  stroke="#00BCD4" stroke-width="2" opacity="0.6"/>
            <text x="148" y="56"  font-size="11" fill="#00838F" font-weight="600">w₁</text>

            <line x1="82" y1="100" x2="228" y2="100" stroke="#00BCD4" stroke-width="2" opacity="0.6"/>
            <text x="148" y="93"  font-size="11" fill="#00838F" font-weight="600">w₂</text>

            <line x1="82" y1="160" x2="228" y2="110" stroke="#00BCD4" stroke-width="2" opacity="0.6"/>
            <text x="148" y="148" font-size="11" fill="#00838F" font-weight="600">w₃</text>

            <!-- sum node -->
            <circle cx="250" cy="100" r="28" fill="#00BCD4" stroke="#00838F" stroke-width="2"/>
            <text x="250" y="106" text-anchor="middle" font-size="15" fill="#ffffff" font-weight="700">Σ</text>

            <!-- arrow to activation -->
            <line x1="278" y1="100" x2="348" y2="100" stroke="#2c3e50" stroke-width="2"
                  marker-end="url(#arr)"/>
            <defs><marker id="arr" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto">
                <path d="M0,0 L8,4 L0,8" fill="#2c3e50"/></marker></defs>

            <!-- activation -->
            <rect x="350" y="74" width="90" height="52" rx="6" fill="#f0fafa" stroke="#00BCD4" stroke-width="2"/>
            <text x="395" y="104" text-anchor="middle" font-size="13" fill="#2c3e50" font-weight="600">f(Σ)</text>

            <!-- arrow to output -->
            <line x1="440" y1="100" x2="500" y2="100" stroke="#2c3e50" stroke-width="2"
                  marker-end="url(#arr)"/>

            <!-- output node -->
            <circle cx="530" cy="100" r="24" fill="#e8f5e9" stroke="#27ae60" stroke-width="2"/>
            <text x="530" y="106" text-anchor="middle" font-size="13" fill="#2c3e50" font-weight="600">ŷ</text>

            <!-- labels row -->
            <text x="60"  y="197" text-anchor="middle" font-size="10" fill="#7f8c8d">Ieejas</text>
            <text x="250" y="145" text-anchor="middle" font-size="10" fill="#7f8c8d">Summa</text>
            <text x="395" y="142" text-anchor="middle" font-size="10" fill="#7f8c8d">Aktivācija</text>
            <text x="530" y="140" text-anchor="middle" font-size="10" fill="#7f8c8d">Izeja</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="slide-text" style="color:#7f8c8d; margin-top:1.5rem;">
    Tik vienkārša shēma — un tomēr no tās izauga viss, ko šodien saucam par
    neironu tīkliem.
    </p>
    """, unsafe_allow_html=True)
