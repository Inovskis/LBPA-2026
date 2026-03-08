import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Atdzimšana", "No backpropagation līdz Transformer arhitektūrai")

    st.markdown("""
    <p class="slide-text">
    Katrs no šiem soļiem bija iespējams tikai tāpēc, ka mainījās skaitļošanas jauda.
    Idejas bija sen — trūka tikai aparatūras un datu, lai tās pārbaudītu.
    </p>
    """, unsafe_allow_html=True)

    # ── CSS timeline ──────────────────────────────────────────────
    st.markdown("""
    <style>
    .tl-deep {
        position: relative;
        margin: 1.8rem 0 1rem 0;
        display: flex;
        flex-direction: column;
        gap: 0;
    }
    .tl-deep-row {
        display: flex;
        align-items: stretch;
        min-height: 90px;
        animation: fadeIn 0.5s ease-out both;
    }
    .tl-deep-row:nth-child(1) { animation-delay: 0.08s; }
    .tl-deep-row:nth-child(2) { animation-delay: 0.18s; }
    .tl-deep-row:nth-child(3) { animation-delay: 0.28s; }
    .tl-deep-row:nth-child(4) { animation-delay: 0.38s; }
    .tl-deep-row:nth-child(5) { animation-delay: 0.48s; }

    /* left year column */
    .tl-deep-year {
        width: 70px;
        flex-shrink: 0;
        text-align: right;
        padding-right: 1.2rem;
        padding-top: 0.85rem;
        font-size: 0.9rem;
        font-weight: 700;
        color: #00BCD4;
    }

    /* center spine */
    .tl-deep-spine {
        width: 28px;
        flex-shrink: 0;
        position: relative;
        display: flex;
        justify-content: center;
    }
    .tl-deep-spine::before {
        content: '';
        position: absolute;
        top: 0;
        bottom: 0;
        width: 3px;
        background: #b2ebf2;
        border-radius: 2px;
    }
    .tl-deep-row:first-child .tl-deep-spine::before { top: 50%; }
    .tl-deep-row:last-child .tl-deep-spine::before  { bottom: 50%; }
    .tl-deep-dot {
        width: 14px;
        height: 14px;
        background: #00BCD4;
        border: 3px solid #ffffff;
        border-radius: 50%;
        box-shadow: 0 0 0 2px #00BCD4;
        position: absolute;
        top: 0.85rem;
        z-index: 1;
    }
    .tl-deep-row.highlight .tl-deep-dot {
        width: 18px;
        height: 18px;
        top: 0.72rem;
        background: #00838F;
        box-shadow: 0 0 0 3px #00838F, 0 0 12px rgba(0,188,212,0.35);
    }

    /* right card */
    .tl-deep-card {
        flex: 1;
        background: #f5f7fa;
        border-radius: 6px;
        padding: 0.8rem 1.1rem;
        margin: 0.3rem 0 0.3rem 0.8rem;
        border-left: 3px solid transparent;
        transition: border-color 0.2s;
    }
    .tl-deep-row.highlight .tl-deep-card {
        background: #f0fafa;
        border-left-color: #00BCD4;
        box-shadow: 0 2px 10px rgba(0,188,212,0.08);
    }
    .tl-deep-card h4 {
        margin: 0 0 0.25rem 0;
        font-size: 1rem;
        font-weight: 600;
        color: #2c3e50;
    }
    .tl-deep-card p {
        margin: 0;
        font-size: 0.92rem;
        color: #5d6d7e;
        line-height: 1.5;
    }
    .tl-deep-card .tl-badge {
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.1rem 0.5rem;
        border-radius: 3px;
        margin-top: 0.35rem;
    }
    .badge-accuracy {
        background: #e8f5e9;
        color: #2e7d32;
    }
    .badge-concept {
        background: #e0f7fa;
        color: #00838F;
    }
    </style>

    <div class="tl-deep fade-in">

        <!-- 1986 -->
        <div class="tl-deep-row">
            <div class="tl-deep-year">1986</div>
            <div class="tl-deep-spine"><div class="tl-deep-dot"></div></div>
            <div class="tl-deep-card">
                <h4>Hinton &amp; Rumelhart — Backpropagation strādā</h4>
                <p>
                    Werbos ideju publicē atkārtoti un pierāda praktiski.
                    Kļūdas signāls izplatās atpakaļ cauri slāņiem —
                    un tīkli sāk mācīties.
                </p>
                <span class="tl-badge badge-concept">pamatideja</span>
            </div>
        </div>

        <!-- 1997 -->
        <div class="tl-deep-row">
            <div class="tl-deep-year">1997</div>
            <div class="tl-deep-spine"><div class="tl-deep-dot"></div></div>
            <div class="tl-deep-card">
                <h4>Hochreiter &amp; Schmidhuber — LSTM</h4>
                <p>
                    Long Short-Term Memory — šūnas, kas spēj atcerēties iepriekšējo
                    kontekstu. Tīkli pirmo reizi iegūst kaut ko līdzīgu atmiņai.
                </p>
                <span class="tl-badge badge-concept">atmiņa tīklos</span>
            </div>
        </div>

        <!-- 2012 -->
        <div class="tl-deep-row highlight">
            <div class="tl-deep-year">2012</div>
            <div class="tl-deep-spine"><div class="tl-deep-dot"></div></div>
            <div class="tl-deep-card">
                <h4>AlexNet — Deep learning uzvar ImageNet</h4>
                <p>
                    Attēlu atpazīšanas sacensībā — kļūdu līmenis nokrīt
                    no ~26% uz ~16%. GPU skaitļošana pierāda, ka dziļie tīkli
                    strādā labāk par jebkuru rokām rakstītu algoritmu.
                </p>
                <span class="tl-badge badge-accuracy">kļūda: 26% → 16%</span>
            </div>
        </div>

        <!-- 2014 -->
        <div class="tl-deep-row">
            <div class="tl-deep-year">2014</div>
            <div class="tl-deep-spine"><div class="tl-deep-dot"></div></div>
            <div class="tl-deep-card">
                <h4>Ian Goodfellow — GAN</h4>
                <p>
                    Ģeneratīvie pretinieku tīkli — divi tīkli sacenšas,
                    un viens no tiem iemācās <em>radīt</em> jaunus datus.
                    Pirmo reizi mašīna nevis klasificē, bet ģenerē.
                </p>
                <span class="tl-badge badge-concept">ģenerēšana</span>
            </div>
        </div>

        <!-- 2017 -->
        <div class="tl-deep-row highlight">
            <div class="tl-deep-year">2017</div>
            <div class="tl-deep-spine"><div class="tl-deep-dot"></div></div>
            <div class="tl-deep-card">
                <h4>Vaswani et al. — "Attention Is All You Need"</h4>
                <p>
                    Transformer arhitektūra — ļauj modelim "skatīties" uz visu
                    tekstu vienlaikus, nevis pa vārdam. Pamats visam, kas notiek
                    pēc tam — BERT, GPT, Claude, tulkošana, kods.
                </p>
                <span class="tl-badge badge-concept">pamats modernai AI</span>
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ── Transformer "attention" mini-diagram ──────────────────────
    st.markdown("""
    <style>
    .attn-diagram {
        background: #f5f7fa;
        border-radius: 8px;
        padding: 1.2rem 1rem;
        margin-top: 1rem;
        text-align: center;
    }
    .attn-diagram .diagram-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #7f8c8d;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.6rem;
    }
    .attn-blocks {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.2rem;
        flex-wrap: wrap;
    }
    .attn-block {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: #ffffff;
        border: 2px solid #00BCD4;
        border-radius: 6px;
        padding: 0.5rem 0.9rem;
        font-size: 0.85rem;
        font-weight: 600;
        color: #2c3e50;
        min-width: 80px;
    }
    .attn-block.core {
        background: #00BCD4;
        color: #ffffff;
        border-color: #00838F;
        transform: scale(1.08);
        box-shadow: 0 2px 12px rgba(0,188,212,0.25);
    }
    .attn-arrow {
        font-size: 1.2rem;
        color: #90a4ae;
        padding: 0 0.15rem;
    }
    </style>

    <div class="attn-diagram fade-in">
        <div class="diagram-label">Transformer — vienkāršota shēma</div>
        <div class="attn-blocks">
            <div class="attn-block">Ievade<br><span style="font-size:0.72rem;font-weight:400;color:#7f8c8d;">Embedding</span></div>
            <span class="attn-arrow">→</span>
            <div class="attn-block core">Attention<br><span style="font-size:0.72rem;font-weight:400;color:#e0f7fa;">Q · K · V</span></div>
            <span class="attn-arrow">→</span>
            <div class="attn-block">Feed-<br>Forward</div>
            <span class="attn-arrow">→</span>
            <div class="attn-block">× N<br><span style="font-size:0.72rem;font-weight:400;color:#7f8c8d;">slāņi</span></div>
            <span class="attn-arrow">→</span>
            <div class="attn-block">Izeja<br><span style="font-size:0.72rem;font-weight:400;color:#7f8c8d;">Tokeni</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="slide-text" style="color:#7f8c8d; margin-top:1.2rem;">
    No 1986. līdz 2017. — trīsdesmit viens gads. Ne revolūcija, bet lēns, nevienmērīgs
    ceļš, kurā idejas bieži apsteidza savu laiku.
    </p>
    """, unsafe_allow_html=True)
