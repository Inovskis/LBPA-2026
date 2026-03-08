import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Lēciens", "No GPT-3 līdz šodienai")

    # ── 4-column cards for key moments ──────────────────────────
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div style="background:#f5f7fa; border-radius:8px; padding:1rem 1.2rem;
                    border-top:4px solid #b2ebf2; height:100%;">
            <div style="font-size:1.5rem; font-weight:700; color:#00BCD4;">2020</div>
            <div style="font-size:1.02rem; font-weight:600; color:#2c3e50; margin:0.3rem 0;">
                GPT-3</div>
            <div style="font-size:0.88rem; color:#5d6d7e; line-height:1.45;">
                175 miljardi parametru. Pirmais modelis, kas raksta saskarīgu tekstu
                un atbild uz jautājumiem bez specifiskas apmācības.</div>
            <span style="display:inline-block; margin-top:0.4rem; font-size:0.75rem; font-weight:600;
                         padding:0.15rem 0.5rem; border-radius:3px; background:#e0f7fa; color:#00838F;">
                175B parametru</span>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div style="background:#f0fafa; border-radius:8px; padding:1rem 1.2rem;
                    border-top:4px solid #00BCD4; height:100%;
                    box-shadow:0 2px 10px rgba(0,188,212,0.1);">
            <div style="font-size:1.5rem; font-weight:700; color:#00838F;">2022</div>
            <div style="font-size:1.02rem; font-weight:600; color:#2c3e50; margin:0.3rem 0;">
                ChatGPT</div>
            <div style="font-size:0.88rem; color:#5d6d7e; line-height:1.45;">
                100 miljoni lietotāju 2 mēnešos — ātrākais pieaugums tehnoloģiju vēsturē.
                AI kļūst par ikdienas sarunu tēmu.</div>
            <span style="display:inline-block; margin-top:0.4rem; font-size:0.75rem; font-weight:600;
                         padding:0.15rem 0.5rem; border-radius:3px; background:#e0f7fa; color:#00838F;">
                100M / 2 mēneši</span>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div style="background:#f0fafa; border-radius:8px; padding:1rem 1.2rem;
                    border-top:4px solid #00BCD4; height:100%;">
            <div style="font-size:1.5rem; font-weight:700; color:#00BCD4;">2023</div>
            <div style="font-size:1.02rem; font-weight:600; color:#2c3e50; margin:0.3rem 0;">
                GPT-4, Claude, open-source</div>
            <div style="font-size:0.88rem; color:#5d6d7e; line-height:1.45;">
                Modeļi saprot kodu, matemātiku, kontekstu. Atvērtā koda alternatīvas
                (Llama, Mistral) demokratizē pieeju.</div>
            <span style="display:inline-block; margin-top:0.4rem; font-size:0.75rem; font-weight:600;
                         padding:0.15rem 0.5rem; border-radius:3px; background:#e0f7fa; color:#00838F;">
                kods + matemātika</span>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div style="background:#f5f7fa; border-radius:8px; padding:1rem 1.2rem;
                    border-top:4px solid #00838F; height:100%;">
            <div style="font-size:1.5rem; font-weight:700; color:#00838F;">2024–26</div>
            <div style="font-size:1.02rem; font-weight:600; color:#2c3e50; margin:0.3rem 0;">
                Koda ģenerēšana & aģenti</div>
            <div style="font-size:0.88rem; color:#5d6d7e; line-height:1.45;">
                Multimodālie modeļi redz attēlus un raksta kodu.
                AI asistenti veic vairāku soļu uzdevumus. No sarunu rīka — uz darba instrumentu.</div>
            <span style="display:inline-block; margin-top:0.4rem; font-size:0.75rem; font-weight:600;
                         padding:0.15rem 0.5rem; border-radius:3px; background:#e0f7fa; color:#00838F;">
                rīks → kolēģis</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:1.2rem;'></div>", unsafe_allow_html=True)

    # ── Growth comparison — horizontal bar chart ──────────────────
    st.markdown("""
    <div style="background:#f5f7fa; border-radius:8px; padding:1.2rem 1.5rem;">
        <div style="font-size:0.8rem; font-weight:600; color:#7f8c8d; text-transform:uppercase;
                    letter-spacing:1px; margin-bottom:0.8rem;">
            Laiks līdz 100 miljoniem lietotāju</div>
        <div style="display:flex; gap:0.8rem; flex-wrap:wrap;">
            <div style="flex:1; min-width:100px; text-align:center;">
                <div style="font-size:0.82rem; color:#5d6d7e;">Telefons</div>
                <div style="height:8px; background:#e0e6ed; border-radius:4px; overflow:hidden; margin:0.3rem 0;">
                    <div style="height:100%; width:100%; background:#cfd8dc; border-radius:4px;"></div></div>
                <div style="font-size:0.9rem; font-weight:600; color:#90a4ae;">75 gadi</div>
            </div>
            <div style="flex:1; min-width:100px; text-align:center;">
                <div style="font-size:0.82rem; color:#5d6d7e;">Internets</div>
                <div style="height:8px; background:#e0e6ed; border-radius:4px; overflow:hidden; margin:0.3rem 0;">
                    <div style="height:100%; width:9.3%; background:#b0bec5; border-radius:4px;"></div></div>
                <div style="font-size:0.9rem; font-weight:600; color:#78909c;">7 gadi</div>
            </div>
            <div style="flex:1; min-width:100px; text-align:center;">
                <div style="font-size:0.82rem; color:#5d6d7e;">Instagram</div>
                <div style="height:8px; background:#e0e6ed; border-radius:4px; overflow:hidden; margin:0.3rem 0;">
                    <div style="height:100%; width:3.3%; background:#80cbc4; border-radius:4px;"></div></div>
                <div style="font-size:0.9rem; font-weight:600; color:#00897B;">2.5 gadi</div>
            </div>
            <div style="flex:1; min-width:100px; text-align:center;">
                <div style="font-size:0.82rem; color:#5d6d7e;">TikTok</div>
                <div style="height:8px; background:#e0e6ed; border-radius:4px; overflow:hidden; margin:0.3rem 0;">
                    <div style="height:100%; width:1.2%; background:#4dd0e1; border-radius:4px;"></div></div>
                <div style="font-size:0.9rem; font-weight:600; color:#00ACC1;">9 mēn.</div>
            </div>
            <div style="flex:1; min-width:100px; text-align:center; background:#f0fafa;
                        border-radius:6px; padding:0.3rem; border:1px solid #b2ebf2;">
                <div style="font-size:0.82rem; font-weight:600; color:#00838F;">ChatGPT</div>
                <div style="height:8px; background:#e0e6ed; border-radius:4px; overflow:hidden; margin:0.3rem 0;">
                    <div style="height:100%; width:0.3%; background:#00BCD4; border-radius:4px;
                                box-shadow:0 0 8px rgba(0,188,212,0.5);"></div></div>
                <div style="font-size:0.9rem; font-weight:600; color:#00838F;">2 mēneši</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Bottom note ───────────────────────────────────────────────
    st.markdown("""
    <div class="accent-box" style="margin-top:1.2rem;">
        Un tad kāds inženieris padomāja — ko, ja šo varētu izmantot aprēķinos?
    </div>
    """, unsafe_allow_html=True)
