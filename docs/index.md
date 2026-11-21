# chemhelper

**chemhelper** solves introductory chemistry problems — molar mass, percent
composition, gram/mole/molarity conversions and the ideal gas law — and shows
its work.

Every solver has a twin ending in `_steps` that prints the worked solution,
so you can check an answer *and* show how it was reached. It was written for
tutoring: check a student's work quickly, then spend the session on
understanding.

```python
>>> from chemhelper import compounds
>>> compounds.mass('Ca(OH)2')
74.1
>>> compounds.mass_steps('H2O')
H2O
H: 2 x 1.008 = 2.016
O: 16.0

Mass H2O = 2.016 + 16.0 = 18.02
```

## Modules

| Module | What it does |
| --- | --- |
| [`elements`](reference/elements.md) | Periodic table data for elements 1–92 |
| [`compounds`](reference/compounds.md) | Formula parsing, molar mass, composition, percent composition |
| [`conversions`](reference/conversions.md) | Grams ↔ moles, molarity |
| [`ideal_gas`](reference/ideal_gas.md) | Solve PV = nRT for any variable, with unit conversion |

Start with [Getting started](getting-started.md).
