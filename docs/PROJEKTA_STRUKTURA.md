# RC Design Web - Projekta Tehniskais Pārskats

## Pārskats

**RC Design Web** ir web-bāzēta platforma būvkonstrukciju aprēķiniem, kas pieejama [design.kforma.lv](https://design.kforma.lv). Platforma nodrošina inženieriem ātrus, uzticamus aprēķinus saskaņā ar Eirokodeksu standartiem.

---

## Projekta Statistika

| Parametrs | Vērtība |
|-----------|---------|
| Python faili | 73 |
| HTML templates | 44 |
| JavaScript/CSS | 15+ |
| Kopējās koda rindas | ~148,000 |
| Aprēķinu moduļi | 26+ |
| Atbalstītie standarti | EC2, EC3, EC5, EC7, EN 1991 |

---

## Tehnoloģiju Stack

### Backend
- **Flask** - Python web framework
- **SQLAlchemy** - ORM datubāzes operācijām
- **Flask-Login** - Lietotāju autentifikācija
- **Jinja2** - HTML templating

### Frontend
- **Bootstrap 5** - UI framework
- **JavaScript (ES6+)** - Interaktīvas funkcijas
- **SVG** - Vektoru grafikas vizualizācijas
- **CSS3** - Stili un animācijas

### Deployment
- **Railway** - Cloud hosting platforma
- **Cloudflare** - DNS un CDN
- **SQLite/PostgreSQL** - Datubāze

---

## Projekta Struktūra

```
rc-design-web/
├── app.py                    # Flask aplikācijas ieejas punkts
├── config/
│   └── settings.py           # Konfigurācijas iestatījumi
├── models/
│   ├── user.py               # Lietotāja modelis
│   ├── saved_calculation.py  # Saglabāto aprēķinu modelis
│   └── shared_preset.py      # Koplietojamo preset modelis
├── routes/                   # API un lappušu maršruti
│   ├── main.py               # Galvenās lapas
│   ├── bending.py            # Lieces aprēķini
│   ├── punching.py           # Caurspiešanas aprēķini
│   ├── column.py             # Kolonnu aprēķini
│   ├── wall.py               # Sienu aprēķini
│   └── ...                   # 20+ citi moduļi
├── calculations/             # Aprēķinu loģika
│   ├── bending_calc.py       # Lieces formulas
│   ├── punching_calc.py      # Caurspiešanas formulas
│   ├── column_calc.py        # Kolonnu formulas
│   └── ...                   # Katram modulim savs fails
├── templates/
│   ├── base.html             # Bāzes template
│   ├── modules/              # Moduļu lapas
│   │   ├── bending.html
│   │   ├── punching.html
│   │   └── ...
│   └── errors/               # Kļūdu lapas
├── static/
│   ├── css/                  # Stili
│   ├── js/                   # JavaScript
│   └── images/               # Attēli
└── docs/                     # Dokumentācija
```

---

## Aprēķinu Moduļi

### Dzelzsbetona Konstrukcijas (EC2)
| Modulis | Apraksts | Standarts |
|---------|----------|-----------|
| **Liece (Bending)** | Sijas un plātnes lieces aprēķins | EN 1992-1-1 |
| **Caurspiešana (Punching)** | Plātņu caurspiešanas izturība | EN 1992-1-1 §6.4 |
| **Kolonnas** | Kolonnu nestspēja ar M-N diagrammām | EN 1992-1-1 §5.8 |
| **Sienas** | Nesošo sienu aprēķins | EN 1992-1-1 |
| **Konsoles (Corbels)** | Īso konsolu projektēšana | EN 1992-1-1 §6.5 |
| **Detalizēšana** | Stiegrojuma izvietojuma prasības | EN 1992-1-1 §8 |
| **Pāļi** | Pāļu nestspēja | EN 1992-1-1 |
| **Pāļu rosti** | FEM analīze ar gmsh/scikit-fem | EN 1992-1-1 |
| **Saskares zona** | Lieces spraugas aprēķins | EN 1992-1-1 §6.2.5 |
| **HCS (Hollowcore)** | Dobās plātnes analīze | EN 1992-1-1 |
| **Šķērsgriezums** | Vispārēja šķērsgriezuma analīze | EN 1992-1-1 |
| **Aizsargslānis** | Betona aizsargslāņa noteikšana | EN 1992-1-1 §4 |

### Tērauda Konstrukcijas (EC3)
| Modulis | Apraksts | Standarts |
|---------|----------|-----------|
| **Tērauda sija** | Siju liece un bīde | EN 1993-1-1 |
| **Finplate** | Bīdes savienojumi | EN 1993-1-8 |
| **Finplate FEM** | FEM analīze savienojumiem | EN 1993-1-8 |
| **Gala plāksne** | Momentu savienojumi | EN 1993-1-8 |
| **Saites** | Vertikālo saišu aprēķins | EN 1993-1-1 |

### Koka Konstrukcijas (EC5)
| Modulis | Apraksts | Standarts |
|---------|----------|-----------|
| **Koka sija** | Lieces un bīdes aprēķins | EN 1995-1-1 |

### Slodzes (EN 1991)
| Modulis | Apraksts | Standarts |
|---------|----------|-----------|
| **Sniega slodze** | Jumta sniega slodzes | EN 1991-1-3 |
| **Vēja slodze** | Vēja spiediens ar 3D vizualizāciju | EN 1991-1-4 |
| **Lietderīgās slodzes** | Grīdu slodzes pēc kategorijām | EN 1991-1-1 |
| **Pastāvīgās slodzes** | Materiālu tilpumsvari | EN 1991-1-1 |
| **Kombinācijas** | Slodžu kombinācijas | EN 1990 |

### Papildus Rīki
| Modulis | Apraksts |
|---------|----------|
| **Materiāli** | Betona, tērauda, koka parametri |
| **Saglabātie aprēķini** | Lietotāju projektu pārvaldība |
| **FEM Vizualizācija** | 3D spriegumu attēlojums |

---

## Drošība un Autentifikācija

- **Flask-Login** lietotāju sesiju pārvaldībai
- **Werkzeug** paroļu hash-ēšanai (PBKDF2)
- **CSRF aizsardzība** formās
- **SQL injection aizsardzība** caur SQLAlchemy ORM
- **XSS aizsardzība** caur Jinja2 auto-escaping

---

## Deployment Process

### Railway Konfigurācija
```python
# app.py - PORT konfigurācija
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```

### Deployment Soļi
1. Git push uz `main` branch
2. Railway automātiski build un deploy
3. Cloudflare nodrošina SSL un CDN

### Vides Mainīgie
- `FLASK_ENV` - development/production
- `DATABASE_URL` - PostgreSQL savienojums
- `SECRET_KEY` - Flask secret key
- `PORT` - Railway dinamiskais ports

---

## Izstrādes Rīki

### AI Asistents
- **Claude Code** - koda rakstīšana un debugging
- Efektīvs sarežģītu funkciju izstrādei
- SVG vizualizāciju automatizēta izveide
- Kļūdu diagnostika un labošana

### Version Control
- **Git** - versiju kontrole
- **GitHub** - repozitorija hosting

### Testēšana
- Lokāla testēšana ar `flask run`
- Production testēšana uz Railway

---

## Veiktspēja

### Optimizācijas
- Static failu kešošana (7 dienas)
- Lazy loading vizualizācijām
- Efektīvas SQL vaicājumi
- Minimāla JavaScript bibliotēku izmantošana

### Monitorings
- Railway logs reāllaika monitoringam
- Kļūdu apstrāde ar traceback

---

## Turpmākā Attīstība

### Plānotie Moduļi
- Pamatu aprēķini (EN 1997)
- Seismiskie aprēķini (EN 1998)
- Ugunsdrošības aprēķini
- PDF atskaišu ģenerēšana

### Infrastruktūras Uzlabojumi
- Automatizēta testēšana (pytest)
- CI/CD pipeline
- API dokumentācija (OpenAPI)

---

*Dokuments izveidots: 2026-02-12*
*Autors: RC Design Web Team*
