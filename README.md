# chemhelper

[![PyPI](https://img.shields.io/pypi/v/chemhelper)](https://pypi.org/project/chemhelper/)
[![CI](https://github.com/drosenman/chemhelper/actions/workflows/ci.yml/badge.svg)](https://github.com/drosenman/chemhelper/actions/workflows/ci.yml)
[![Docs](https://github.com/drosenman/chemhelper/actions/workflows/docs.yml/badge.svg)](https://drosenman.github.io/chemhelper/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**General chemistry answers in one line of Python, and the worked solution in
one more.**

chemhelper solves the problems that fill a first-year chemistry course: molar
mass, percent composition, converting between grams, moles and molarity, and
the ideal gas law. Every solver has a twin ending in `_steps` that prints the
solution the way you would write it on a whiteboard.

It was written by a chemistry tutor, for tutoring: check a student's answer
in a second, show where it came from, and spend the session on understanding.

**Status:** actively developed. Version 1.0 is a full overhaul of the
original 2017 package, and more is planned. See the
[roadmap](https://drosenman.github.io/chemhelper/project/roadmap/).

### 📖 Full documentation: **https://drosenman.github.io/chemhelper/**

---

## Contents

- [Install](#install)
- [A two-minute tour](#a-two-minute-tour)
- [Everything it can do](#everything-it-can-do)
- [Writing formulas](#writing-formulas)
- [Units and rounding](#units-and-rounding)
- [Documentation](#documentation)
- [Development](#development)
- [License](#license)

## Install

```bash
pip install chemhelper
```

Version 1.0 requires Python 3.10 or newer and installs pandas with it. Until
1.0 is on PyPI, install it from GitHub:

```bash
pip install git+https://github.com/drosenman/chemhelper.git
```

## A two-minute tour

```pycon
>>> from chemhelper import elements, compounds, conversions, ideal_gas
```

### Get an answer

```pycon
>>> compounds.mass('Ca(OH)2')
74.1
>>> conversions.grams_to_moles(90.1, 'H2O')
5.0
>>> ideal_gas.ideal_gas('P', V=5, n=4, T=300)
19.7
```

### Show the work

Add `_steps` to any solver's name.

```pycon
>>> compounds.mass_steps('Al2(SO4)3')
Al2(SO4)3
Al: 2 x 26.98 = 53.96
S: 3 x 32.07 = 96.21
O: 12 x 16.0 = 192.0

Mass Al2(SO4)3 = 53.96 + 96.21 + 192.0 = 342.17
```

### Look up an element

```pycon
>>> print(elements.Fe)
Element: Iron, Fe
Atomic Number: 26
Mass: 55.85
>>> elements.element_table.head()
Atomic Number Symbol       Name   Mass
1                  H   Hydrogen   1.01
2                 He     Helium   4.00
3                 Li    Lithium   6.94
4                 Be  Beryllium   9.01
5                  B      Boron  10.81
```

### Percent composition

```pycon
>>> compounds.percent_composition('C6H12O6')
C          39.999
H           6.714
O          53.287
Total:    100.000
Name: C6H12O6, dtype: float64
>>> compounds.percent_composition_steps('H2O')
H2O
H: 2 x 1.008 = 2.016
O: 16.0

Mass H2O = 2.016 + 16.0 = 18.02

H          2.016
O         16.000
Total:    18.020
Name: H2O, dtype: float64
H: 100 x 2.016g H/18.02g H2O = 11.19%
O: 100 x 16.0g O/18.02g H2O = 88.81%
```

### Solutions

How many grams of NaCl are needed for 2 L of a 0.5 M solution?

```pycon
>>> conversions.molarity_to_grams(0.5, 2, 'NaCl')
58.44
>>> conversions.molarity_to_grams_steps(0.5, 2, 'NaCl')
0.5 moles/L x 2 L = 1 moles
NaCl
Na: 22.99
Cl: 35.45

Mass NaCl = 22.99 + 35.45 = 58.44
1 moles x 58.44 grams/mole = 58.44 grams
```

What is the molarity of 10 g of NaOH in 0.25 L of solution?

```pycon
>>> conversions.molarity_steps(0.25, mass=10, chemical='NaOH')
10g NaOH x 1 mole NaOH/40.0g NaOH = 0.25 moles NaOH
0.25 moles/0.25 L = 1 M
```

### The ideal gas law

Solve for any variable. Give a mass in place of moles, and use the units the
problem gives you.

```pycon
>>> ideal_gas.ideal_gas_steps('P', substance='O2', m=32, V=500, Vunits='mL', T=25, Tunits='C')
n = 32g x 1 mole O2/32.0g O2 = 1 moles O2
V = 500 mL x 1 L/1000 mL = 0.5 L
T = (25 + 273.15) K = 298.15 K
PV = nRT
P = nRT/V
P = 1 moles x 0.0821 L*atm/(mol*K) x 298.15 K / 0.5 L = 48.96 atm
```

### Helpful errors

```pycon
>>> compounds.mass('NACL')
Traceback (most recent call last):
  ...
ValueError: Unknown element 'A' in formula 'NACL'
>>> ideal_gas.ideal_gas('P', V=5, T=300)
Traceback (most recent call last):
  ...
ValueError: Missing value(s) for: n
```

## Everything it can do

Every function below, except `parse_formula`, has a `_steps` twin that takes
the same arguments and prints the worked solution.

### `chemhelper.elements`

| Name | Description |
| --- | --- |
| `Element` | Class holding `symbol`, `name`, `atomic_number` and `mass` |
| `H`, `He`, … `U` | One `Element` per element, named by symbol |
| `elements` | pandas Series of `Element` objects, indexed by symbol |
| `element_index` | Symbols in order of atomic number |
| `element_objects` | `Element` objects in order of atomic number |
| `element_table` | pandas DataFrame of symbol, name and mass |

### `chemhelper.compounds`

| Function | Returns |
| --- | --- |
| `parse_formula(chemical)` | Atom counts for each element |
| `mass(chemical)` | Molar mass in g/mol |
| `composition(chemical)` | Grams of each element per mole of compound |
| `percent_composition(chemical)` | Percent by mass of each element |

### `chemhelper.conversions`

| Function | Returns |
| --- | --- |
| `grams_to_moles(mass, chemical)` | Moles |
| `moles_to_grams(moles, chemical)` | Grams |
| `molarity(volume, mass=None, chemical=None, moles=None)` | Molarity, from moles or from a mass |
| `molarity_to_moles(M, volume)` | Moles of solute |
| `molarity_to_grams(molarity, volume, chemical)` | Grams of solute |

### `chemhelper.ideal_gas`

| Function | Returns |
| --- | --- |
| `ideal_gas(solve_for, substance=None, P=None, V=None, n=None, T=None, m=None, decimals=2, Tunits='K', Vunits='L', Punits='atm')` | P in atm, V in L, n in mol or T in K |

`solve_for` is `'P'`, `'V'`, `'n'` or `'T'`. Inputs may be given in torr,
mmHg, kPa, mL or °C with `Punits`, `Vunits` and `Tunits`.

## Writing formulas

Formulas are strings, written as in a textbook.

| Rule | Example |
| --- | --- |
| Symbols are case-sensitive | `'Co'` is cobalt, `'CO'` is carbon monoxide |
| A number after a symbol is its count | `'C6H12O6'` |
| Groups go in parentheses or brackets | `'Ca(OH)2'`, `'K4[Fe(CN)6]'` |
| Repeated elements are added together | `'CH3COOH'` is C₂H₄O₂ |
| Hydrates use parentheses, not a dot | `'CuSO4(H2O)5'` |

Elements 1 to 92 (H to U) are supported.

```pycon
>>> dict(compounds.parse_formula('K4[Fe(CN)6]'))
{'K': 4, 'Fe': 1, 'C': 6, 'N': 6}
```

## Units and rounding

| Quantity | Unit |
| --- | --- |
| Mass | grams |
| Amount | moles |
| Volume | liters (`ideal_gas` also accepts mL) |
| Concentration | mol/L |
| Pressure | atm (`ideal_gas` also accepts torr, mmHg, kPa) |
| Temperature | kelvin (`ideal_gas` also accepts °C) |

Results are rounded for display, most to two decimals. Intermediate steps
keep full precision. `ideal_gas` uses R = 0.0821 L·atm/(mol·K) and takes a
`decimals` argument.

## Documentation

The [documentation site](https://drosenman.github.io/chemhelper/) covers
everything in depth:

| Section | What's there |
| --- | --- |
| [Getting started](https://drosenman.github.io/chemhelper/getting-started/installation/) | Installation, quickstart, formula rules, units and rounding |
| [User guide](https://drosenman.github.io/chemhelper/guide/) | Every function with arguments, formulas, errors and examples |
| [Tutorials](https://drosenman.github.io/chemhelper/tutorials/) | A tutoring session, preparing solutions, gas law problems |
| [Cookbook](https://drosenman.github.io/chemhelper/cookbook/) | Short recipes: hydrates, limiting reagent, dilution, gas density and more |
| [Periodic table](https://drosenman.github.io/chemhelper/periodic-table/) | The atomic masses chemhelper uses |
| [API reference](https://drosenman.github.io/chemhelper/reference/compounds/) | Generated from the docstrings |
| [Migrating from 0.4](https://drosenman.github.io/chemhelper/project/migrating/) | What changed in 1.0 |

## Development

```bash
git clone https://github.com/drosenman/chemhelper.git
cd chemhelper
pip install -e ".[test,docs]"
```

| Task | Command |
| --- | --- |
| Run the tests | `pytest` |
| Check every example in the docs and this README | `python tools/docs_examples.py` |
| Regenerate example output | `python tools/docs_examples.py --write` |
| Preview the docs | `mkdocs serve` |

Bug reports, corrections and new solvers are welcome. See
[Contributing](https://drosenman.github.io/chemhelper/project/contributing/)
and the [changelog](CHANGELOG.md).

## License

[MIT](LICENSE) © Dave Rosenman
