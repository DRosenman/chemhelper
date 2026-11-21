# chemhelper

[![PyPI](https://img.shields.io/pypi/v/chemhelper)](https://pypi.org/project/chemhelper/)
[![CI](https://github.com/drosenman/chemhelper/actions/workflows/ci.yml/badge.svg)](https://github.com/drosenman/chemhelper/actions/workflows/ci.yml)

Solve introductory chemistry problems — molar mass, percent composition,
gram/mole/molarity conversions and the ideal gas law — **and show the work**.
Every solver has a `_steps` twin that prints a step-by-step solution, which
makes it handy for tutoring: check a student's answer, then walk through it.

**Documentation:** https://drosenman.github.io/chemhelper/

## Install

```bash
pip install chemhelper
```

Requires Python 3.9+ and pandas.

## Quick start

```python
>>> from chemhelper import compounds, conversions, ideal_gas

>>> compounds.mass('Ca(OH)2')
74.1

>>> compounds.mass_steps('H2O')
H2O
H: 2 x 1.008 = 2.016
O: 16.0

Mass H2O = 2.016 + 16.0 = 18.02

>>> conversions.molarity_to_grams(0.5, 2, 'NaCl')   # 2 L of 0.5 M NaCl
58.44

>>> ideal_gas.ideal_gas('V', n=1, T=0, Tunits='C', P=1)
22.43
```

## Modules

| Module | What it does |
| --- | --- |
| `chemhelper.elements` | Periodic table data for elements 1–92 |
| `chemhelper.compounds` | Formula parsing, molar mass, composition, percent composition |
| `chemhelper.conversions` | Grams ↔ moles, molarity |
| `chemhelper.ideal_gas` | Solve PV = nRT for P, V, n or T, with unit conversion |

See the [documentation](https://drosenman.github.io/chemhelper/) for the full
API and worked examples, and [CHANGELOG.md](CHANGELOG.md) for what changed in 1.0.

## Development

```bash
pip install -e ".[test,docs]"
pytest
mkdocs serve
```

## License

MIT
