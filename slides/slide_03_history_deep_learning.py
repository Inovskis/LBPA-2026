import streamlit as st
from components.navigation import slide_header
from components.media import show_image


def render():
    slide_header("Atdzimšana", "No backpropagation līdz Transformer arhitektūrai")

    # ── Image + milestone cards ────────────────────────────────────
    col_img, col_cards = st.columns([1, 1.2])

    with col_img:
        show_image("deep_learning_evolution.png",
                   caption="No viena perceptrona līdz dziļajiem tīkliem", width=500)

    with col_cards:
        st.markdown("""
        <div style="display:flex; flex-direction:column; gap:0.6rem;">
            <div style="background:#f0fafa; border-radius:6px; padding:0.8rem 1rem;
                        border-left:4px solid #00BCD4;">
                <span style="font-size:1.2rem; font-weight:700; color:#00BCD4;">1986</span>
                <span style="font-weight:600; color:#2c3e50; margin-left:0.5rem;">
                    Hinton & Rumelhart — Backpropagation strādā</span>
                <div style="font-size:0.88rem; color:#5d6d7e; margin-top:0.2rem;">
                    Kļūdas signāls izplatās atpakaļ cauri slāņiem — tīkli sāk mācīties.</div>
            </div>
            <div style="background:#f0fafa; border-radius:6px; padding:0.8rem 1rem;
                        border-left:4px solid #00BCD4;">
                <span style="font-size:1.2rem; font-weight:700; color:#00BCD4;">1997</span>
                <span style="font-weight:600; color:#2c3e50; margin-left:0.5rem;">
                    Hochreiter & Schmidhuber — LSTM</span>
                <div style="font-size:0.88rem; color:#5d6d7e; margin-top:0.2rem;">
                    Long Short-Term Memory — tīkli pirmo reizi iegūst kaut ko līdzīgu atmiņai.</div>
            </div>
            <div style="background:#f0fafa; border-radius:6px; padding:0.8rem 1rem;
                        border-left:4px solid #00838F;
                        box-shadow:0 2px 8px rgba(0,188,212,0.1);">
                <span style="font-size:1.2rem; font-weight:700; color:#00838F;">2012</span>
                <span style="font-weight:600; color:#2c3e50; margin-left:0.5rem;">
                    AlexNet — Deep learning uzvar ImageNet</span>
                <div style="font-size:0.88rem; color:#5d6d7e; margin-top:0.2rem;">
                    Kļūdu līmenis: 26% → 16%. GPU pierāda: dziļie tīkli pārspēj visu iepriekšējo.</div>
            </div>
            <div style="background:#f0fafa; border-radius:6px; padding:0.8rem 1rem;
                        border-left:4px solid #00BCD4;">
                <span style="font-size:1.2rem; font-weight:700; color:#00BCD4;">2014</span>
                <span style="font-weight:600; color:#2c3e50; margin-left:0.5rem;">
                    Goodfellow — GAN</span>
                <div style="font-size:0.88rem; color:#5d6d7e; margin-top:0.2rem;">
                    Divi tīkli sacenšas — viens iemācās <em>radīt</em> jaunus datus.</div>
            </div>
            <div style="background:#f0fafa; border-radius:6px; padding:0.8rem 1rem;
                        border-left:4px solid #00838F;
                        box-shadow:0 2px 8px rgba(0,188,212,0.1);">
                <span style="font-size:1.2rem; font-weight:700; color:#00838F;">2017</span>
                <span style="font-weight:600; color:#2c3e50; margin-left:0.5rem;">
                    "Attention Is All You Need" — Transformer</span>
                <div style="font-size:0.88rem; color:#5d6d7e; margin-top:0.2rem;">
                    Pamats visam modernai AI — GPT, Claude, BERT. Modelis "skatās" uz visu vienlaikus.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <p style="color:#7f8c8d; margin-top:0.8rem; font-size:0.92rem; text-align:center;">
    No 1986. līdz 2017. — trīsdesmit viens gads. Idejas bija sen — trūka aparatūras un datu.
    </p>
    """, unsafe_allow_html=True)
