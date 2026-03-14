import streamlit as st
from components.navigation import slide_header
from components.media import show_image


def render():
    slide_header("Lēciens", "No GPT-3 līdz šodienai")

    # ── Image + cards ──────────────────────────────────────────────
    col_img, col_cards = st.columns([1, 1.3])

    with col_img:
        show_image("exponential_growth.png",
                   caption="Eksponenciāls pieaugums", width=450)

    with col_cards:
        st.markdown("""
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.6rem;">
            <div style="background:#f5f7fa; border-radius:6px; padding:0.8rem 1rem;
                        border-top:3px solid #b2ebf2;">
                <div style="font-size:1.3rem; font-weight:700; color:#00BCD4;">2020</div>
                <div style="font-weight:600; color:#2c3e50; margin:0.2rem 0;">GPT-3</div>
                <div style="font-size:0.85rem; color:#5d6d7e; line-height:1.45;">
                    175 miljardi parametru. Pirmais universālais valodas modelis.</div>
            </div>
            <div style="background:#f0fafa; border-radius:6px; padding:0.8rem 1rem;
                        border-top:3px solid #00BCD4;
                        box-shadow:0 2px 8px rgba(0,188,212,0.1);">
                <div style="font-size:1.3rem; font-weight:700; color:#00838F;">2022</div>
                <div style="font-weight:600; color:#2c3e50; margin:0.2rem 0;">ChatGPT</div>
                <div style="font-size:0.85rem; color:#5d6d7e; line-height:1.45;">
                    100M lietotāju 2 mēnešos. AI kļūst par ikdienas sarunu tēmu.</div>
            </div>
            <div style="background:#f0fafa; border-radius:6px; padding:0.8rem 1rem;
                        border-top:3px solid #00BCD4;">
                <div style="font-size:1.3rem; font-weight:700; color:#00BCD4;">2023</div>
                <div style="font-weight:600; color:#2c3e50; margin:0.2rem 0;">GPT-4, Claude, open-source</div>
                <div style="font-size:0.85rem; color:#5d6d7e; line-height:1.45;">
                    Saprot kodu, matemātiku. Llama, Mistral demokratizē pieeju.</div>
            </div>
            <div style="background:#f5f7fa; border-radius:6px; padding:0.8rem 1rem;
                        border-top:3px solid #00838F;">
                <div style="font-size:1.3rem; font-weight:700; color:#00838F;">2024–26</div>
                <div style="font-weight:600; color:#2c3e50; margin:0.2rem 0;">Koda ģenerēšana & aģenti</div>
                <div style="font-size:0.85rem; color:#5d6d7e; line-height:1.45;">
                    Multimodālie modeļi. No sarunu rīka — uz darba instrumentu.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Growth comparison ──────────────────────────────────────────
    st.markdown("""
    <div style="background:#f5f7fa; border-radius:8px; padding:1rem 1.5rem;">
        <div style="font-size:0.8rem; font-weight:600; color:#7f8c8d; text-transform:uppercase;
                    letter-spacing:1px; margin-bottom:0.5rem;">
            Laiks līdz 100 miljoniem lietotāju</div>
        <div style="display:flex; gap:0.8rem; flex-wrap:wrap;">
            <div style="flex:1; min-width:80px; text-align:center;">
                <div style="font-size:0.82rem; color:#5d6d7e;">Telefons</div>
                <div style="height:6px; background:#e0e6ed; border-radius:3px; overflow:hidden; margin:0.2rem 0;">
                    <div style="height:100%; width:100%; background:#cfd8dc; border-radius:3px;"></div></div>
                <div style="font-size:0.85rem; font-weight:600; color:#90a4ae;">75 gadi</div>
            </div>
            <div style="flex:1; min-width:80px; text-align:center;">
                <div style="font-size:0.82rem; color:#5d6d7e;">Internets</div>
                <div style="height:6px; background:#e0e6ed; border-radius:3px; overflow:hidden; margin:0.2rem 0;">
                    <div style="height:100%; width:9.3%; background:#b0bec5; border-radius:3px;"></div></div>
                <div style="font-size:0.85rem; font-weight:600; color:#78909c;">7 gadi</div>
            </div>
            <div style="flex:1; min-width:80px; text-align:center;">
                <div style="font-size:0.82rem; color:#5d6d7e;">Instagram</div>
                <div style="height:6px; background:#e0e6ed; border-radius:3px; overflow:hidden; margin:0.2rem 0;">
                    <div style="height:100%; width:3.3%; background:#80cbc4; border-radius:3px;"></div></div>
                <div style="font-size:0.85rem; font-weight:600; color:#00897B;">2.5 gadi</div>
            </div>
            <div style="flex:1; min-width:80px; text-align:center;">
                <div style="font-size:0.82rem; color:#5d6d7e;">TikTok</div>
                <div style="height:6px; background:#e0e6ed; border-radius:3px; overflow:hidden; margin:0.2rem 0;">
                    <div style="height:100%; width:1.2%; background:#4dd0e1; border-radius:3px;"></div></div>
                <div style="font-size:0.85rem; font-weight:600; color:#00ACC1;">9 mēn.</div>
            </div>
            <div style="flex:1; min-width:80px; text-align:center; background:#f0fafa;
                        border-radius:6px; padding:0.2rem; border:1px solid #b2ebf2;">
                <div style="font-size:0.82rem; font-weight:600; color:#00838F;">ChatGPT</div>
                <div style="height:6px; background:#e0e6ed; border-radius:3px; overflow:hidden; margin:0.2rem 0;">
                    <div style="height:100%; width:0.3%; background:#00BCD4; border-radius:3px;
                                box-shadow:0 0 8px rgba(0,188,212,0.5);"></div></div>
                <div style="font-size:0.85rem; font-weight:600; color:#00838F;">2 mēneši</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="accent-box" style="margin-top:0.8rem;">
        Un tad kāds inženieris padomāja — ko, ja šo varētu izmantot aprēķinos?
    </div>
    """, unsafe_allow_html=True)
