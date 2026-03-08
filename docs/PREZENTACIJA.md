# Prezentācija: AI un Python Būvkonstrukciju Projektēšanā

## Informācija

**Ilgums:** 20-30 minūtes
**Mērķauditorija:** Inženieri-konstruktori
**Platforma:** design.kforma.lv

---

# SLAIDS 1: Tituls

## AI un Python Būvkonstrukciju Projektēšanā

**Praktiska pieredze ar design.kforma.lv**

*[Tavs vārds]*
*[Datums]*

---

# SLAIDS 2: Par Mani

## Kas es esmu

- Būvinženieris / Konstruktors
- Python programmētājs
- design.kforma.lv izstrādātājs

### Ko šodien apskatīsim:
1. Kāpēc Python inženieriem?
2. Platformas demonstrācija
3. AI kā izstrādes palīgs

---

# SLAIDS 3: Problēma

## Tradicionālo Rīku Ierobežojumi

### Excel
- Grūti izsekot formulas
- Nav versiju kontroles
- Kļūdas kopējot

### MathCAD / SMath
- Dārga licence (MathCAD)
- Ierobežotas vizualizācijas
- Nav web pieejamības

### Komerciālā programmatūra
- Augsta cena
- "Black box" aprēķini
- Nav pielāgojama

---

# SLAIDS 4: Risinājums

## Web Platforma ar Python

### design.kforma.lv

- **Bezmaksas** lietošanai
- **Web-bāzēta** - pieejama jebkurā ierīcē
- **Atvērts kods** - pārredzamas formulas
- **Validēta** pret Eirokodeksiem

### Skaiti

| Parametrs | Vērtība |
|-----------|---------|
| Aprēķinu moduļi | 26+ |
| Koda rindas | ~148,000 |
| Standarti | EC2, EC3, EC5, EC7, EN1991 |

---

# SLAIDS 5: Kāpēc Python?

## Python Priekšrocības Inženieriem

### 1. Bezmaksas un Atvērts
- Nav licences maksu
- Liela kopiena

### 2. Bagāta Bibliotēku Ekosistēma
```python
import numpy as np       # Matricas
import matplotlib.pyplot # Grafiki
from concreteproperties import ...  # Dzelzsbetona analīze
```

### 3. Lasāms Kods
```python
# EC2 formula - uzreiz saprotama
k = min(1 + sqrt(200/d), 2.0)
v_Rd_c = 0.18/gamma_c * k * (100*rho_l*fck)**(1/3)
```

---

# SLAIDS 6: Galvenās Bibliotēkas

## Python Bibliotēkas Konstrukcijām

| Bibliotēka | Mērķis |
|------------|--------|
| **NumPy** | Matricu operācijas |
| **Matplotlib** | Grafiki un diagrammas |
| **concreteproperties** | Dzelzsbetona šķērsgriezumi |
| **sectionproperties** | Ģeometriskās īpašības |
| **structuralcodes** | Eirokodeksu formulas |
| **gmsh + scikit-fem** | FEM analīze |

### Visas ir BEZMAKSAS un open-source!

---

# SLAIDS 7: structuralcodes Bibliotēka

## Validētas Eirokodeksu Formulas

```python
from structuralcodes.codes.ec2_2004 import (
    v_rdc_punching,  # Caurspiešana
    k_factor,        # k koeficients
)

# Aprēķins ar validētām formulām
v_Rd_c = v_rdc_punching(
    d_eff=200,    # mm
    f_ck=30,      # MPa
    rho_l=0.015,  # -
    gamma_c=1.5   # -
)
```

### Priekšrocība: Formulas jau pārbaudītas!

---

# SLAIDS 8: Vizualizācijas

## Matplotlib - Profesionāli Grafiki

*[Screenshot: M-N diagramma no platformas]*

```python
import matplotlib.pyplot as plt

# M-N diagrammas izveide
plt.plot(M_values, N_values)
plt.fill(M_values, N_values, alpha=0.3)
plt.xlabel('Moments M (kNm)')
plt.ylabel('Normālspēks N (kN)')
```

