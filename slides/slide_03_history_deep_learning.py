import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Atdzimšana", "No backpropagation līdz Transformer arhitektūrai")

    # ── Row 1: 3 milestones ──────────────────────────────────────
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div style="background:#f0fafa; border-radius:8px; padding:1rem 1.2rem;
                    border-left:4px solid #00BCD4; height:100%;">
            <div style="font-size:1.5rem; font-weight:700; color:#00BCD4;">1986</div>
            <div style="font-size:1.05rem; font-weight:600; color:#2c3e50; margin:0.3rem 0;">
                Hinton & Rumelhart</div>
            <div style="font-size:0.9rem; color:#5d6d7e; line-height:1.5;">
                Backpropagation strādā! Kļūdas signāls izplatās atpakaļ cauri slāņiem —
                tīkli sāk mācīties.</div>
            <span style="display:inline-block; margin-top:0.4rem; font-size:0.75rem; font-weight:600;
                         padding:0.15rem 0.5rem; border-radius:3px; background:#e0f7fa; color:#00838F;">
                pamatideja</span>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div style="background:#f0fafa; border-radius:8px; padding:1rem 1.2rem;
                    border-left:4px solid #00BCD4; height:100%;">
            <div style="font-size:1.5rem; font-weight:700; color:#00BCD4;">1997</div>
            <div style="font-size:1.05rem; font-weight:600; color:#2c3e50; margin:0.3rem 0;">
                Hochreiter & Schmidhuber — LSTM</div>
            <div style="font-size:0.9rem; color:#5d6d7e; line-height:1.5;">
                Long Short-Term Memory — šūnas, kas spēj atcerēties kontekstu.
                Tīkli pirmo reizi iegūst kaut ko līdzīgu atmiņai.</div>
            <span style="display:inline-block; margin-top:0.4rem; font-size:0.75rem; font-weight:600;
                         padding:0.15rem 0.5rem; border-radius:3px; background:#e0f7fa; color:#00838F;">
                atmiņa tīklos</span>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div style="background:#f0fafa; border-radius:8px; padding:1rem 1.2rem;
                    border-left:4px solid #00838F; height:100%;
                    box-shadow:0 2px 10px rgba(0,188,212,0.1);">
            <div style="font-size:1.5rem; font-weight:700; color:#00838F;">2012</div>
            <div style="font-size:1.05rem; font-weight:600; color:#2c3e50; margin:0.3rem 0;">
                AlexNet — Deep learning uzvar</div>
            <div style="font-size:0.9rem; color:#5d6d7e; line-height:1.5;">
                ImageNet sacensībā kļūdu līmenis nokrīt no ~26% uz ~16%.
                GPU pierāda: dziļie tīkli pārspēj rokām rakstītus algoritmus.</div>
            <span style="display:inline-block; margin-top:0.4rem; font-size:0.75rem; font-weight:600;
                         padding:0.15rem 0.5rem; border-radius:3px; background:#e8f5e9; color:#2e7d32;">
                kļūda: 26% → 16%</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)

    # ── Row 2: 2 milestones + Transformer diagram ────────────────
    c4, c5, c6 = st.columns([1, 1, 1.5])

    with c4:
        st.markdown("""
        <div style="background:#f5f7fa; border-radius:8px; padding:1rem 1.2rem;
                    border-left:4px solid #00BCD4; height:100%;">
            <div style="font-size:1.5rem; font-weight:700; color:#00BCD4;">2014</div>
            <div style="font-size:1.05rem; font-weight:600; color:#2c3e50; margin:0.3rem 0;">
                Goodfellow — GAN</div>
            <div style="font-size:0.9rem; color:#5d6d7e; line-height:1.5;">
                Ģeneratīvie pretinieku tīkli — divi tīkli sacenšas,
                un viens iemācās <em>radīt</em> jaunus datus.</div>
            <span style="display:inline-block; margin-top:0.4rem; font-size:0.75rem; font-weight:600;
                         padding:0.15rem 0.5rem; border-radius:3px; background:#e0f7fa; color:#00838F;">
                ģenerēšana</span>
        </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown("""
        <div style="background:#f0fafa; border-radius:8px; padding:1rem 1.2rem;
                    border-left:4px solid #00838F; height:100%;
                    box-shadow:0 2px 10px rgba(0,188,212,0.1);">
            <div style="font-size:1.5rem; font-weight:700; color:#00838F;">2017</div>
            <div style="font-size:1.05rem; font-weight:600; color:#2c3e50; margin:0.3rem 0;">
                "Attention Is All You Need"</div>
            <div style="font-size:0.9rem; color:#5d6d7e; line-height:1.5;">
                Transformer arhitektūra — modelis "skatās" uz visu tekstu vienlaikus.
                Pamats visam modernai AI — GPT, Claude, BERT.</div>
            <span style="display:inline-block; margin-top:0.4rem; font-size:0.75rem; font-weight:600;
                         padding:0.15rem 0.5rem; border-radius:3px; background:#e0f7fa; color:#00838F;">
                pamats modernai AI</span>
        </div>
        """, unsafe_allow_html=True)

    with c6:
        st.markdown("""
        <div style="background:#f5f7fa; border-radius:8px; padding:1.2rem; height:100%; text-align:center;">
            <div style="font-size:0.75rem; font-weight:600; color:#7f8c8d; text-transform:uppercase;
                        letter-spacing:1px; margin-bottom:0.8rem;">
                Transformer — vienkāršota shēma</div>
            <div style="display:flex; align-items:center; justify-content:center; gap:0.3rem; flex-wrap:wrap;">
                <div style="background:#fff; border:2px solid #00BCD4; border-radius:6px;
                            padding:0.5rem 0.7rem; font-size:0.85rem; font-weight:600; color:#2c3e50;">
                    Ievade</div>
                <span style="color:#90a4ae; font-size:1.2rem;">→</span>
                <div style="background:#00BCD4; border:2px solid #00838F; border-radius:6px;
                            padding:0.5rem 0.7rem; font-size:0.85rem; font-weight:600; color:#fff;
                            box-shadow:0 2px 8px rgba(0,188,212,0.25);">
                    Attention<br><span style="font-size:0.7rem; font-weight:400;">Q·K·V</span></div>
                <span style="color:#90a4ae; font-size:1.2rem;">→</span>
                <div style="background:#fff; border:2px solid #00BCD4; border-radius:6px;
                            padding:0.5rem 0.7rem; font-size:0.85rem; font-weight:600; color:#2c3e50;">
                    Feed-Forward</div>
                <span style="color:#90a4ae; font-size:1.2rem;">→</span>
                <div style="background:#fff; border:2px solid #00BCD4; border-radius:6px;
                            padding:0.5rem 0.7rem; font-size:0.85rem; font-weight:600; color:#2c3e50;">
                    × N slāņi</div>
                <span style="color:#90a4ae; font-size:1.2rem;">→</span>
                <div style="background:#fff; border:2px solid #00BCD4; border-radius:6px;
                            padding:0.5rem 0.7rem; font-size:0.85rem; font-weight:600; color:#2c3e50;">
                    Izeja</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <p style="color:#7f8c8d; margin-top:1rem; font-size:0.92rem; text-align:center;">
    No 1986. līdz 2017. — trīsdesmit viens gads. Idejas bija sen — trūka aparatūras un datu.
    </p>
    """, unsafe_allow_html=True)
