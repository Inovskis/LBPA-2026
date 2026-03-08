# LBPA 2026 Streamlit Prezentācija — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build an interactive Streamlit slide-based presentation for the LBPA congress about AI and Python in structural engineering design.

**Architecture:** Single-page Streamlit app with session_state-driven slide navigation. Each slide is a Python function in its own module. A shared components layer handles navigation (prev/next buttons + progress bar), custom CSS theming (LBPA + K-forma colors), and media embedding. Assets (images, videos) are stored locally.

**Tech Stack:** Python 3.12, Streamlit, Pillow (for image handling), qrcode (for QR code generation)

**Project directory:** `/home/nauris/Dropbox/Projects/LBPA 2026/`

**Key references:**
- K-forma logo: `/home/nauris/Dropbox/Projects/structural-design-tools/static/images/k-forma-rgb-transparent.png`
- BTF screenshot: `/home/nauris/Dropbox/Projects/LBPA 2026/1734784405264.jpg`
- Existing docs: `/home/nauris/Dropbox/Projects/LBPA 2026/docs/`

---

### Task 1: Project Scaffolding & Dependencies

**Files:**
- Create: `app.py`
- Create: `requirements.txt`
- Create: `slides/__init__.py`
- Create: `components/__init__.py`
- Create: `assets/images/` (directory)
- Create: `assets/videos/` (directory)
- Create: `.streamlit/config.toml`

**Step 1: Create directory structure**

```bash
cd "/home/nauris/Dropbox/Projects/LBPA 2026"
mkdir -p slides components assets/images assets/videos .streamlit
```

**Step 2: Create requirements.txt**

```
streamlit>=1.30
Pillow>=10.0
qrcode>=7.4
```

**Step 3: Install dependencies**

```bash
pip3 install -r requirements.txt
```

**Step 4: Create Streamlit config**

Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#00BCD4"
backgroundColor = "#1a1f2e"
secondaryBackgroundColor = "#32373c"
textColor = "#ffffff"
font = "sans serif"

[server]
headless = true
```

**Step 5: Create minimal app.py that shows a title**

```python
import streamlit as st