### Rezultāts: Atskaites kvalitātes grafiki

---

# SLAIDS 9: DEMO - Platformas Pārskats

## design.kforma.lv

*[Pārslēgties uz live demo vai screenshots]*

### Demonstrējamie moduļi:
1. **Liece** - pamata aprēķins
2. **Caurspiešana** - ar SVG vizualizāciju
3. **Vēja slodzes** - ar 3D grafiku

---

# SLAIDS 10: DEMO - Lieces Modulis

## Sijas Lieces Aprēķins

*[Screenshot vai live demo]*

### Funkcionalitāte:
- Ievada: šķērsgriezums, moments, materiāli
- Izvada: nepieciešamais stiegrojums
- Grafiks: spriegumu sadalījums

---

# SLAIDS 11: DEMO - Caurspiešana

## Caurspiešanas Aprēķins ar Vizualizāciju

*[Screenshot ar SVG plānskatu]*

### Funkcionalitāte:
- Interaktīvs plānskats (SVG)
- EC2 un MC2010 salīdzinājums
- Automātiska kāpuru izvēle

---

# SLAIDS 12: DEMO - Vēja Slodzes

## 3D Vēja Spiediena Vizualizācija

*[Screenshot ar 3D grafiku]*

### Funkcionalitāte:
- Reljefa kategorijas izvēle
- Spiediena profila 3D grafiks
- Eksponēšanas koeficienti

---

# SLAIDS 13: AI Izstrādē - Ievads

## Claude Code kā Izstrādes Palīgs

### Kas tas ir?
- AI asistents komandrindā
- Var lasīt, rakstīt, izpildīt kodu
- Saprot kontekstu un mērķus

### Kāpēc izmantot?
- **Ātrums** - sarežģītas funkcijas stundās
- **Kvalitāte** - konsekvents kods
- **Debugging** - efektīva problēmu risināšana

---

# SLAIDS 14: AI Piemērs 1 - SVG Vizualizācija

## Uzdevums: Izveidot interaktīvu plānskatu

### Dialogs ar AI:
```
Es: "Pievieno SVG vizualizāciju caurspiešanas modulim
     ar kolonnas skatu no augšas"

AI: "Izveidošu trīs komponentes: PunchingViz,
     SectionViz, PunchingResultsViz..."
```

### Rezultāts:
- ~400 rindas JavaScript
- Izstrādāts **30 minūtēs**
- Tradicionāli: 4-6 stundas

---

# SLAIDS 15: AI Piemērs 2 - Kļūdu Labošana

## Uzdevums: MC2010 integrācija

### Problēma:
```
v_Rd,c = 271,562 MPa  # ???
# Jābūt ~0.5-1.5 MPa
```

### AI Diagnostika:
```
AI: "Funkcija atgriež SPĒKU (N), nevis
     SPRIEGUMU (MPa). Vienību kļūda!"
```

### Risinājums:
```python
# Pareiza formula
v_rdc = k_psi * sqrt(fck) / gamma_c
```

---

# SLAIDS 16: AI Piemērs 3 - Deployment

## Uzdevums: "Bad Gateway" kļūda

### Situācija:
- Lokāli strādā (port 5000)
- Production nestrādā

### AI Atklājums:
```python
# Problēma: hardkodēts ports
app.run(port=5000)

# Risinājums: Railway dinamisks ports
port = os.environ.get('PORT', 5000)
```

### Rezultāts: 2 rindu fix, 15 minūtes

---

# SLAIDS 17: AI Efektivitāte

## Laika Ietaupījums

| Uzdevums | Bez AI | Ar AI |
|----------|--------|-------|
| SVG vizualizācija | 4-6 h | 30 min |
| Bibliotēkas integrācija | 2-3 h | 20 min |
| Deployment fix | 1-2 h | 15 min |
| Jauna funkcionalitāte | 2-4 h | 45 min |

