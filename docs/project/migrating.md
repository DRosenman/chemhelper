# Migrating from 0.4

Version 1.0 keeps every function name and every argument from 0.4. Code
written for 0.4 will run. Some of it will give different, more accurate
results, and a few return types changed.

```pycon
>>> from chemhelper import elements, compounds, conversions, ideal_gas
```

## Summary

| Area | 0.4 | 1.0 | Do you need to change code? |
| --- | --- | --- | --- |
| `ideal_gas('T', ...)` | returned a tuple `(T, 2)` | returns a number | Yes, if you unpacked the tuple |
| Celsius conversion | added 273.5 | adds 273.15 | No; results change slightly |
| Intermediate rounding | moles and volumes rounded mid-calculation | only the final result is rounded | No; results change slightly |
| `moles_to_grams` | unrounded | rounded to 2 decimals | Only if you relied on extra digits |
| Repeated elements | listed twice in `composition` | combined | Only if you relied on duplicates |
| Parentheses | ignored, giving wrong masses | supported | No |
| Bad input | `KeyError` or `TypeError` | `ValueError` with a clear message | Yes, if you caught the old exceptions |
| Technetium | symbol stored as `'TC'` | `'Tc'` | No |
| Python | not specified | 3.10 or newer | Upgrade Python if needed |

## Changes in detail

### `ideal_gas` returns a number when solving for temperature

In 0.4, solving for `'T'` returned a two-item tuple by mistake.

```pycon
>>> ideal_gas.ideal_gas('T', P=1, V=12, n=0.5)
292.33
```

If your code did `T, _ = ideal_gas.ideal_gas('T', ...)` or indexed the result
with `[0]`, remove that.

### Celsius is converted correctly

0.4 added 273.5 to Celsius temperatures. 1.0 adds 273.15. Any gas
calculation with `Tunits='C'` changes by about 0.1 %.

### Intermediate values are no longer rounded

0.4 rounded moles to two decimals and converted volumes to two decimals
before using them, which could shift the answer noticeably. A volume of
250 mL was fine, but 125 mL became 0.12 L.

```pycon
>>> ideal_gas.ideal_gas('n', P=1, V=125, Vunits='mL', T=298, decimals=5)
0.00511
```

### `decimals` now works

The `decimals` argument of `ideal_gas` existed in 0.4 but was ignored.

```pycon
>>> ideal_gas.ideal_gas('V', n=1, T=273.15, P=1, decimals=4)
22.4256
```

### Parentheses and brackets are understood

0.4 ignored parentheses, so `'Ca(OH)2'` was read as one Ca, one O and one H,
and the mass was wrong. 1.0 reads groups correctly, including nested ones.

```pycon
>>> compounds.mass('Ca(OH)2')
74.1
>>> compounds.mass('K4[Fe(CN)6]')
368.37
```

!!! warning "Check old results that used parentheses"
    If you used 0.4 with formulas containing parentheses, those molar masses
    were incorrect. Recalculate them.

### Repeated elements are combined

In 0.4, `composition('CH3COOH')` had two `C` rows, two `H` rows and two `O`
rows. 1.0 has one of each.

```pycon
>>> compounds.composition('CH3COOH')
C         24.020
H          4.032
O         32.000
Total:    60.050
Name: CH3COOH, dtype: float64
```

### `moles_to_grams` is rounded

It now rounds to two decimals, like `grams_to_moles` and
`molarity_to_grams`.

```pycon
>>> conversions.moles_to_grams(0.333, 'H2O')
6.0
```

### `molarity` uses unrounded moles

When given a mass, 0.4 rounded the moles to two decimals before dividing by
the volume. 1.0 does not.

```pycon
>>> round(conversions.molarity(1, mass=1.0, chemical='NaCl'), 4)
0.0171
```

In 0.4 this returned 0.02.

### Errors are `ValueError`

Invalid input used to surface as a `KeyError` from pandas or a `TypeError`
from arithmetic on `None`. Now every invalid input raises `ValueError` with a
message describing the problem.

```pycon
>>> compounds.mass('Xy2')
Traceback (most recent call last):
  ...
ValueError: Unknown element 'Xy' in formula 'Xy2'
>>> ideal_gas.ideal_gas('P', V=5, T=300)
Traceback (most recent call last):
  ...
ValueError: Missing value(s) for: n
>>> conversions.molarity(1, mass=10)
Traceback (most recent call last):
  ...
ValueError: Give either moles, or both mass and chemical.
```

If your code has `except KeyError:` around a chemhelper call, change it to
`except ValueError:`.

### Element data corrections

- Technetium's symbol is `'Tc'` (was `'TC'`).
- Beryllium, Holmium and Protactinium are spelled correctly.

```pycon
>>> elements.Tc
Element('Tc', 'Technetium', 43, 98)
```

### Printed solutions changed

The text printed by `_steps` functions was tidied. If you compared printed
output against saved text, update the saved text. The main differences:

- Multiplication is shown with `x` throughout.
- Moles, volumes and molarities are shown to four significant figures. 0.4
  showed two decimals, which turned small amounts into `0.00`.
- `ideal_gas_steps` prints converted values to six significant figures, and
  prints the law before the rearranged form for every
  variable.
- `molarity_to_grams_steps` now starts with the molarity-to-moles line.

## New in 1.0

- [`compounds.parse_formula`](../guide/compounds.md#parse_formula)
- Pressure in `'mmHg'` and `'kPa'`
- [`ideal_gas.R`](../guide/ideal-gas.md#the-gas-constant)
- `chemhelper.__version__`
- `import chemhelper` loads all four modules

## Installing

The package name is unchanged:

```bash
pip install --upgrade chemhelper
```

The full list of changes is in the [changelog](changelog.md).
