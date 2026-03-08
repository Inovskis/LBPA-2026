# AI Kā Izstrādes Palīgs - Reāli Piemēri

## Pārskats

Šis dokuments apraksta, kā **Claude Code** (Anthropic AI asistents) tika izmantots RC Design Web platformas izstrādē. Dokumentā ir iekļauti konkrēti piemēri no reālām izstrādes sesijām.

---

## Kas ir Claude Code?

**Claude Code** ir AI asistents, kas darbojas komandrindas vidē un var:
- Lasīt un rakstīt kodu
- Pārlūkot failu sistēmu
- Izpildīt bash komandas
- Veikt web meklēšanu dokumentācijai
- Analizēt kļūdas un piedāvāt risinājumus

### Galvenās Priekšrocības
1. **Ātrums** - Sarežģītas funkcijas stundās, nevis dienās
2. **Kvalitāte** - Konsekventas koda prakses
3. **Debugging** - Efektīva kļūdu diagnostika
4. **Dokumentācija** - Automātiska koda komentēšana

---

## Piemērs 1: SVG Vizualizācijas Izveide

### Uzdevums
Pievienot interaktīvu plānskatu caurspiešanas (punching) modulim, kas attēlo:
- Kolonnas novietojumu (iekšējā/malas/stūra)
- Kritisko perimetru u₁
- Stiegrojuma virzienu simbolus

### AI Risinājums

Claude Code izveidoja pilnīgu SVG vizualizācijas sistēmu ar trim objektiem:

```javascript
// Izveidotie objekti
const PunchingViz = {
    // Plānskata vizualizācija ar kritisko perimetru
    draw: function(params) { ... }
};

const SectionViz = {
    // Šķērsgriezuma vizualizācija
    draw: function(params) { ... }
};

const PunchingResultsViz = {
    // Rezultātu grafiskais attēlojums
    draw: function(params) { ... }
};
```

### Rezultāts
- ~400 rindas JavaScript koda
- Interaktīva vizualizācija, kas atjaunojas reāllaikā
- Izstrādāts **1 sesijā** (~30 min)

### AI Dialoga Fragments
```
User: Pievieno SVG vizualizāciju caurspiešanas modulim ar kolonnas
      skatu no augšas un kritisko perimetru

Claude: Es izveidošu vizualizācijas sistēmu ar trim komponentiem...
        [Izveido PunchingViz, SectionViz, PunchingResultsViz]

User: Virsraksts pārklājas ar saturu

Claude: Pārvietošu virsrakstu un palielināšu SVG augstumu...
        [Labo SVG viewBox un elementu pozīcijas]
```

---

## Piemērs 2: MC2010 Integrācija

### Uzdevums
Salīdzināt EC2 (Eirokodekss 2) caurspiešanas aprēķinu ar fib Model Code 2010, izmantojot `structuralcodes` bibliotēku.

### Problēma
Sākotnējā implementācija atgrieza nereālu vērtību:
```
v_Rd,c (MC2010) = 271562 MPa  # Acīmredzami nepareizi!
```

### AI Diagnostika

Claude Code analizēja bibliotēkas funkciju:

```python
# Problēma: v_rdc_punching() atgriež SPĒKU (N), nevis SPRIEGUMU (MPa)
from structuralcodes.codes.mc2010 import v_rdc_punching

# Nepareiza izmantošana:
v_rdc = v_rdc_punching(d_eff=200, ...)  # Atgriež N, nevis MPa

# Pareiza pieeja:
k_psi_val = k_psi(psi=rotation)
v_rdc = k_psi_val * math.sqrt(fck) / gamma_c  # MPa
```

### Rezultāts
```
EC2 v_Rd,c = 0.849 MPa
MC2010 v_Rd,c = 0.679 MPa (-20%)
```

### Mācība
AI spēja:
1. Identificēt kļūdu (vienību nesaderība)
2. Izpētīt bibliotēkas dokumentāciju
3. Piedāvāt pareizo risinājumu

---

## Piemērs 3: Railway Deployment Problēma

### Problēma
Pēc Railway redeploy, `design.kforma.lv` parādīja "Bad Gateway" kļūdu.

### Diagnostikas Process

**1. Solis: Lokālā testēšana**
```bash
curl http://localhost:5000/
# HTTP 200 OK - lokāli strādā
```

**2. Solis: Cloudflare pārbaude**
```bash
# Citi servisi caur to pašu tuneli strādā
# Problēma nav Cloudflare pusē
```

**3. Solis: Railway URL pārbaude**
```bash
curl https://q6i6uzph.up.railway.app/
# "Not found" - vecais URL vairs nestrādā!
```

