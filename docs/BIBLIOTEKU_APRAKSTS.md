# Python Bibliotēkas Būvkonstrukciju Aprēķiniem

## Pārskats

Šis dokuments apraksta galvenās Python bibliotēkas, kas tiek izmantotas RC Design Web platformā. Bibliotēkas ir sadalītas kategorijās pēc to pielietojuma.

---

## 1. Skaitliskās Aprēķinu Bibliotēkas

### NumPy
**Mērķis:** Matricu un masīvu operācijas

```python
import numpy as np

# Spriegumu sadalījuma aprēķins
sigma = np.array([sigma_top, sigma_bottom])
eps = sigma / E  # Elementwise dalīšana

# Matricu inversija FEM aprēķiniem
K_inv = np.linalg.inv(stiffness_matrix)
```

**Pielietojumi projektā:**
- Stresa-deformācijas aprēķini
- FEM stinguma matricu operācijas
- Šķērsgriezumu īpašību aprēķini

### SciPy
**Mērķis:** Zinātniskās skaitļošanas rīki

```python
from scipy.optimize import brentq
from scipy.integrate import quad

# Neitrālās ass atrašana ar Brent metodi
def find_neutral_axis(x_na):
    return compression_force(x_na) - tension_force(x_na)

x_solution = brentq(find_neutral_axis, 0, h)
```

**Pielietojumi projektā:**
- Nelineāro vienādojumu risināšana
- Integrācija šķērsgriezumu analīzē
- Interpolācijas funkcijas

---

## 2. Vizualizācijas Bibliotēkas

### Matplotlib
**Mērķis:** 2D un 3D grafiku veidošana

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# M-N diagrammas izveide
fig, ax = plt.subplots()
ax.plot(M_values, N_values, 'b-', linewidth=2)
ax.fill(M_values, N_values, alpha=0.3)
ax.set_xlabel('Moments M (kNm)')
ax.set_ylabel('Normālspēks N (kN)')
```

**Pielietojumi projektā:**
- M-N mijiedarbības diagrammas (kolonnas)
- Šķērsgriezumu vizualizācijas
- Spriegumu epīras
- Vēja spiediena 3D virsmas

### Base64 Encoding (attēlu embed)
```python
import io
import base64

# Matplotlib attēla konvertēšana HTML embed
buffer = io.BytesIO()
plt.savefig(buffer, format='png', dpi=150)
buffer.seek(0)
image_base64 = base64.b64encode(buffer.read()).decode()
img_tag = f'<img src="data:image/png;base64,{image_base64}">'
```

---

## 3. Konstrukciju Analīzes Bibliotēkas

### concreteproperties
**Mērķis:** Dzelzsbetona šķērsgriezumu analīze

```python
from concreteproperties.material import Concrete, SteelBar
from concreteproperties.geometry import ConcreteSection
from concreteproperties.analysis import ConcreteAnalysis

# Šķērsgriezuma definēšana
concrete = Concrete(
    name="C30/37",
    density=2500,
    stress_strain_profile=ConcreteLinear(elastic_modulus=33000),
    compressive_strength=30,
    tensile_strength=2.9
)

# M-N diagrammas aprēķins
analysis = ConcreteAnalysis(section)
diagram = analysis.moment_interaction_diagram()
```

**Pielietojumi projektā:**
- Kolonnu M-N diagrammas
- Šķērsgriezumu kapacitātes
- Spriegumu sadalījums

### sectionproperties
**Mērķis:** Šķērsgriezumu ģeometriskās īpašības

```python
from sectionproperties.pre.geometry import Geometry
from sectionproperties.analysis.section import Section

# HCS (Hollowcore) šķērsgriezuma analīze
geometry = Geometry.from_dxf("hollowcore.dxf")
section = Section(geometry)
section.calculate_geometric_properties()

print(f"Inerces moments: {section.ixx:.2e} mm4")
print(f"Pretestības moments: {section.zxx:.2e} mm3")
```

**Pielietojumi projektā:**
- Dobo plātņu (HCS) analīze
- Kompleksu šķērsgriezumu īpašības
- Efektīvā šķērsgriezuma aprēķins

### structuralcodes
**Mērķis:** Eirokodeksu formulu implementācija

```python
from structuralcodes.codes.ec2_2004 import (
    v_rdc_punching,
    v_rdmax_punching,
    k_factor
)
from structuralcodes.codes.mc2010 import (
    k_psi,
    v_rdc_punching as mc2010_v_rdc
)

# EC2 caurspiešanas izturība
v_rd_c = v_rdc_punching(
    approx_lvl=1,
    d_eff=200,
    f_ck=30,
    rho_l=0.015,
    gamma_c=1.5
)

# MC2010 salīdzinājums
k_psi_val = k_psi(psi=0.015)  # rotācija
v_rd_mc2010 = mc2010_v_rdc(k_psi_val, fck=30, gamma_c=1.5)
```

**Pielietojumi projektā:**
- Formulu validācija pret standartiem
- MC2010 salīdzinājumi
- Parametru aprēķini

---

## 4. FEM (Finite Element Method) Bibliotēkas

### gmsh
**Mērķis:** Galīgo elementu režģa ģenerēšana

```python
import gmsh

