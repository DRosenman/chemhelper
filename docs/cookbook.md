# Cookbook

Short recipes for single tasks. Each one stands alone, given these imports:

```pycon
>>> from chemhelper import elements, compounds, conversions, ideal_gas
```

## Formulas and molar mass

### Molar masses for a list of compounds

```pycon
>>> formulas = ['H2O', 'CO2', 'NaCl', 'C6H12O6', 'Ca(OH)2']
>>> {f: compounds.mass(f) for f in formulas}
{'H2O': 18.02, 'CO2': 44.01, 'NaCl': 58.44, 'C6H12O6': 180.16, 'Ca(OH)2': 74.1}
```

As a table, sorted from heaviest to lightest:

```pycon
>>> import pandas as pd
>>> table = pd.Series({f: compounds.mass(f) for f in formulas}, name='g/mol')
>>> table.sort_values(ascending=False)
C6H12O6    180.16
Ca(OH)2     74.10
NaCl        58.44
CO2         44.01
H2O         18.02
Name: g/mol, dtype: float64
```

### Count the atoms in a formula

```pycon
>>> counts = compounds.parse_formula('Ca3(PO4)2')
>>> dict(counts)
{'Ca': 3, 'P': 2, 'O': 8}
>>> sum(counts.values())
13
```

### Check that a formula is valid

```pycon
>>> def is_valid(formula):
...     try:
...         compounds.parse_formula(formula)
...         return True
...     except ValueError:
...         return False
>>> [is_valid(f) for f in ['H2O', 'h2o', 'Ca(OH)2', 'Ca(OH2']]
[True, False, True, False]
```

### Molar mass of a hydrate

Write the water of hydration in parentheses. Copper(II) sulfate pentahydrate,
CuSO₄·5H₂O:

```pycon
>>> compounds.mass('CuSO4(H2O)5')
249.7
```

### Percent water in a hydrate

Divide the mass of the water by the mass of the whole hydrate:

```pycon
>>> round(5 * compounds.mass('H2O') / compounds.mass('CuSO4(H2O)5') * 100, 2)
36.08
```

### Compare an element's share across compounds

Which iron ore is richest in iron?

```pycon
>>> for ore in ['Fe2O3', 'Fe3O4', 'FeCO3', 'FeS2']:
...     print(ore, float(compounds.percent_composition(ore)['Fe']))
Fe2O3 69.944
Fe3O4 72.36
FeCO3 48.205
FeS2 46.546
```

### Check an empirical formula against percent composition

> A compound is 40.0 % C, 6.7 % H and 53.3 % O. Is CH₂O a possible empirical
> formula?

```pycon
>>> compounds.percent_composition('CH2O')
C          39.999
H           6.714
O          53.287
Total:    100.000
Name: CH2O, dtype: float64
```

The percentages match. Glucose, C₆H₁₂O₆, has the same empirical formula and
so the same percent composition:

```pycon
>>> compounds.percent_composition('C6H12O6')
C          39.999
H           6.714
O          53.287
Total:    100.000
Name: C6H12O6, dtype: float64
```

### Find the molecular formula from a molar mass

> The empirical formula is CH₂O and the molar mass is about 180 g/mol.

```pycon
>>> round(180 / compounds.mass('CH2O'))
6
```

The molecular formula is six empirical units: C₆H₁₂O₆.

## Moles, molecules and mass

### Number of molecules in a sample

Multiply moles by Avogadro's number. chemhelper does not define the constant,
so write it in:

```pycon
>>> AVOGADRO = 6.022e23
>>> moles = conversions.grams_to_moles(18.02, 'H2O')
>>> moles * AVOGADRO
6.022e+23
```

### Mass of a single molecule, in grams

```pycon
>>> '{:.3e}'.format(compounds.mass('H2O') / 6.022e23)
'2.992e-23'
```

### Grams of an element in a sample of a compound

> How many grams of iron are in 250 g of Fe₂O₃?

```pycon
>>> fraction = float(compounds.percent_composition('Fe2O3')['Fe']) / 100
>>> round(250 * fraction, 1)
174.9
```

### Grams of product from grams of reactant

> N₂ + 3 H₂ → 2 NH₃. How many grams of ammonia form from 56.0 g of N₂?

```pycon
>>> moles_n2 = conversions.grams_to_moles(56.0, 'N2')
>>> moles_nh3 = moles_n2 * 2 / 1
>>> conversions.moles_to_grams(moles_nh3, 'NH3')
68.12
```

The `2 / 1` is the mole ratio of NH₃ to N₂ from the balanced equation.

### Find the limiting reagent

> 2 H₂ + O₂ → 2 H₂O. You have 10.0 g of H₂ and 64.0 g of O₂.

Divide each reactant's moles by its coefficient. The smallest result is the
limiting reagent.