### ~5x ātrāk ar AI palīdzību

---

# SLAIDS 18: AI Izmantošanas Principi

## Efektīva AI Lietošana

### 1. Skaidrs uzdevums
```
❌ "Uztaisi vizualizāciju"
✓ "Izveido SVG ar kolonnu centrā un perimetru 2d attālumā"
```

### 2. Iteratīva pieeja
- Pamata funkcionalitāte → Uzlabojumi → Testēšana

### 3. Vienmēr verificēt!
- AI var kļūdīties
- Testēt ar reāliem datiem
- Validēt pret standartiem

---

# SLAIDS 19: Tehniskā Arhitektūra

## Platformas Uzbūve

```
┌─────────────────────────────────────┐
│           Frontend (HTML/JS)        │
├─────────────────────────────────────┤
│           Flask (Python)            │
├─────────────────────────────────────┤
│        Calculations (Python)        │
│  ┌─────────┐ ┌────────┐ ┌────────┐  │
│  │ NumPy   │ │ gmsh   │ │ struct │  │
│  │ SciPy   │ │ skfem  │ │ codes  │  │
│  └─────────┘ └────────┘ └────────┘  │
├─────────────────────────────────────┤
│          Database (SQLite)          │
└─────────────────────────────────────┘
```

---

# SLAIDS 20: Turpmākie Plāni

## Platformas Attīstība

### Plānotie moduļi:
- Pamatu aprēķini (EN 1997)
- Seismiskie aprēķini (EN 1998)
- PDF atskaišu ģenerēšana

### Infrastruktūra:
- Automatizēta testēšana
- API dokumentācija
- Mobile-friendly UI

---

# SLAIDS 21: Kopsavilkums

## Galvenie Secinājumi

### 1. Python ir spēcīgs rīks inženieriem
- Bezmaksas bibliotēkas
- Validētas formulas
- Profesionālas vizualizācijas

### 2. AI paātrina izstrādi ~5x
- Sarežģītas funkcijas stundās
- Efektīva problēmu risināšana
- Bet nepieciešama verifikācija!

### 3. Web platformas ir nākotne
- Pieejamība jebkurā ierīcē
- Nav instalācijas
- Vienmēr aktuāla versija

---

# SLAIDS 22: Aicinājums

## Izmēģini Pats!

### design.kforma.lv

- Bezmaksas reģistrācija
- 26+ aprēķinu moduļi
- Regulāri atjauninājumi

### Jautājumi?

*[Kontaktinformācija]*

---

# DEMO SCENĀRIJS

## Sagatavotie Ievaddati

### Moduļis 1: Liece
- Sija 300x500 mm
- MEd = 150 kNm
- Betons C30/37

### Moduļis 2: Caurspiešana
- Kolonna 400x400 mm
- Plātne h=250 mm
- VEd = 500 kN

### Moduļis 3: Vēja Slodze
- Augstums 12 m
- Terrain II
- Latvija, Rīga

---

# BACKUP MATERIĀLI

## Ja Internets Nestrādā

Sagatavot screenshots:
1. [ ] Platformas sākumlapa
2. [ ] Lieces modulis ar rezultātiem
3. [ ] Caurspiešanas SVG vizualizācija
4. [ ] Vēja slodzes 3D grafiks
5. [ ] M-N diagrammas piemērs

---

# PRESENTER NOTES

## Laika Sadalījums

| Sadaļa | Minūtes |
|--------|---------|
| Ievads | 3 |
| Kāpēc Python | 5 |
| Demo | 8 |
| AI piemēri | 7 |
| Arhitektūra | 4 |
| Q&A | 3 |
| **Kopā** | **30** |

## Atgādnes

- Runāt lēnām pie koda piemēriem
- Demo: ja kaut kas nestrādā, pāriet uz screenshots
- Q&A: ja nav jautājumu, parādīt papildus moduli

---

*Prezentācija izveidota: 2026-02-12*
*Versija: 1.0*
