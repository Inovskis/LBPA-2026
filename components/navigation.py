import streamlit as st

TOTAL_SLIDES = 20


def init_navigation():
    """Initialise session-state key for the current slide."""
    if "current_slide" not in st.session_state:
        st.session_state.current_slide = 1


def render_navigation():
    """Render the bottom navigation bar with progress indicator."""
    current = st.session_state.current_slide
    progress_pct = (current / TOTAL_SLIDES) * 100

    # Thin, subtle progress bar + clearly visible slide counter
    st.markdown(
        f"""
        <div class="progress-bar-bg">
            <div class="progress-bar-fill" style="width:{progress_pct:.1f}%"></div>
        </div>
        <div class="slide-counter">{current} / {TOTAL_SLIDES}</div>
        """,
        unsafe_allow_html=True,
    )

    # Prev / Next — large touch-friendly buttons
    col_prev, col_spacer, col_next = st.columns([1, 2, 1])

    with col_prev:
        if current > 1:
            if st.button("\u2190  Atpakaļ", key="nav_prev", use_container_width=True):
                st.session_state.current_slide -= 1
                st.rerun()

    with col_next:
        if current < TOTAL_SLIDES:
            if st.button("Tālāk  \u2192", key="nav_next", use_container_width=True):
                st.session_state.current_slide += 1
                st.rerun()


def slide_header(title, subtitle=None):
    """Render a consistent slide heading with fade-in and cyan border."""
    html = f'<div class="fade-in"><h1 class="slide-title">{title}</h1>'
    if subtitle:
        html += f'<p class="slide-subtitle">{subtitle}</p>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def inject_keyboard_nav():
    """Inject JS for keyboard nav + click-anywhere-to-advance."""
    st.markdown("""
    <script>
    (function() {
        var pd = parent.document;

        // Keyboard navigation
        pd.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
                var btns = pd.querySelectorAll('button');
                for (var i = 0; i < btns.length; i++) {
                    if (btns[i].textContent.includes('Tālāk')) { btns[i].click(); break; }
                }
            }
            if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
                var btns = pd.querySelectorAll('button');
                for (var i = 0; i < btns.length; i++) {
                    if (btns[i].textContent.includes('Atpakaļ')) { btns[i].click(); break; }
                }
            }
        });

        // Click anywhere to advance (skip interactive elements)
        pd.addEventListener('click', function(e) {
            if (e.target.closest('button, a, input, select, textarea, [role="tab"], details, summary, [data-testid="stExpander"], .stCodeBlock, video, img')) {
                return;
            }
            var btns = pd.querySelectorAll('button');
            for (var i = 0; i < btns.length; i++) {
                if (btns[i].textContent.includes('Tālāk')) { btns[i].click(); break; }
            }
        });
    })();
    </script>
    """, unsafe_allow_html=True)