st.set_page_config(
    page_title="AI un Python Būvkonstrukciju Projektēšanā",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("LBPA 2026 — Prezentācija")
st.write("Notiek izstrāde...")
```

**Step 6: Create empty __init__.py files**

Create `slides/__init__.py` and `components/__init__.py` as empty files.

**Step 7: Run app to verify it starts**

```bash
cd "/home/nauris/Dropbox/Projects/LBPA 2026" && streamlit run app.py --server.port 8501
```
Expected: Browser opens with "LBPA 2026 — Prezentācija" title on dark background.

---

### Task 2: Navigation Component & Slide Framework

**Files:**
- Create: `components/navigation.py`
- Create: `components/styling.py`
- Modify: `app.py`

**Step 1: Create components/styling.py — CSS theme**

```python
import streamlit as st


def apply_theme():
    """Inject custom CSS for presentation mode."""
    st.markdown("""
    <style>
    /* Hide Streamlit chrome for presentation */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Slide container */
    .slide-container {
        max-width: 1100px;
        margin: 0 auto;
        padding: 2rem 3rem;
        min-height: 70vh;
    }

    /* Typography */
    .slide-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1.5rem;
        border-bottom: 4px solid #00BCD4;
        padding-bottom: 0.5rem;
    }

    .slide-subtitle {
        font-size: 1.6rem;
        color: #b0bec5;
        margin-bottom: 1rem;
    }

    .slide-text {
        font-size: 1.2rem;
        line-height: 1.8;
        color: #e0e0e0;
    }

    /* Accent elements */
    .accent-box {
        background: linear-gradient(135deg, #00BCD4 0%, #0097A7 100%);
        border-radius: 12px;
        padding: 1.5rem 2rem;
        color: #ffffff;
        margin: 1rem 0;
        font-size: 1.1rem;
    }

    .stat-card {
        background: #32373c;
        border-left: 4px solid #00BCD4;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin: 0.5rem 0;
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #00BCD4;
    }

    .stat-label {
        font-size: 1rem;
        color: #b0bec5;
    }

    /* Navigation */
    .nav-container {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #151a28;
        padding: 0.8rem 2rem;
        z-index: 999;
        border-top: 1px solid #32373c;
    }

    .progress-bar-bg {
        background: #32373c;
        border-radius: 4px;
        height: 6px;
        width: 100%;
        margin-bottom: 0.5rem;
    }

    .progress-bar-fill {
        background: linear-gradient(90deg, #00BCD4, #0097A7);
        border-radius: 4px;
        height: 6px;
        transition: width 0.3s ease;
    }

    /* Code blocks */
    .stCodeBlock {
        border: 1px solid #00BCD4;
        border-radius: 8px;
    }

    /* Comparison columns */
    .compare-old {
        background: #3e2723;
        border-radius: 8px;
        padding: 1rem;
        border-left: 4px solid #ef5350;
    }

    .compare-new {
        background: #1b5e20;
        border-radius: 8px;
        padding: 1rem;
        border-left: 4px solid #66bb6a;
    }

    /* Fade in animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .fade-in {
        animation: fadeIn 0.6s ease-out;
    }

    /* Bottom padding for nav bar */
    .block-container {
        padding-bottom: 100px !important;
    }
    </style>
    """, unsafe_allow_html=True)
```

**Step 2: Create components/navigation.py**

```python
import streamlit as st

TOTAL_SLIDES = 17


def init_navigation():
    """Initialize session state for slide navigation."""
    if "current_slide" not in st.session_state:
        st.session_state.current_slide = 1


def render_navigation():
    """Render progress bar and prev/next buttons at the bottom."""
    slide = st.session_state.current_slide
    progress = slide / TOTAL_SLIDES

    # Progress bar
    st.markdown(f"""
    <div class="progress-bar-bg">
        <div class="progress-bar-fill" style="width: {progress * 100:.0f}%;"></div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation buttons
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if slide > 1:
            if st.button("◀ Iepriekšējais", key="prev", use_container_width=True):
                st.session_state.current_slide -= 1
                st.rerun()

    with col2:
        st.markdown(
            f"<p style='text-align:center; color:#b0bec5; margin:0;'>"
            f"{slide} / {TOTAL_SLIDES}</p>",
            unsafe_allow_html=True,
        )

    with col3:
        if slide < TOTAL_SLIDES:
            if st.button("Nākamais ▶", key="next", use_container_width=True):
                st.session_state.current_slide += 1
                st.rerun()


def slide_header(title: str, subtitle: str = ""):
    """Render a consistent slide header."""
    st.markdown(f'<div class="fade-in">', unsafe_allow_html=True)
    st.markdown(f'<h1 class="slide-title">{title}</h1>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(
            f'<p class="slide-subtitle">{subtitle}</p>', unsafe_allow_html=True
        )
```

**Step 3: Update app.py — wire up navigation**

```python
import streamlit as st
from components.styling import apply_theme
from components.navigation import init_navigation, render_navigation, TOTAL_SLIDES

st.set_page_config(
    page_title="AI un Python Būvkonstrukciju Projektēšanā",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_theme()
init_navigation()

# Import all slide functions
from slides import get_slide

# Render current slide
slide_fn = get_slide(st.session_state.current_slide)
slide_fn()

# Render navigation
render_navigation()
```

**Step 4: Create slides/__init__.py with registry**

```python
def get_slide(number: int):
    """Return the render function for a given slide number."""
    from slides.slide_01_title import render as s01
    from slides.slide_02_new_era import render as s02
    from slides.slide_03_problem import render as s03
    from slides.slide_04_solution import render as s04
    from slides.slide_05_demo import render as s05
    from slides.slide_06_why_python import render as s06
    from slides.slide_07_libraries import render as s07
    from slides.slide_08_ai_assistant import render as s08
    from slides.slide_09_ai_examples import render as s09
    from slides.slide_10_prediction import render as s10
    from slides.slide_11_ralph_wiggum import render as s11
    from slides.slide_12_deployment import render as s12
    from slides.slide_13_other_tools import render as s13
    from slides.slide_14_pyrevit import render as s14
    from slides.slide_15_podcasts import render as s15
    from slides.slide_16_universities import render as s16
    from slides.slide_17_summary import render as s17

    slides = {
        1: s01, 2: s02, 3: s03, 4: s04, 5: s05,
        6: s06, 7: s07, 8: s08, 9: s09, 10: s10,
        11: s11, 12: s12, 13: s13, 14: s14, 15: s15,
        16: s16, 17: s17,
    }
    return slides.get(number, s01)
```

**Step 5: Create a placeholder slide to test navigation**

Create `slides/slide_01_title.py`:
```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("AI un Python Būvkonstrukciju Projektēšanā")
    st.write("Placeholder — titulslaids")
```

Create placeholder files for slides 2-17 following the same pattern with unique placeholder text.

**Step 6: Run and verify navigation works**

```bash
cd "/home/nauris/Dropbox/Projects/LBPA 2026" && streamlit run app.py
```
Expected: Dark-themed app with slide 1 visible, progress bar at top, Next button works, slide counter shows "1 / 17".

---

### Task 3: Copy Assets & Logo Files

**Files:**
- Copy: K-forma logo → `assets/images/kforma_logo.png`
- Copy: BTF screenshot → `assets/images/btf_screenshot.jpg`
- Create: `components/media.py`

**Step 1: Copy assets**

```bash
cd "/home/nauris/Dropbox/Projects/LBPA 2026"
cp "/home/nauris/Dropbox/Projects/structural-design-tools/static/images/k-forma-rgb-transparent.png" assets/images/kforma_logo.png
cp "1734784405264.jpg" assets/images/btf_screenshot.jpg
```

**Step 2: Fetch LBPA logo from website (or create placeholder)**

```bash
# Try to download LBPA logo
curl -sL "https://lbpa.lv/wp-content/uploads/2021/01/lbpa_logo.svg" -o assets/images/lbpa_logo.svg 2>/dev/null || echo "Will use text placeholder"
```

If logo is not downloadable, create a text-based logo in the slide.

**Step 3: Create components/media.py — helper for images and media**

```python
import streamlit as st
import base64
from pathlib import Path

ASSETS_DIR = Path(__file__).parent.parent / "assets"


def show_image(filename: str, caption: str = "", width: int = None):
    """Display an image from assets/images/."""
    path = ASSETS_DIR / "images" / filename
    if path.exists():
        st.image(str(path), caption=caption, width=width)
    else:
        st.warning(f"Attēls nav atrasts: {filename}")


def show_video(filename: str):
    """Display a video from assets/videos/."""
    path = ASSETS_DIR / "videos" / filename
    if path.exists():
        st.video(str(path))
    else:
        st.info(f"Video vēl nav pievienots: {filename}")


def image_to_base64(filename: str) -> str:
    """Convert image to base64 for HTML embedding."""
    path = ASSETS_DIR / "images" / filename
    if path.exists():
        data = path.read_bytes()
        return base64.b64encode(data).decode()
    return ""


def logo_header():
    """Render logos side by side."""
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        show_image("kforma_logo.png", width=120)
    with col3:
        lbpa_path = ASSETS_DIR / "images" / "lbpa_logo.svg"
        if lbpa_path.exists():
            st.image(str(lbpa_path), width=120)
        else:
            st.markdown(
                '<p style="font-size:1.5rem; font-weight:700; color:#ffffff;">'
                "LBPA</p>",
                unsafe_allow_html=True,
            )
```

**Step 4: Verify assets are in place**

```bash
ls -la "/home/nauris/Dropbox/Projects/LBPA 2026/assets/images/"
```
Expected: `kforma_logo.png`, `btf_screenshot.jpg`, possibly `lbpa_logo.svg`.

---

### Task 4: Slides 1-4 (Title, New Era, Problem, Solution)

**Files:**
- Modify: `slides/slide_01_title.py`
- Modify: `slides/slide_02_new_era.py`
- Modify: `slides/slide_03_problem.py`
- Modify: `slides/slide_04_solution.py`

**Step 1: Slide 1 — Title**

```python
import streamlit as st
from components.media import logo_header


def render():
    logo_header()

    st.markdown("""
    <div style="text-align:center; margin-top:3rem;" class="fade-in">
        <h1 style="font-size:3.2rem; font-weight:700; color:#ffffff; margin-bottom:0.5rem;">
            AI un Python
        </h1>
        <h1 style="font-size:3.2rem; font-weight:700; color:#00BCD4; margin-bottom:2rem;">
            Būvkonstrukciju Projektēšanā
        </h1>
        <p style="font-size:1.4rem; color:#b0bec5;">
            Nauris — KFORMA SIA
        </p>
        <p style="font-size:1.1rem; color:#78909c;">
            LBPA Kongress 2026
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-top:4rem;">
        <p style="font-size:1rem; color:#546e7a;">
            design.kforma.lv
        </p>
    </div>
    """, unsafe_allow_html=True)
```

**Step 2: Slide 2 — Jaunā Ēra**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Jaunā Ēra", "Indivīds var radīt to, kam agrāk vajadzēja veselu komandu")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="compare-old">
            <h3 style="color:#ef5350;">⏮ Agrāk</h3>
            <ul class="slide-text">
                <li>Lielas programmētāju komandas</li>
                <li>Milzīgi budžeti</li>
                <li>Gadi izstrādē</li>
                <li>Dārgas licences</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="compare-new">
            <h3 style="color:#66bb6a;">▶ Tagad</h3>
            <ul class="slide-text">
                <li>Viens inženieris + AI</li>
                <li>Bezmaksas rīki</li>
                <li>Nedēļas, ne gadi</li>
                <li>Open-source bibliotēkas</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="accent-box" style="text-align:center; margin-top:2rem;">
        <p style="font-size:1.4rem; margin:0;">
            <strong>design.kforma.lv</strong> — 31 modulis, ~148,000 koda rindas<br>
            Izstrādāts viena inženiera spēkiem ar AI palīdzību
        </p>
    </div>
    """, unsafe_allow_html=True)
```

**Step 3: Slide 3 — Problēma**

```python
import streamlit as st
from components.navigation import slide_header
from components.media import show_image


def render():
    slide_header("Problēma", "Tradicionālo rīku ierobežojumi")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        <div class="stat-card">
            <h4 style="color:#ef5350;">📊 Excel</h4>
            <p class="slide-text">Grūti izsekot formulas • Nav versiju kontroles • Kļūdas kopējot</p>
        </div>
        <div class="stat-card">
            <h4 style="color:#ef5350;">🔒 MathCAD</h4>
            <p class="slide-text">Dārga licence • Ierobežotas vizualizācijas • Nav web pieejamības</p>
        </div>
        <div class="stat-card">
            <h4 style="color:#ef5350;">📦 Komerciālā programmatūra</h4>
            <p class="slide-text">"Black box" aprēķini • Augsta cena • Nav pielāgojama</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        show_image("btf_screenshot.jpg", caption="BTF Digital — tipisks komerciāls rīks")
```

**Step 4: Slide 4 — Risinājums**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Risinājums", "design.kforma.lv — atvērta web platforma")

    # Stats row
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="stat-card"><p class="stat-number">31</p>'
                     '<p class="stat-label">Aprēķinu moduļi</p></div>',
                     unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><p class="stat-number">148K</p>'
                     '<p class="stat-label">Koda rindas</p></div>',
                     unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><p class="stat-number">5</p>'
                     '<p class="stat-label">Eirokodeksi</p></div>',
                     unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="stat-card"><p class="stat-number">0€</p>'
                     '<p class="stat-label">Cena lietotājam</p></div>',
                     unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Atbalstītie standarti:**
        - EN 1992 (Dzelzbetona konstrukcijas) + LV NA
        - EN 1993 (Tērauda konstrukcijas)
        - EN 1995 (Koka konstrukcijas)
        - EN 1997 (Ģeotehnika)
        - EN 1991 (Slodzes) + LV NA
        """)
    with col2:
        st.markdown("""
        **Platformas priekšrocības:**
        - Web-bāzēta — pieejama jebkurā ierīcē
        - Atvērts kods — pārredzamas formulas
        - Validēta pret standartiem
        - Regulāri atjauninājumi
        """)
```

**Step 5: Run and verify slides 1-4**

```bash
cd "/home/nauris/Dropbox/Projects/LBPA 2026" && streamlit run app.py
```
Expected: Navigate through slides 1-4, check styling, logos, BTF image, stat cards render correctly.

---

### Task 5: Slide 5 — Demo (Labākie moduļi)

**Files:**
- Modify: `slides/slide_05_demo.py`

**Step 1: Write slide with tabs for each module**

```python
import streamlit as st
from components.navigation import slide_header
from components.media import show_image, show_video


def render():
    slide_header("Demo", "Platformas labākie moduļi")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🏗️ KF3D FEM",
        "🔩 Pāļi (CPT)",
        "📐 Liece",
        "⬡ Caurspiešana"
    ])

    with tab1:
        st.markdown("""
        <div class="stat-card">
            <h4>KF3D — 3D Strukturālā Analīze</h4>
            <p class="slide-text">
            11,000+ koda rindas • Three.js 3D vizualizācija • PyNite FEM backend<br>
            Mezgli, stieņi, čaulas, balsti, slodzes — pilna 3D analīze pārlūkā
            </p>
        </div>
        """, unsafe_allow_html=True)
        show_video("demo_kf3d.mp4")  # Placeholder — video jāpievieno
        show_image("demo_kf3d.png", caption="KF3D FEM modulis")

    with tab2:
        st.markdown("""
        <div class="stat-card">
            <h4>Pāļu Projektēšana (CPT)</h4>
            <p class="slide-text">
            2,789 koda rindas • CPT datu analīze • Vairāku profilu salīdzinājums<br>
            Aksiālā nestspēja no CPT datiem ar detalizētu vizualizāciju
            </p>
        </div>
        """, unsafe_allow_html=True)
        show_video("demo_pile.mp4")
        show_image("demo_pile.png", caption="Pāļu CPT modulis")

    with tab3:
        st.markdown("""
        <div class="stat-card">
            <h4>Lieces Aprēķins</h4>
            <p class="slide-text">
            1,953 koda rindas • EC2 / GEM / Mander betona modeļi<br>
            M-N diagrammas, plaisu kontrole, deformācijas
            </p>
        </div>
        """, unsafe_allow_html=True)
        show_video("demo_bending.mp4")
        show_image("demo_bending.png", caption="Lieces modulis")

    with tab4:
        st.markdown("""
        <div class="stat-card">
            <h4>Caurspiešanas Aprēķins</h4>
            <p class="slide-text">
            Interaktīvs SVG plānskats • EC2 un MC2010 salīdzinājums<br>
            Automātiska kritiskā perimetra vizualizācija
            </p>
        </div>
        """, unsafe_allow_html=True)
        show_video("demo_punching.mp4")
        show_image("demo_punching.png", caption="Caurspiešanas modulis")

    st.info("💡 Video ieraksti — ja nav pievienoti, sagatavot ekrāna ierakstus no design.kforma.lv")
```

**Step 2: Run and verify tab navigation works**

Expected: 4 tabs, each with placeholder content. Videos show "not found" info until recorded.

---

### Task 6: Slides 6-7 (Python, Libraries)

**Files:**
- Modify: `slides/slide_06_why_python.py`
- Modify: `slides/slide_07_libraries.py`

**Step 1: Slide 6 — Kāpēc Python**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Kāpēc Python?", "Inženieru izvēle Nr. 1")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Bezmaksas un atvērts
        - Nav licences maksu
        - Liela kopiena (>10M izstrādātāju)

        ### Bagāta bibliotēku ekosistēma
        - 500,000+ pakotnes PyPI
        - Specializētas inženieru bibliotēkas

        ### Lasāms kods
        - Kods lasa kā formula
        - Viegli auditējams
        """)

    with col2:
        st.markdown("### EC2 formula Python kodā:")
        st.code("""
# EC2 §6.2.2 — Bīdes izturība bez šķērsstiegrojuma
import math

k = min(1 + math.sqrt(200 / d), 2.0)
rho_l = min(As / (b * d), 0.02)

v_Rd_c = (0.18 / gamma_c) * k * (100 * rho_l * fck) ** (1/3) * b * d

# Rezultāts uzreiz saprotams!
        """, language="python")

        st.markdown("""
        <div class="accent-box">
            Kods = Dokumentācija = Aprēķins
        </div>
        """, unsafe_allow_html=True)
```

**Step 2: Slide 7 — Python bibliotēkas**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Python Bibliotēkas", "Specializēti rīki konstrukcijām")

    libs = [
        ("structuralcodes", "Validētas Eirokodeksu formulas",
         "from structuralcodes.codes.ec2_2004 import v_rdc_punching\nresult = v_rdc_punching(d_eff=200, f_ck=30, rho_l=0.015, gamma_c=1.5)"),
        ("concreteproperties", "Dzelzsbetona šķērsgriezumu analīze, M-N diagrammas",
         "from concreteproperties.material import Concrete, SteelBar\nanalysis = ConcreteAnalysis(section)\ndiagram = analysis.moment_interaction_diagram()"),
        ("sectionproperties", "Ģeometriskās īpašības jebkuram šķērsgriezumam",
         "from sectionproperties.pre.geometry import Geometry\nsection = Section(geometry)\nsection.calculate_geometric_properties()"),
        ("scikit-fem + gmsh", "FEM analīze — režģi un risinātājs",
         "import gmsh\nfrom skfem import *\nmesh = MeshTri.load('model.msh')\nK = stiffness.assemble(basis)\nu = solve(K, f)"),
        ("PyNite", "3D frame/shell analīze",
         "from PyNite import FEModel3D\nmodel = FEModel3D()\nmodel.add_node('N1', 0, 0, 0)\nmodel.analyze()"),
    ]

    for name, desc, code in libs:
        with st.expander(f"📦 **{name}** — {desc}", expanded=False):
            st.code(code, language="python")

    st.markdown("""
    <div class="accent-box" style="text-align:center;">
        Visas bibliotēkas ir <strong>bezmaksas</strong> un <strong>open-source</strong>!
    </div>
    """, unsafe_allow_html=True)
```

**Step 3: Run and verify**

Expected: Slide 6 shows two-column layout with code. Slide 7 shows expandable library cards.

---

### Task 7: Slides 8-10 (AI Assistant, Examples, Prediction vs Determinism)

**Files:**
- Modify: `slides/slide_08_ai_assistant.py`
- Modify: `slides/slide_09_ai_examples.py`
- Modify: `slides/slide_10_prediction.py`

**Step 1: Slide 8 — AI kā izstrādes palīgs**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("AI Kā Izstrādes Palīgs", "Claude Code uz atsevišķas Linux mašīnas")

    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown("""
        ### Kas tas ir?

        **Claude Code** — AI asistents komandrindā:
        - Lasa un raksta kodu
        - Izpilda komandas
        - Saprot projekta kontekstu
        - Meklē dokumentāciju

        ### Kāpēc atsevišķa Linux mašīna?
        - Izolēta vide
        - Nepārtraukta pieejamība
        - Paralēla izstrāde
        """)

    with col2:
        st.markdown("### Tipiska sesija:")
        st.code("""
$ claude

> Pievieno SVG vizualizāciju caurspiešanas modulim
  ar kolonnas skatu no augšas un kritisko perimetru

Claude: Es izveidošu vizualizācijas sistēmu ar trim
        komponentiem: PunchingViz, SectionViz,
        PunchingResultsViz...

        [Izveido ~400 rindas JavaScript]
        [Testē ar reāliem datiem]
        [Labo layout problēmas]

Rezultāts: Pilna funkcionalitāte 30 minūtēs
        """, language="text")
```

**Step 2: Slide 9 — AI piemēri**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("AI Piemēri", "Reāli gadījumi no design.kforma.lv izstrādes")

    # Time savings table
    st.markdown("""
    | Uzdevums | Bez AI | Ar AI | Ietaupījums |
    |----------|--------|-------|-------------|
    | SVG vizualizācija | 4-6 h | 30 min | **~10x** |
    | MC2010 integrācija | 2-3 h | 20 min | **~8x** |
    | Railway deployment fix | 1-2 h | 15 min | **~6x** |
    | Jauna funkcionalitāte | 2-4 h | 45 min | **~4x** |
    """)

    tab1, tab2, tab3 = st.tabs(["🎨 SVG Izveide", "🐛 Kļūdu Diagnostika", "🚀 Deployment"])

    with tab1:
        st.markdown("""
        **Uzdevums:** Interaktīvs caurspiešanas plānskats ar kolonnu un kritisko perimetru

        **AI izveidoja:** 3 JavaScript objektus (~400 rindas), interaktīva vizualizācija kas atjaunojas reāllaikā

        **Laiks:** 30 minūtes (tradicionāli 4-6 stundas)
        """)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.error("MC2010 v_Rd,c = 271,562 MPa ???")
            st.caption("Jābūt ~0.5-1.5 MPa")
        with col2:
            st.success("AI diagnostika: Funkcija atgriež SPĒKU (N), nevis SPRIEGUMU (MPa)")
            st.code("# Risinājums:\nv_rdc = k_psi * sqrt(fck) / gamma_c  # MPa", language="python")

    with tab3:
        st.markdown("""
        **Problēma:** "Bad Gateway" pēc Railway redeploy

        **AI atklājums:** Hardkodēts ports `app.run(port=5000)`
        """)
        st.code("# Fix (2 rindas):\nport = int(os.environ.get('PORT', 5000))\napp.run(port=port, host='0.0.0.0')", language="python")

    st.markdown("""
    <div class="accent-box" style="text-align:center;">
        Vidēji <strong>~5x ātrāk</strong> ar AI palīdzību
    </div>
    """, unsafe_allow_html=True)
```

**Step 3: Slide 10 — AI prediction vs determinisms**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("AI Prognozes vs Determinisms",
                 "Kāpēc AI nevar aizstāt inženieri, bet var palīdzēt")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="compare-old">
            <h3 style="color:#ef5350;">⚠ AI (LLM) Prognozes</h3>
            <ul class="slide-text">
                <li>Statistiski modeļi — <strong>var kļūdīties</strong></li>
                <li>Halucinācijas — izdomā formulas</li>
                <li>Nav garantijas par pareizību</li>
                <li>Atkarīgi no apmācības datiem</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="compare-new">
            <h3 style="color:#66bb6a;">✓ Python Bibliotēkas</h3>
            <ul class="slide-text">
                <li><strong>Determinēts</strong> rezultāts</li>
                <li>Validētas pret standartiem</li>
                <li>Vienāda ievade = vienāds rezultāts</li>
                <li>Atvērtā pirmkods — auditējams</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="accent-box">
        <p style="font-size:1.3rem; margin:0; text-align:center;">
            <strong>AI raksta kodu</strong> → <strong>Python bibliotēkas nodrošina pareizību</strong> → <strong>Inženieris verificē</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Piemērs:** AI palīdz uzrakstīt `structuralcodes` izsaukumu, bet formula pati nāk no
    validētas bibliotēkas — rezultāts vienmēr ir determinēts un pareizs.
    """)