### AI Atklājums

Claude Code identificēja divus jautājumus:

**Problēma A:** Railway URL bija mainījies
```
Vecais: q6i6uzph.up.railway.app
Jaunais: web-production-36380.up.railway.app
```

**Problēma B:** `app.py` hardkodēja portu
```python
# Nepareizi:
app.run(port=5000)

# Pareizi:
port = int(os.environ.get('PORT', 5000))
app.run(port=port)
```

### Risinājums
```python
# app.py - 2 rindu labojums
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```

### Rezultāts
- Problēma atrisināta 15 minūtēs
- Dokumentācija atjaunināta nākotnes novēršanai

---

## Piemērs 4: Papildus Stiegrojuma Funkcionalitāte

### Uzdevums
Pievienot iespēju ievadīt divus dažādus stiegrojuma tīklus caurspiešanas aprēķinā:
- Pamata tīkls (visa plātne)
- Papildus tīkls (virs kolonnas)

### AI Risinājums

**Frontend (HTML):**
```html
<div class="form-check">
    <input type="checkbox" id="use_additional_rebar"
           onchange="toggleAdditionalRebar()">
    <label>Papildus siets virs kolonnas</label>
</div>

<div id="additional_rebar_inputs" style="display: none;">
    <input name="phi_y2" placeholder="Y virziena diametrs">
    <input name="s_y2" placeholder="Y virziena solis">
    <!-- ... -->
</div>
```

**Backend (Python):**
```python
# routes/punching.py
use_additional = form_data.get('use_additional_rebar') == 'on'

if use_additional:
    phi_y2 = float(form_data.get('phi_y2', 0))
    As_y2 = math.pi * (phi_y2/2)**2
    As_y_per_m += As_y2 * (1000 / s_y2)

# Kombinētais ρl aprēķins
rho_l = (As_y_per_m + As_z_per_m) / (2 * 1000 * d_approx)
```

### Rezultāts
- Pilnīga funkcionalitāte 1 sesijā
- HTML, JavaScript, un Python sinhronizēti

---

## AI Izmantošanas Statistika

### Laika Ietaupījums
| Uzdevums | Tradicionāli | Ar AI |
|----------|--------------|-------|
| SVG vizualizācija | 4-6 h | 30 min |
| MC2010 integrācija | 2-3 h | 20 min |
| Deployment fix | 1-2 h | 15 min |
| Jauna funkcionalitāte | 2-4 h | 45 min |

### Koda Kvalitāte
- Konsekventas nosaukumu konvencijas
- Automātiski komentāri sarežģītam kodam
- Kļūdu apstrāde iekļauta pēc noklusējuma

---

## Efektīvas AI Izmantošanas Principi

### 1. Skaidrs Uzdevuma Formulējums
```
❌ "Uztaisi vizualizāciju"
✓ "Izveido SVG plānskatu ar kolonnu centrā, kritisko perimetru u₁
   attālumā 2d no kolonnas malas, un stiegrojuma simboliem"
```

### 2. Iteratīva Pieeja
```
1. Pamata funkcionalitāte
2. Vizuālā uzlabošana
3. Kļūdu apstrāde
4. Edge cases
```

### 3. Konteksta Nodrošināšana
```
❌ "Labo kļūdu"
✓ "Funkcija atgriež 271562 MPa, bet jābūt ~0.5-1.5 MPa.
   Domāju, ka problēma ir vienību konversijā."
```

### 4. Koda Review
- Vienmēr pārskatīt AI ģenerēto kodu
- Testēt ar reāliem datiem
- Validēt pret standartiem

---

## Secinājumi

### AI Priekšrocības Inženiertehniskā Izstrādē

1. **Ātrums** - Sarežģītas funkcijas stundās
2. **Konsistence** - Vienota koda kvalitāte
3. **Debugging** - Efektīva problēmu diagnostika
4. **Mācīšanās** - AI var izpētīt jaunas bibliotēkas

### Ierobežojumi

1. **Validācija nepieciešama** - AI var kļūdīties aprēķinos
2. **Konteksts jānodrošina** - Labāki rezultāti ar detalizētiem uzdevumiem
3. **Inženiera zināšanas** - Nepieciešamas rezultātu verificēšanai

### Ieteikumi

- Izmantot AI kā **palīgu**, nevis **aizstājēju**
- Vienmēr **testēt** ģenerēto kodu
- **Dokumentēt** AI sesijas nākotnes uzziņai
- **Iterēt** - sadalīt lielus uzdevumus mazākos

---

*Dokuments izveidots: 2026-02-12*
*Autors: RC Design Web Team*
