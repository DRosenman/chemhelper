# Getting started

## Install

```bash
pip install chemhelper
```

chemhelper needs Python 3.9 or newer and pandas.

## Import

```python
from chemhelper import elements, compounds, conversions, ideal_gas
```

## Writing formulas

Formulas are case-sensitive, as on paper: `NaCl`, `C6H12O6`, `CH3COOH`.
Groups go in parentheses or square brackets and can be nested:
`Ca(OH)2`, `Al2(SO4)3`, `K4[Fe(CN)6]`. An element that appears more than once
is counted together, so `CH3COOH` is treated as C2H4O2.

A misspelled formula raises `ValueError` and says what's wrong:

```python
>>> compounds.mass('Xy2')
ValueError: Unknown element 'Xy' in formula 'Xy2'
```

## Answers vs. worked solutions

Each solver returns a number (or a pandas Series). Its `_steps` twin prints
the solution instead and returns nothing:

```python
>>> conversions.grams_to_moles(36.04, 'H2O')
2.0
>>> conversions.grams_to_moles_steps(36.04, 'H2O')
36.04g H2O x 1 mole H2O/18.02g H2O = 2.0 moles H2O
```

## Rounding

Results are rounded for display — molar masses and most conversions to 2
decimals, percent composition to 3 — but intermediate steps are carried at
full precision. `ideal_gas` takes a `decimals` argument.

## Units

| Quantity | Units |
| --- | --- |
| Mass | grams |
| Amount | moles |
| Volume | liters (`ideal_gas` also accepts `Vunits='mL'`) |
| Pressure | atm (`ideal_gas` also accepts `'torr'`, `'mmHg'`, `'kPa'`) |
| Temperature | kelvin (`ideal_gas` also accepts `Tunits='C'`) |

The gas constant is R = 0.0821 L·atm/(mol·K), the value most textbooks use.