```

**Step 4: Run and verify slides 8-10**

Expected: AI slides render with tabs, comparison columns, code blocks.

---

### Task 8: Slide 11 — Ralph Wiggum Metode

**Files:**
- Modify: `slides/slide_11_ralph_wiggum.py`

**Step 1: Write slide with animated loop visualization**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Ralph Wiggum Metode",
                 "Iteratīvā AI cilpa — reverse engineering")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        ### Kā tas darbojas?

        **Geoffrey Huntley** (2025) izveidoja 5 rindu Bash skriptu:
        """)

        st.code("""
while true; do
    claude --prompt "Build program X" \\
           --context "$(cat output.log)" \\
           | tee output.log
done
        """, language="bash")

        st.markdown("""
        ### Princips
        1. AI ģenerē kodu
        2. Kods tiek izpildīts
        3. Kļūdas un rezultāti atgriežas AI
        4. AI labo un uzlabo
        5. **Atkārto līdz darbojas!**

        ### Rezultāts
        - Komerciālas programmatūras klonēšana
        - Piemērs: grāmatvedības programma rekonstruēta pilnībā
        - Claude Code plugin pieejams oficiāli
        """)

    with col2:
        # ASCII art loop diagram
        st.markdown("""
        <div style="background:#1a1f2e; border:2px solid #00BCD4; border-radius:12px;
                    padding:2rem; text-align:center;">
            <p style="font-size:1.2rem; color:#00BCD4;">🔄 CILPA</p>
            <p style="color:#fff;">↓</p>
            <div style="background:#32373c; padding:0.8rem; border-radius:8px; margin:0.5rem 0;">
                <p style="color:#66bb6a; margin:0;">AI ģenerē kodu</p>
            </div>
            <p style="color:#fff;">↓</p>
            <div style="background:#32373c; padding:0.8rem; border-radius:8px; margin:0.5rem 0;">
                <p style="color:#ef5350; margin:0;">Kļūdas / rezultāti</p>
            </div>
            <p style="color:#fff;">↓</p>
            <div style="background:#32373c; padding:0.8rem; border-radius:8px; margin:0.5rem 0;">
                <p style="color:#ffb74d; margin:0;">Atgriež AI kā kontekstu</p>
            </div>
            <p style="color:#fff;">↓</p>
            <div style="background:#32373c; padding:0.8rem; border-radius:8px; margin:0.5rem 0;">
                <p style="color:#00BCD4; margin:0;">Atkārto līdz ✓</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    > *"Kontekstuālais spiediena katls" — katrs cikls pievieno zināšanas
    > līdz AI saprot visu sistēmu.*
    """)
```

