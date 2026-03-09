# LBPA 2026 Kongresa Prezentācija - Projekta Konteksts

## Projekta mērķis
Interaktīva Streamlit prezentācija LBPA (Latvijas Būvinženieru Projektēšanas Asociācija) kongresam par AI izmantošanu būvkonstrukciju projektēšanā.

## Organizācija
- **LBPA** - lbpa.lv
- Vizuālā identitāte: #32373c (tumši pelēks), #ffffff (balts), minimālistisks profesionāls stils
- 70+ biedri, ikgadēji semināri, "Būvkonstruktors" balva

## design.kforma.lv platforma
- **Lokācija:** `/home/nauris/Dropbox/Projects/structural-design-tools`
- **Tehnoloģijas:** Flask, SQLAlchemy, Bootstrap 5, Railway hosting
- **Statistika:** 73 Python faili, 44 HTML templates, ~148,000 koda rindas, 31 aprēķinu moduļi
- **Standarti:** EC2, EC3, EC5, EC7, EN 1991 (ar LV NA)
- **Logo:** `/home/nauris/Dropbox/Projects/structural-design-tools/static/images/k-forma-rgb-transparent.png`
- **Vizuālā identitāte:** Ciāna/tirkīza (#00BCD4) uz tumša fona (#1a1f2e, #151a28)
- **Deployment:** Railway.app + Cloudflare DNS, PostgreSQL production, Docker (Python 3.10-slim)

### Jaudīgākie moduļi (pēc koda apjoma)
1. **KF3D FEM** - 11,022 rindas (template) - 3D strukturālā analīze ar Three.js + PyNite
2. **Pile Design (CPT)** - 2,789 rindas - ģeotehniskā analīze ar CPT datiem
3. **Graphics Module** - 2,574 rindas - centrālais vizualizāciju dzinējs
4. **Ties/Floor Ties** - 2,331 rindas - grīdu saišu projektēšana
5. **Bending Analysis** - 1,953 rindas - DB liece ar EC2/GEM/Mander modeļiem
6. **Steel Beam** - 1,438 rindas - tērauda siju kapacitāte un stabilitāte

### Galvenās Python bibliotēkas platformā
- NumPy, SciPy - skaitliskā analīze
- Matplotlib - vizualizācijas (base64 embed)
- concreteproperties - dzelzsbetona šķērsgriezumi, M-N diagrammas
- sectionproperties - ģeometriskās īpašības
- structuralcodes - Eirokodeksu formulas (EC2, MC2010)
- gmsh + scikit-fem - FEM režģi un analīze
- PyNite - 3D frame/shell FEM

## Esošie dokumenti (docs/ mapē)
1. **PREZENTACIJA.md** - 22 slaidu uzmetums (v1.0, 2026-02-12)
2. **AI_IZSTRADE.md** - Claude Code lietošanas piemēri (SVG, MC2010, Railway, stiegrojums)
3. **BIBLIOTEKU_APRAKSTS.md** - Python bibliotēku detalizēts apraksts
4. **PROJEKTA_STRUKTURA.md** - Tehniskais pārskats ar moduļu sarakstu

## Faili projekta mapē
- `1734784405264.jpg` - BTF Digital "Beam Support Verification" ekrānšāviņš (komerciāla programma, EC2)
- `gustafsson2020scikit-fem.pdf` - scikit-fem zinātniskais raksts (JOSS, 2020)

## Prezentācijas tēmas (lietotāja pieprasījums)
1. design.kforma.lv platforma un tās labākie moduļi ar Gemini integrāciju
2. Python bibliotēkas: structuralcodes, concreteproperties, sectionproperties u.c.
3. PyRevit - Revit add-ins ar Python
4. Podkāsti: flocode u.c.
5. Rīki: Viktor, calctree.com, calcpad, GPAI
6. Claude Code uz Linux mašīnas (terminālis)
7. Reverse engineering komerciālām programmām ar AI ("Simpsonu metode")
8. Jaunā ēra - indivīds var radīt rīkus ko agrāk tikai lielas komandas
9. Resursi: Railway, GitHub, Streamlit
10. AI prediction vs deterministic results + Python bibliotēku loma
11. Universitātes kas māca Python inženieriem
12. Interaktīvi ar audio/video efektiem

## Formāts
**Streamlit app** - interaktīva prezentācija ar live demo iespējām

## Streamlit Cloud ierobežojumi

- **Inline SVG nestrādā** — `st.markdown("<svg>...</svg>", unsafe_allow_html=True)` tiek nogriezts. Streamlit Cloud strip SVG tagus no unsafe_allow_html. Vizuālas diagrammas jāveido ar HTML/CSS (div, flexbox, border, border-radius) vai ar `st.image()` (base64/fails).
- **design.kforma.lv** ir tikai piemērs, ne produkts — visur jāformulē kā ilustrācija.
- **Uzņēmuma nosaukums:** K FORMA (ar atstarpi), ne KFORMA.
- **Hosting:** Streamlit Community Cloud, repo Inovskis/LBPA-2026 (public), push uz `main` UN `master`.
