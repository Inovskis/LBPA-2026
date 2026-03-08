# Dizains: LBPA 2026 Streamlit Prezentācija

**Datums:** 2026-03-08
**Statuss:** Apstiprināts

## Mērķis
Interaktīva Streamlit prezentācija LBPA kongresam par AI un Python izmantošanu būvkonstrukciju projektēšanā. 20-30 minūtes, latviešu valodā.

## Tehnoloģija
- **Framework:** Streamlit multipage app
- **Navigācija:** Slaidu režīms ar prev/next pogām + progress bar
- **Valoda:** Latviešu
- **Demo:** Screenshots + video ieraksti (bez live iframe)
- **Vizuālā identitāte:** LBPA (#32373c) + K-forma (#00BCD4, #1a1f2e)
- **Logo:** LBPA logo + K-forma logo (no structural-design-tools/static/images/)

## Slaidu struktūra (17 slaidi, ~25 min)

### 1. Tituls (0:30)
- LBPA + K-forma logo
- "AI un Python Būvkonstrukciju Projektēšanā"
- Autors: Nauris
- Datums

### 2. Jaunā ēra (2:00)
- Demokratizācija: indivīds var radīt rīkus ko agrāk tikai lielas komandas ar milzīgiem budžetiem
- Vizuāls salīdzinājums: agrāk vs tagad
- Iedvesmojoši piemēri

### 3. Problēma (1:30)
- Excel: grūti izsekot formulas, nav versiju kontroles
- MathCAD: dārga licence, ierobežotas vizualizācijas
- Komerciālā programmatūra: "black box", augsta cena
- BTF Digital screenshot kā piemērs (1734784405264.jpg)

### 4. Risinājums: design.kforma.lv (1:30)
- Platforma pārskats: 31 modulis, ~148,000 koda rindas
- Eirokodeksi: EC2, EC3, EC5, EC7, EN 1991 ar LV NA
- Bezmaksas, web-bāzēta, atvērts kods
- Screenshot no platformas

### 5. Demo: Labākie moduļi (3:00)
- KF3D FEM (3D strukturālā analīze)
- Pile Design CPT (ģeotehniskā analīze)
- Bending Analysis (lieces aprēķins ar M-N diagrammām)
- Punching (caurspiešana ar SVG vizualizāciju)
- Video ieraksti vai annotēti screenshots

### 6. Kāpēc Python (1:30)
- Bezmaksas un atvērts kods
- Bagāta bibliotēku ekosistēma
- Lasāms kods (EC2 formula piemērs)
- Liela kopiena un atbalsts

### 7. Python bibliotēkas (2:00)
- structuralcodes: validētas Eirokodeksu formulas
- concreteproperties: dzelzsbetona šķērsgriezumu analīze
- sectionproperties: ģeometriskās īpašības
- scikit-fem + gmsh: FEM analīze
- PyNite: 3D frame analīze
- Koda piemēri ar syntax highlighting

### 8. AI kā izstrādes palīgs (1:30)
- Claude Code uz atsevišķas Linux mašīnas (terminālis)
- Kas tas ir: AI asistents kas lasa, raksta, izpilda kodu
- Kāpēc: ātrums, kvalitāte, debugging
- Screenshot/video no Claude Code sesijas

### 9. AI piemēri (2:00)
- SVG vizualizācija: 30 min vs 4-6h tradicionāli
- MC2010 integrācija: vienību kļūdas diagnostika
- Railway deployment: 2 rindu fix
- Laika ietaupījuma tabula: ~5x ātrāk

### 10. AI prediction vs determinisms (2:00)
- AI ir prognožu (prediction) metode - var kļūdīties
- Būvkonstrukcijām nepieciešams determinēts rezultāts
- Risinājums: Python bibliotēkas (structuralcodes, concreteproperties) nodrošina determinētus, validētus aprēķinus
- AI palīdz rakstīt kodu, bet formulas nāk no verificētām bibliotēkām
- Vienmēr verificēt pret standartiem

### 11. Ralph Wiggum metode (2:00)
- Geoffrey Huntley: 5 rindu Bash cilpa
- Iteratīvi baro AI ar output (kļūdas, stack traces) atpakaļ kā input
- "Kontekstuālais spiediena katls" - atkārto līdz programma strādā
- Piemērs: komerciālas programmatūras klonēšana (grāmatvedības programma)
- Claude Code plugin pieejams
- Video/animācija kas parāda cikla procesu

### 12. Deployment resursi (1:30)
- Railway.app: Cloud hosting ar Docker, auto-deploy no GitHub
- GitHub: versiju kontrole, sadarbība
- Streamlit: alternatīva ātrai app izveidei
- Docker: reproducējama vide
- design.kforma.lv deployment piemērs

### 13. Citi labi rīki (2:00)
- Viktor.AI: low-code inženieru app platforma ar Python
- CalcTree: cloud-bāzēti inženieru aprēķini, Python & MathJS, €2.3M investīcijas
- Calcpad: bezmaksas open-source aprēķinu rīks, 100+ Eirokodeksu šabloni
- GPAI (gpai.app): AI STEM solver - foto/PDF input, triple-verified (GPT-5, Gemini, Deepseek)
  - Live piemērs: vienkāršs inženierijas prompts → risinājums ar vizualizāciju
- Screenshots no katra rīka

### 14. PyRevit (1:00)
- Bezmaksas open-source Revit add-in
- Python skripti bez Visual Studio
- Automatizē atkārtojošos uzdevumus
- Piemērs: strukturālā modelēšana, batch operācijas
- Zemāks barjeras slieksnis nekā C# add-ini

### 15. Podkāsti un resursi (1:00)
- Flocode (James O'Reilly): Python + inženierija
  - Epizodes: structuralcodes (Morten Engen), PyNite (Craig Brinck), Connor Ferster
- StructuralPython (structuralpython.com)
- EngineeringSkills.com
- civils.ai kurss

### 16. Universitātes (1:00)
- NTNU (Norvēģija): "Python for Structural Engineering" kurss (2026 pavasaris)
- Cal Poly (ASV): architectural engineering computing
- Ko darīt Latvijā: integrēt Python RTU/LLU inženieru programmās
- Aicinājums LBPA: atbalstīt Python apmācību iniciatīvas

### 17. Kopsavilkums + Jautājumi (1:30)
- 3 galvenie secinājumi:
  1. Python ir spēcīgs bezmaksas rīks inženieriem
  2. AI paātrina izstrādi ~5x (bet jāverificē!)
  3. Jaunā ēra: katrs indivīds var radīt profesionālus rīkus
- QR kods uz design.kforma.lv
- Kontaktinfo
- Jautājumi

## Tehniskie detaļi

### Streamlit app struktūra
```
lbpa-presentation/
├── app.py                    # Galvenais Streamlit app
├── pages/                    # Nav izmantots (single-page ar session state)
├── assets/
│   ├── images/               # Screenshots, logo
│   ├── videos/               # Demo video ieraksti
│   └── audio/                # Skaņas efekti (opcija)
├── slides/                   # Katra slaida saturs kā Python modulis
│   ├── __init__.py
│   ├── slide_01_title.py
│   ├── slide_02_new_era.py
│   ├── ...
│   └── slide_17_summary.py
├── components/
│   ├── navigation.py         # Prev/Next pogas, progress bar
│   ├── styling.py            # CSS, krāsas, fonti
│   └── media.py              # Video/audio embed helpers
├── requirements.txt
└── README.md
```

### Navigācijas mehānisms
- `st.session_state.current_slide` kontrolē aktīvo slaidu
- Prev/Next pogas lapas apakšā
- Progress bar augšā
- Keyboard shortcut support (ja iespējams)

### Stilizācija
- Custom CSS ar st.markdown(unsafe_allow_html=True)
- LBPA krāsas: #32373c (fons), #ffffff (teksts)
- K-forma akcents: #00BCD4 (tirkīza)
- Tumšs/profesionāls dizains
- Fonti: sans-serif (modernais stils)

### Video/Audio
- st.video() priekš demo ierakstiem
- Vienkārši pārejas efekti ar CSS animācijām
- st.balloons() / st.snow() kā akcenti

## Avoti un resursi

- Ralph Wiggum metode: Geoffrey Huntley, awesomeclaude.ai/ralph-wiggum
- Flocode podcast: flocode.substack.com
- Viktor.AI: viktor.ai
- CalcTree: calctree.com
- Calcpad: calcpad.eu
- GPAI: gpai.app
- PyRevit: docs.pyrevitlabs.io
- NTNU kurss: ntnu.edu/studies/courses/KT6198
- scikit-fem: Gustafsson & McBain (2020), JOSS