**Step 2: Run and verify the loop diagram renders**

---

### Task 9: Slides 12-14 (Deployment, Other Tools, PyRevit)

**Files:**
- Modify: `slides/slide_12_deployment.py`
- Modify: `slides/slide_13_other_tools.py`
- Modify: `slides/slide_14_pyrevit.py`

**Step 1: Slide 12 — Deployment resursi**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Deployment Resursi", "No koda līdz produkcijai")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="stat-card" style="text-align:center;">
            <p style="font-size:2rem;">🚂</p>
            <h4 style="color:#00BCD4;">Railway</h4>
            <p class="slide-text" style="font-size:0.9rem;">
            Cloud hosting<br>Auto-deploy no GitHub<br>PostgreSQL iekļauts<br>
            <strong>design.kforma.lv</strong> darbojas šeit
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stat-card" style="text-align:center;">
            <p style="font-size:2rem;">🐙</p>
            <h4 style="color:#00BCD4;">GitHub</h4>
            <p class="slide-text" style="font-size:0.9rem;">
            Versiju kontrole<br>Sadarbības platforma<br>CI/CD pipelines<br>
            Bezmaksas privātie repo
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="stat-card" style="text-align:center;">
            <p style="font-size:2rem;">🎈</p>
            <h4 style="color:#00BCD4;">Streamlit</h4>
            <p class="slide-text" style="font-size:0.9rem;">
            Python → Web app<br>Bezmaksas hosting<br>
            <strong>Šī prezentācija</strong><br>ir Streamlit app!
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="stat-card" style="text-align:center;">
            <p style="font-size:2rem;">🐳</p>
            <h4 style="color:#00BCD4;">Docker</h4>
            <p class="slide-text" style="font-size:0.9rem;">
            Reproducējama vide<br>Viena komanda deploy<br>Izolēta sistēma
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### design.kforma.lv deployment plūsma:")
    st.code("""
git push origin main          # 1. Push kodu
# Railway automātiski:
#   2. Build Docker image
#   3. Deploy jaunas versijas
#   4. Cloudflare nodrošina SSL
# Gatavs ~2 minūtēs!
    """, language="bash")