```pycon
>>> h2 = conversions.grams_to_moles(10.0, 'H2') / 2
>>> o2 = conversions.grams_to_moles(64.0, 'O2') / 1
>>> h2, o2
(2.475, 2.0)
>>> 'H2' if h2 < o2 else 'O2'
'O2'
```

Water formed, from the limiting reagent:

```pycon
>>> conversions.moles_to_grams(o2 * 2, 'H2O')
72.08
```

### Percent yield

> The theoretical yield is 72.08 g and you collected 61.3 g.

```pycon
>>> round(61.3 / 72.08 * 100, 1)
85.0
```

## Solutions

### Molarity from milliliters

```pycon
>>> conversions.molarity(250 / 1000, mass=10, chemical='NaOH')
1.0
```

### Grams needed for a list of concentrations

```pycon
>>> for M in [0.1, 0.25, 0.5, 1.0]:
...     print(M, 'M:', conversions.molarity_to_grams(M, 0.500, 'NaCl'), 'g')
0.1 M: 2.92 g
0.25 M: 7.3 g
0.5 M: 14.61 g
1.0 M: 29.22 g
```

### Dilution

> 25.0 mL of 6.0 M acid diluted to 500 mL.

```pycon
>>> round(conversions.molarity(0.500, moles=conversions.molarity_to_moles(6.0, 0.0250)), 3)
0.3
```

### Concentration in grams per liter

```pycon
>>> conversions.molarity_to_grams(0.15, 1, 'NaCl')
8.77
```

## Gases

### Molar volume at a given temperature and pressure

```pycon
>>> ideal_gas.ideal_gas('V', n=1, P=1, T=25, Tunits='C')
24.48
```

### Density of a gas

Density is the mass of one mole divided by the volume of one mole.

```pycon
>>> molar_volume = ideal_gas.ideal_gas('V', n=1, P=1, T=25, Tunits='C', decimals=4)
>>> round(compounds.mass('CO2') / molar_volume, 3)
1.798
```

That is in grams per liter.

### Pressure in other units

```pycon
>>> p = ideal_gas.ideal_gas('P', n=0.5, V=10, T=300)
>>> {'atm': p, 'torr': round(p * 760, 1), 'kPa': round(p * 101.325, 1)}
{'atm': 1.23, 'torr': 934.8, 'kPa': 124.6}
```

### Volume across a range of temperatures

```pycon
>>> for celsius in [0, 25, 50, 100]:
...     print(celsius, 'C:', ideal_gas.ideal_gas('V', n=1, P=1, T=celsius, Tunits='C'), 'L')
0 C: 22.43 L
25 C: 24.48 L
50 C: 26.53 L
100 C: 30.64 L
```

## The periodic table

### Look up an element by name

```pycon
>>> table = elements.element_table
>>> table[table['Name'] == 'Tungsten']
Atomic Number Symbol      Name    Mass
74                 W  Tungsten  183.84
```

### Atomic number from a symbol

```pycon
>>> elements.elements['W'].atomic_number
74
```

### The lightest and heaviest elements in a formula

```pycon
>>> symbols = list(compounds.parse_formula('K4[Fe(CN)6]'))
>>> masses = {s: elements.elements[s].mass for s in symbols}
>>> min(masses, key=masses.get), max(masses, key=masses.get)
('C', 'Fe')
```

### Elements in a mass range

```pycon
>>> table[(table['Mass'] > 50) & (table['Mass'] < 60)]
Atomic Number Symbol       Name   Mass
23                 V   Vanadium  50.94
24                Cr   Chromium  52.00
25                Mn  Manganese  54.94
26                Fe       Iron  55.85
27                Co     Cobalt  58.93
28                Ni     Nickel  58.69
```

## Working with the output

### Capture a worked solution as a string

`_steps` functions print. This helper returns what any of them would have
printed:

```pycon
>>> import contextlib, io
>>> def solution_text(steps_function, *args, **kwargs):
...     buffer = io.StringIO()
...     with contextlib.redirect_stdout(buffer):
...         steps_function(*args, **kwargs)
...     return buffer.getvalue()
>>> text = solution_text(compounds.mass_steps, 'NaCl')
>>> print(text)
NaCl
Na: 22.99
Cl: 35.45

Mass NaCl = 22.99 + 35.45 = 58.44
```

### Save a worked solution to a file

```python
with open('solution.txt', 'w') as f:
    f.write(solution_text(conversions.molarity_steps, 0.25, mass=10, chemical='NaOH'))
```

### Build an answer key

```pycon
>>> problems = [('H2O', 36.04), ('NaCl', 100), ('CO2', 22.0)]
>>> for formula, grams in problems:
...     print(formula, grams, 'g =', conversions.grams_to_moles(grams, formula), 'mol')
H2O 36.04 g = 2.0 mol
NaCl 100 g = 1.71 mol
CO2 22.0 g = 0.5 mol
```

### Turn a composition into a plain dictionary

```pycon
>>> compounds.percent_composition('H2O').drop('Total:').to_dict()
{'H': 11.19, 'O': 88.81}
```
