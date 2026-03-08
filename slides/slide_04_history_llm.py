import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Lēciens", "No GPT-3 līdz šodienai")

    st.markdown("""
    <p class="slide-text">
    Pēdējo piecu gadu laikā notika kaut kas, ko neviens īsti neparedzēja —
    valodas modeļi kļuva pietiekami labi, lai ar tiem varētu sarunāties. Un strādāt.
    </p>
    """, unsafe_allow_html=True)

    # ── Horizontal visual timeline with impact stats ──────────────
    st.markdown("""
    <style>
    .tl-llm {
        position: relative;
        margin: 1.8rem 0 0.5rem 0;
    }

    /* horizontal track */
    .tl-llm-track {
        position: relative;
        display: flex;
        justify-content: space-between;
        padding: 0 0.5rem;
    }
    .tl-llm-track::before {
        content: '';
        position: absolute;
        top: 1.55rem;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #b2ebf2 0%, #00BCD4 50%, #00838F 100%);
        border-radius: 2px;
        z-index: 0;
    }
    .tl-llm-node {
        position: relative;
        z-index: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        flex: 1;
        animation: fadeIn 0.5s ease-out both;
    }
    .tl-llm-node:nth-child(1) { animation-delay: 0.1s; }
    .tl-llm-node:nth-child(2) { animation-delay: 0.25s; }
    .tl-llm-node:nth-child(3) { animation-delay: 0.4s; }
    .tl-llm-node:nth-child(4) { animation-delay: 0.55s; }

    .tl-llm-dot {
        width: 16px;
        height: 16px;
        background: #00BCD4;
        border: 3px solid #ffffff;
        border-radius: 50%;
        box-shadow: 0 0 0 2px #00BCD4;
        margin-top: 0.85rem;
    }
    .tl-llm-node.big .tl-llm-dot {
        width: 22px;
        height: 22px;
        margin-top: 0.65rem;
        background: #00838F;
        box-shadow: 0 0 0 3px #00838F, 0 0 14px rgba(0,188,212,0.3);
    }
    .tl-llm-year-lbl {
        font-size: 0.82rem;
        font-weight: 700;
        color: #00838F;
        margin-top: 0.15rem;
    }

    /* cards below the track */
    .tl-llm-cards {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.6rem;
        margin-top: 0.6rem;
    }
    .tl-llm-card {
        background: #f5f7fa;
        border-radius: 6px;
        padding: 0.9rem;
        border-top: 3px solid #b2ebf2;
        animation: fadeIn 0.5s ease-out both;
    }
    .tl-llm-card:nth-child(1) { animation-delay: 0.15s; }
    .tl-llm-card:nth-child(2) { animation-delay: 0.3s; border-top-color: #00BCD4; }
    .tl-llm-card:nth-child(3) { animation-delay: 0.45s; border-top-color: #00BCD4; }
    .tl-llm-card:nth-child(4) { animation-delay: 0.6s; border-top-color: #00838F; }
    .tl-llm-card h4 {
        margin: 0 0 0.3rem 0;
        font-size: 0.95rem;
        font-weight: 600;
        color: #2c3e50;
    }
    .tl-llm-card p {
        margin: 0;
        font-size: 0.88rem;
        color: #5d6d7e;
        line-height: 1.45;
    }
    .tl-llm-card .impact {
        display: inline-block;
        margin-top: 0.4rem;
        font-size: 0.78rem;
        font-weight: 600;
        padding: 0.15rem 0.55rem;
        border-radius: 3px;
        background: #e0f7fa;
        color: #00838F;
    }

    @media (max-width: 700px) {
        .tl-llm-cards { grid-template-columns: 1fr 1fr; }
    }
    </style>

    <div class="tl-llm fade-in">

        <!-- dot track -->
        <div class="tl-llm-track">
            <div class="tl-llm-node">
                <div class="tl-llm-dot"></div>
                <span class="tl-llm-year-lbl">2020</span>
            </div>
            <div class="tl-llm-node big">
                <div class="tl-llm-dot"></div>
                <span class="tl-llm-year-lbl">2022</span>
            </div>
            <div class="tl-llm-node big">
                <div class="tl-llm-dot"></div>
                <span class="tl-llm-year-lbl">2023</span>
            </div>
            <div class="tl-llm-node">
                <div class="tl-llm-dot"></div>
                <span class="tl-llm-year-lbl">2024–26</span>
            </div>
        </div>

        <!-- detail cards -->
        <div class="tl-llm-cards">

            <div class="tl-llm-card">
                <h4>GPT-3</h4>
                <p>175 miljardi parametru. Pirmais modelis, kas spēj rakstīt
                   saskarīgu tekstu, atbildēt uz jautājumiem, tulkot —
                   bez specifiskas apmācības katram uzdevumam.</p>
                <span class="impact">175B parametru</span>
            </div>

            <div class="tl-llm-card">
                <h4>ChatGPT</h4>
                <p>2022. gada novembris. 100 miljoni lietotāju divās mēnešos —
                   ātrākais pieaugums tehnoloģiju vēsturē. AI kļūst par
                   ikdienas sarunu tēmu.</p>
                <span class="impact">100M lietotāju / 2 mēn.</span>
            </div>

            <div class="tl-llm-card">
                <h4>GPT-4, Claude, open-source</h4>
                <p>Kvalitāte pieaug eksponenciāli. Modeļi sāk saprast kodu,
                   matemātiku, kontekstu. Atvērtā koda alternatīvas —
                   Llama, Mistral — demokratizē pieeju.</p>
                <span class="impact">kods + matemātika</span>
            </div>

            <div class="tl-llm-card">
                <h4>Koda ģenerēšana &amp; aģenti</h4>
                <p>Multimodālie modeļi, kas redz attēlus un raksta kodu.
                   AI asistenti, kas veic vairāku soļu uzdevumus.
                   No sarunu rīka — uz darba instrumentu.</p>
                <span class="impact">rīks → kolēģis</span>
            </div>

        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Growth comparison visual ──────────────────────────────────
    st.markdown("""
    <style>
    .growth-compare {
        display: flex;
        gap: 0.8rem;
        margin-top: 1.5rem;
        flex-wrap: wrap;
    }
    .growth-bar-wrap {
        flex: 1;
        min-width: 130px;
        background: #f5f7fa;
        border-radius: 6px;
        padding: 0.7rem 0.9rem;
        text-align: center;
    }
    .growth-bar-wrap .g-label {
        font-size: 0.82rem;
        color: #5d6d7e;
        margin-bottom: 0.3rem;
    }
    .growth-bar-wrap .g-bar-bg {
        height: 8px;
        background: #e0e6ed;
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 0.25rem;
    }
    .growth-bar-wrap .g-bar-fill {
        height: 100%;
        border-radius: 4px;
        background: #00BCD4;
    }
    .growth-bar-wrap .g-time {
        font-size: 0.9rem;
        font-weight: 600;
        color: #2c3e50;
    }
    </style>

    <div style="margin-top:1.4rem;">
        <div style="font-size:0.8rem;font-weight:600;color:#7f8c8d;text-transform:uppercase;
                    letter-spacing:1px;margin-bottom:0.5rem;">
            Laiks līdz 100 miljoniem lietotāju
        </div>
        <div class="growth-compare fade-in">
            <div class="growth-bar-wrap">
                <div class="g-label">Telefons</div>
                <div class="g-bar-bg"><div class="g-bar-fill" style="width:100%;background:#cfd8dc;"></div></div>
                <div class="g-time" style="color:#90a4ae;">75 gadi</div>
            </div>
            <div class="growth-bar-wrap">
                <div class="g-label">Internets</div>
                <div class="g-bar-bg"><div class="g-bar-fill" style="width:9.3%;background:#b0bec5;"></div></div>
                <div class="g-time" style="color:#78909c;">7 gadi</div>
            </div>
            <div class="growth-bar-wrap">
                <div class="g-label">Instagram</div>
                <div class="g-bar-bg"><div class="g-bar-fill" style="width:3.3%;background:#80cbc4;"></div></div>
                <div class="g-time" style="color:#00897B;">2.5 gadi</div>
            </div>
            <div class="growth-bar-wrap">
                <div class="g-label">TikTok</div>
                <div class="g-bar-bg"><div class="g-bar-fill" style="width:1.2%;background:#4dd0e1;"></div></div>
                <div class="g-time" style="color:#00ACC1;">9 mēn.</div>
            </div>
            <div class="growth-bar-wrap" style="background:#f0fafa;border:1px solid #b2ebf2;">
                <div class="g-label" style="font-weight:600;color:#00838F;">ChatGPT</div>
                <div class="g-bar-bg"><div class="g-bar-fill" style="width:0.3%;background:#00BCD4;
                     box-shadow:0 0 8px rgba(0,188,212,0.5);"></div></div>
                <div class="g-time" style="color:#00838F;">2 mēneši</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Bottom note ───────────────────────────────────────────────
    st.markdown("""
    <div class="accent-box" style="margin-top:1.8rem;">
        Un tad kāds inženieris padomāja — ko, ja šo varētu izmantot aprēķinos?
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="slide-text" style="color:#7f8c8d; margin-top:0.8rem;">
    Nevis hype. Nevis "revolūcija ir klāt". Vienkārši — šie rīki tagad eksistē,
    un jautājums ir, ko mēs ar tiem darīsim savā nozarē.
    </p>
    """, unsafe_allow_html=True)