```

**Step 2: Slide 13 — Citi labi rīki**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Citi Labi Rīki", "Ekosistēma inženieriem")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🔧 Viktor.AI",
        "🌳 CalcTree",
        "📝 Calcpad",
        "🤖 GPAI"
    ])

    with tab1:
        st.markdown("""
        ### Viktor.AI — Low-Code Inženieru Platforma
        - Veido web apps ar dažām Python rindām
        - Integrējas ar SAP2000, ETABS, Excel
        - 2026 roadmap: AI agents + automatizētas darbplūsmas
        - **viktor.ai**
        """)

    with tab2:
        st.markdown("""
        ### CalcTree — Cloud Aprēķinu Platforma
        - Python & MathJS dzinējs
        - Integrējas ar Excel, Grasshopper, ETABS
        - €2.3M investīcijas (Foundamental VC)
        - Lietotāji: Arup, Jacobs, WSP
        - **calctree.com**
        """)

    with tab3:
        st.markdown("""
        ### Calcpad — Bezmaksas Open-Source
        - Programmējams kalkulators inženieriem
        - 100+ Eirokodeksu šablonu
        - HTML atskaites ar formulām
        - Nav nepieciešamas programmēšanas prasmes
        - **calcpad.eu**
        """)

    with tab4:
        st.markdown("""
        ### GPAI — AI STEM Solver
        - Foto/PDF → risinājums ar vizualizāciju
        - Triple-verified (GPT-5, Gemini, Deepseek)
        - Soli-pa-solim skaidrojumi
        - **gpai.app**
        """)

        st.markdown("### Piemērs — vienkāršs prompts:")
        st.code("""
Prompt: "Calculate the bending capacity of a
        300x600mm RC beam, C30/37, 4Ø25 bottom"

GPAI: Provides step-by-step EC2 solution with
      diagrams and verification
        """, language="text")
```