gmsh.initialize()
gmsh.model.add("pilecap")

# Ģeometrijas izveide
p1 = gmsh.model.geo.addPoint(0, 0, 0)
p2 = gmsh.model.geo.addPoint(2000, 0, 0)
# ... citi punkti

# Virsmas izveide
surface = gmsh.model.geo.addPlaneSurface([loop])

# Režģa ģenerēšana
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)

# Režģa eksports
gmsh.write("pilecap.msh")
gmsh.finalize()
```

**Pielietojumi projektā:**
- Pāļu rostu režģi
- Finplate FEM analīze
- 3D spriegumu analīze

### scikit-fem
**Mērķis:** FEM risinātājs Python vidē

```python
from skfem import *
from skfem.models.poisson import laplace

# Režģa ielāde
mesh = MeshTri.load("pilecap.msh")

# Elementa definēšana
element = ElementTriP1()
basis = Basis(mesh, element)

# Stinguma matricas montāža
@bilinear_form
def stiffness(u, v, w):
    return sum(u.grad * v.grad)

K = stiffness.assemble(basis)

# Sistēmas risināšana
u = solve(K, f)
```

**Pielietojumi projektā:**
- Plātņu un rostu analīze
- Spriegumu sadalījuma vizualizācija
- Savienojumu FEM verificēšana

---

## 5. Web Framework Bibliotēkas

### Flask
**Mērķis:** Web aplikācijas pamatstruktūra

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/punching/calculate', methods=['POST'])
def calculate_punching():
    # Ievaddatu apstrāde
    VEd = float(request.form.get('VEd', 500))
    concrete = request.form.get('concrete', 'C30/37')

    # Aprēķins
    results = calculate_punching_shear(VEd, concrete)

    # Rezultātu attēlošana
    return render_template('punching.html', results=results)
```

### Jinja2
**Mērķis:** HTML templating

```html
<!-- templates/modules/punching.html -->
{% extends "base.html" %}

{% block content %}
<h2>Caurspiešanas Aprēķins</h2>

{% if results %}
<div class="results-card {% if results.status == 'OK' %}success{% else %}danger{% endif %}">
    <h3>v<sub>Ed</sub> / v<sub>Rd,c</sub> = {{ "%.2f"|format(results.ratio1) }}</h3>
    {% if results.ratio1 <= 1.0 %}
        <span class="badge bg-success">Izpildās</span>
    {% else %}
        <span class="badge bg-danger">Neizpildās</span>
    {% endif %}
</div>
{% endif %}
{% endblock %}
```

### Flask-Login
**Mērķis:** Lietotāju autentifikācija

```python
from flask_login import login_required, current_user

@app.route('/dashboard')
@login_required
def dashboard():
    calculations = SavedCalculation.query.filter_by(
        user_id=current_user.id
    ).all()
    return render_template('dashboard.html', calculations=calculations)
```

### SQLAlchemy
**Mērķis:** Datubāzes ORM

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SavedCalculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    module = db.Column(db.String(50))
    data = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

---

## 6. Matemātikas Bibliotēkas

### math (standarta bibliotēka)
**Mērķis:** Pamata matemātiskās funkcijas

```python
import math

# Stiegrojuma laukuma aprēķins
As = math.pi * (phi / 2) ** 2  # mm²

# Aprēķina formulas
k = min(1 + math.sqrt(200 / d), 2.0)  # EC2 k faktors
rho_l = min(math.sqrt(rho_lx * rho_ly), 0.02)  # ρl ierobežojums
```

---

## Bibliotēku Instalācija

### requirements.txt
```
flask>=2.0
flask-login>=0.6
flask-sqlalchemy>=3.0
numpy>=1.21
scipy>=1.7
matplotlib>=3.5
concreteproperties>=0.5
sectionproperties>=2.1
structuralcodes>=0.1
gmsh>=4.10
scikit-fem>=7.0
gunicorn>=20.1
```

### Instalācijas komanda
```bash
pip install -r requirements.txt
```

---

## Bibliotēku Salīdzinājums ar Alternatīvām

| Bibliotēka | Alternatīva | Priekšrocības |
|------------|-------------|---------------|
| NumPy | MATLAB | Bezmaksas, Python integrācija |
| Matplotlib | Excel charts | Pilna kontrole, automatizācija |
| concreteproperties | IDEA StatiCa | Open-source, pielāgojams |
| gmsh | ANSYS Mesh | Bezmaksas, Python API |
| scikit-fem | ANSYS/Abaqus | Viegls, Python integrācija |
| structuralcodes | Manuāla kodēšana | Validētas formulas |

---

## Secinājumi

Python bibliotēku ekosistēma nodrošina:

1. **Uzticamību** - Validētas formulas no structuralcodes
2. **Vizualizāciju** - Profesionāla grafika ar matplotlib
3. **FEM iespējas** - Sarežģītu problēmu risināšana
4. **Automatizāciju** - Atkārtojami aprēķini
5. **Elastību** - Pielāgojami moduļi

Visas bibliotēkas ir **open-source** un **bezmaksas lietošanai**.

---

*Dokuments izveidots: 2026-02-12*
*Autors: RC Design Web Team*