**Step 3: Slide 14 — PyRevit**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("PyRevit", "Revit Add-ins ar Python")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Kas ir PyRevit?
        - **Bezmaksas** open-source Revit add-in
        - Python skripti — **bez Visual Studio**
        - Automatizē atkārtojošos uzdevumus
        - Pilna Revit API pieejamība

        ### Piemēri
        - Batch šķērsgriezumu maiņa
        - Automātiska stiegrojuma marķēšana
        - Excel → Revit datu imports
        - Parametru masu atjaunināšana

        ### Barjera
        """)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="compare-old" style="padding:0.5rem;">
                <p style="margin:0;"><strong>C# Add-in:</strong><br>Visual Studio, .NET, kompilēšana</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="compare-new" style="padding:0.5rem;">
                <p style="margin:0;"><strong>PyRevit:</strong><br>Teksta redaktors + Python</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.code("""
# PyRevit skripts — eksportē elementu datus
from pyrevit import revit, DB

doc = revit.doc
collector = DB.FilteredElementCollector(doc)
beams = collector.OfCategory(
    DB.BuiltInCategory.OST_StructuralFraming
).WhereElementIsNotElementType()

for beam in beams:
    mark = beam.get_Parameter(
        DB.BuiltInParameter.ALL_MODEL_MARK
    ).AsString()
    length = beam.get_Parameter(
        DB.BuiltInParameter.INSTANCE_LENGTH
    ).AsDouble() * 304.8  # feet → mm

    print(f"{mark}: {length:.0f} mm")
        """, language="python")

        st.caption("docs.pyrevitlabs.io")
```

**Step 4: Run and verify slides 12-14**

---

### Task 10: Slides 15-17 (Podcasts, Universities, Summary)

**Files:**
- Modify: `slides/slide_15_podcasts.py`
- Modify: `slides/slide_16_universities.py`
- Modify: `slides/slide_17_summary.py`

**Step 1: Slide 15 — Podkāsti un resursi**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Podkāsti un Resursi", "Kur mācīties tālāk")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🎙️ Flocode Podcast
        **James O'Reilly** — Python + Inženierija

        Ieteicamās epizodes:
        - **#058** Morten Engen — *Structuralcodes* bibliotēka
        - **#042** Craig Brinck — *PyNite* FEM analīze
        - **#048** Connor Ferster — Automatizācija
        - **#039** Dr. MZ Naser — ML konstrukcijās

        📍 flocode.substack.com
        """)

    with col2:
        st.markdown("""
        ### 📚 Mācību Resursi

        | Resurss | Apraksts |
        |---------|----------|
        | **StructuralPython** | structuralpython.com |
        | **EngineeringSkills** | engineeringskills.com |
        | **civils.ai** | Python kurss inženieriem |
        | **Udemy** | Programming for Structural Engineers |

        ### 📖 Zinātniskie raksti
        - Gustafsson & McBain (2020) — *scikit-fem* (JOSS)
        """)
```

**Step 2: Slide 16 — Universitātes**

```python
import streamlit as st
from components.navigation import slide_header


def render():
    slide_header("Universitātes", "Python inženieru izglītībā")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🌍 Pasaulē

        <div class="stat-card">
            <h4 style="color:#00BCD4;">🇳🇴 NTNU (Norvēģija)</h4>
            <p class="slide-text">
            Kurss <strong>"Python for Structural Engineering"</strong> (KT6198)<br>
            2026. gada pavasaris — pirmais gadagājums<br>
            Tēmas: drošums, optimizācija, ML, dinamika
            </p>
        </div>

        <div class="stat-card">
            <h4 style="color:#00BCD4;">🇺🇸 Cal Poly (ASV)</h4>
            <p class="slide-text">
            Architectural Engineering Computing<br>
            Python manuālis studentiem
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        ### 🇱🇻 Latvijā

        <div class="accent-box">
            <h4 style="margin-top:0;">Ko darīt?</h4>
            <ul>
                <li>Integrēt Python RTU/LLU inženieru programmās</li>
                <li>Izveidot specializētu kursu (pēc NTNU parauga)</li>
                <li>Semināri praktizējošiem inženieriem</li>
                <li>LBPA kā iniciatīvas virzītājs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        > *Ja Norvēģija var — mēs arī varam.*
        """)
```

**Step 3: Slide 17 — Kopsavilkums + QR kods**

```python
import streamlit as st
from components.navigation import slide_header
from components.media import show_image

try:
    import qrcode
    from io import BytesIO
    HAS_QRCODE = True
except ImportError:
    HAS_QRCODE = False


def render():
    slide_header("Kopsavilkums")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="stat-card" style="text-align:center; min-height:200px;">
            <p style="font-size:2.5rem;">🐍</p>
            <h4 style="color:#00BCD4;">Python</h4>
            <p class="slide-text">Spēcīgs bezmaksas rīks inženieriem ar validētām bibliotēkām</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stat-card" style="text-align:center; min-height:200px;">
            <p style="font-size:2.5rem;">🤖</p>
            <h4 style="color:#00BCD4;">AI</h4>
            <p class="slide-text">Paātrina izstrādi ~5x, bet vienmēr jāverificē rezultāts</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="stat-card" style="text-align:center; min-height:200px;">
            <p style="font-size:2.5rem;">🚀</p>
            <h4 style="color:#00BCD4;">Jaunā Ēra</h4>
            <p class="slide-text">Katrs indivīds var radīt profesionālus rīkus</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="accent-box">
            <h3 style="margin-top:0;">Izmēģini pats!</h3>
            <p style="font-size:1.4rem;">
                <strong>design.kforma.lv</strong><br>
                Bezmaksas reģistrācija • 31 aprēķinu modulis
            </p>
            <p style="font-size:1rem; margin-bottom:0;">
                📧 nauris@kforma.lv
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Jautājumi?")

    with col2:
        # Generate QR code
        if HAS_QRCODE:
            qr = qrcode.make("https://design.kforma.lv")
            buf = BytesIO()
            qr.save(buf, format="PNG")
            st.image(buf.getvalue(), caption="design.kforma.lv", width=200)
        else:
            st.info("QR kods: design.kforma.lv")

    show_image("kforma_logo.png", width=150)
```

**Step 4: Run and verify all 17 slides**

```bash
cd "/home/nauris/Dropbox/Projects/LBPA 2026" && streamlit run app.py
```
Expected: Full slide deck navigable with prev/next, consistent theming, QR code on last slide.

---

### Task 11: Final Polish — Keyboard Navigation & Presenter Notes

**Files:**
- Modify: `components/navigation.py` — add keyboard support via JS injection
- Modify: `app.py` — add sidebar presenter notes

**Step 1: Add keyboard arrow navigation**

In `components/navigation.py`, add a function:

```python
def inject_keyboard_nav():
    """Inject JavaScript for arrow key navigation."""
    st.markdown("""
    <script>
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
            const nextBtn = document.querySelector('button[kind="secondary"]');
            const buttons = document.querySelectorAll('button');
            for (const btn of buttons) {
                if (btn.textContent.includes('Nākamais')) {
                    btn.click();
                    break;
                }
            }
        }
        if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
            const buttons = document.querySelectorAll('button');
            for (const btn of buttons) {
                if (btn.textContent.includes('Iepriekšējais')) {
                    btn.click();
                    break;
                }
            }
        }
    });
    </script>
    """, unsafe_allow_html=True)
```

Call `inject_keyboard_nav()` at the end of `render_navigation()`.

**Step 2: Add presenter notes in sidebar**

In `app.py`, add after `apply_theme()`:

```python
with st.sidebar:
    st.markdown("### 📋 Prezentētāja Piezīmes")
    notes = {
        1: "Sveicināt auditoriju. Iepazīstināt ar tēmu.",
        2: "Uzsvērt: tas nav nākotne — tas ir TAGAD.",
        3: "Pajautāt: cik lietojat Excel aprēķiniem?",
        4: "Parādīt design.kforma.lv pārlūkā.",
        5: "Demonstrēt 2-3 moduļus live vai video.",
        6: "Koda piemērs — uzsvērt lasāmību.",
        7: "Ātri pārskaitīt, neiedziļinoties katrā.",
        8: "Parādīt Claude Code termināli ja iespējams.",
        9: "Konkrēti skaitļi — 30 min vs 6h.",
        10: "SVARĪGI: AI nav burvju nūjiņa, jāverificē!",
        11: "Aizraujoša tēma — pieminēt ka tas ir legāls.",
        12: "Parādīt Railway dashboard ja ir laiks.",
        13: "Ātri pārskaitīt, GPAI piemērs live.",
        14: "Ja auditorijā ir Revit lietotāji — uzsvērt.",
        15: "Ieteikt Flocode kā pirmo resursu.",
        16: "Aicinājums — Latvija nedrīkst atpalikt.",
        17: "Paldies! QR kods uz ekrāna.",
    }
    slide = st.session_state.current_slide
    st.info(notes.get(slide, ""))

    st.markdown("---")
    st.markdown(f"**Laiks:** ~{slide * 1.5:.0f} / 25 min")
```

**Step 3: Run final verification**

```bash
cd "/home/nauris/Dropbox/Projects/LBPA 2026" && streamlit run app.py
```
Expected: Arrow keys navigate slides. Sidebar shows presenter notes. All 17 slides render correctly with consistent theme.

---

### Task 12: Screenshots & Video Placeholders

**Note:** This task is manual — requires capturing screenshots from design.kforma.lv.

**Screenshots needed (save to `assets/images/`):**
1. `demo_kf3d.png` — KF3D FEM module with a 3D model
2. `demo_pile.png` — Pile CPT module with chart
3. `demo_bending.png` — Bending module with results
4. `demo_punching.png` — Punching module with SVG visualization
5. `platform_home.png` — Platform landing page

**Videos needed (save to `assets/videos/`):**
1. `demo_kf3d.mp4` — Screen recording of KF3D usage
2. `demo_pile.mp4` — Screen recording of Pile CPT
3. `demo_bending.mp4` — Screen recording of Bending
4. `demo_punching.mp4` — Screen recording of Punching

**Recording tip:** Use OBS Studio or simple screen recorder, 720p, 30-60 seconds each.

---

## Summary

| Task | Description | Files |
|------|-------------|-------|
| 1 | Scaffolding & deps | app.py, requirements.txt, config |
| 2 | Navigation & framework | components/navigation.py, styling.py |
| 3 | Assets & media helpers | components/media.py, copied images |
| 4 | Slides 1-4 | Title, New Era, Problem, Solution |
| 5 | Slide 5 | Demo (tabbed modules) |
| 6 | Slides 6-7 | Why Python, Libraries |
| 7 | Slides 8-10 | AI Assistant, Examples, Prediction |
| 8 | Slide 11 | Ralph Wiggum method |
| 9 | Slides 12-14 | Deployment, Tools, PyRevit |
| 10 | Slides 15-17 | Podcasts, Universities, Summary+QR |
| 11 | Polish | Keyboard nav, presenter notes |
| 12 | Media (manual) | Screenshots & videos from platform |
