# Units and rounding

chemhelper works with plain numbers. It does not attach units to them, so you
need to know which units each function expects and which it returns.

```pycon
>>> from chemhelper import compounds, conversions, ideal_gas
```

## Units

### What goes in and what comes out

| Quantity | Unit | Used by |
| --- | --- | --- |
| Mass | grams (g) | `conversions`, `ideal_gas` (`m`) |
| Amount | moles (mol) | `conversions`, `ideal_gas` (`n`) |
| Molar mass | grams per mole (g/mol) | `compounds`, `elements` |
| Volume of solution | liters (L) | `conversions` |
| Concentration | moles per liter (M) | `conversions` |
| Gas volume | liters by default; milliliters with `Vunits='mL'` | `ideal_gas` |
| Pressure | atmospheres by default; `Punits` may be `'torr'`, `'mmHg'` or `'kPa'` | `ideal_gas` |
| Temperature | kelvin by default; Celsius with `Tunits='C'` | `ideal_gas` |

### Volumes in `conversions` are always liters

The molarity functions have no unit option. Convert milliliters yourself by
dividing by 1000:

```pycon
>>> conversions.molarity(250 / 1000, moles=0.05)
0.2
```

### Unit options in `ideal_gas` describe your inputs

`Punits`, `Vunits` and `Tunits` tell `ideal_gas` what units the values **you
give** are in. The answer always comes back in the base unit:

| You solve for | The result is in |
| --- | --- |
| `'P'` | atm |
| `'V'` | L |
| `'n'` | mol |
| `'T'` | K |

```pycon
>>> ideal_gas.ideal_gas('n', P=760, Punits='torr', V=500, Vunits='mL', T=25, Tunits='C', decimals=4)
0.0204
```

To get an answer in another unit, convert it afterwards:

```pycon
>>> p_atm = ideal_gas.ideal_gas('P', n=2, V=10, T=300)
>>> p_atm
4.93
>>> round(p_atm * 760, 1)
3746.8
>>> t_kelvin = ideal_gas.ideal_gas('T', P=1, V=12, n=0.5)
>>> round(t_kelvin - 273.15, 2)
19.18
```

### Conversion factors used

| Conversion | Factor |
| --- | --- |
| torr or mmHg → atm | divide by 760 |
| kPa → atm | divide by 101.325 |
| mL → L | divide by 1000 |
| °C → K | add 273.15 |

### The gas constant

`ideal_gas` uses R = 0.0821 L·atm/(mol·K), the three-significant-figure value
printed in most general chemistry textbooks. It is available as a constant:

```pycon
>>> ideal_gas.R
0.0821
```

Because R has three significant figures, ideal gas answers are reliable to
about three significant figures, however many decimals you ask for.

## Rounding

Results are rounded so they look like textbook answers. Each function rounds
only its final result.

| Function | Result is rounded to |
| --- | --- |
| `compounds.mass` | 2 decimals |
| `compounds.composition` | 4 decimals per element; 2 for the total |
| `compounds.percent_composition` | 3 decimals |
| `conversions.grams_to_moles` | 2 decimals |
| `conversions.moles_to_grams` | 2 decimals |
| `conversions.molarity` | not rounded |
| `conversions.molarity_to_moles` | not rounded |
| `conversions.molarity_to_grams` | 2 decimals |
| `ideal_gas.ideal_gas` | `decimals` argument, 2 by default |

### Numbers in printed solutions

`_steps` functions show intermediate quantities to four significant figures
(six in `ideal_gas_steps`), so small amounts such as 0.00375 mol stay
visible. Masses in grams and molar masses are shown to two decimals.

### Molar masses are rounded before they are used in conversions

The `conversions` functions and the mass option of `ideal_gas` use the
two-decimal molar mass from `compounds.mass`, the same number a student would
read off their own calculation.

### Very small amounts

Two decimals is not enough for very small quantities. Five milligrams of
water is a real amount, but it rounds to zero moles:

```pycon
>>> conversions.grams_to_moles(0.005, 'H2O')
0.0
```

When you need more precision, divide by the molar mass yourself:

```pycon
>>> round(0.005 / compounds.mass('H2O'), 6)
0.000277
```

### Choosing decimals for gas problems

```pycon
>>> ideal_gas.ideal_gas('V', n=1, T=273.15, P=1)
22.43
>>> ideal_gas.ideal_gas('V', n=1, T=273.15, P=1, decimals=4)
22.4256
>>> ideal_gas.ideal_gas('V', n=1, T=273.15, P=1, decimals=0)
22.0
```

### Significant figures

chemhelper does not track significant figures. It rounds to a fixed number of
decimals. Apply your course's significant-figure rules to the final answer
yourself. This is on the [roadmap](../project/roadmap.md).

### Floating-point tails

The functions that do not round can return values such as
`0.30000000000000004`. That is ordinary floating-point arithmetic, not a
chemistry error. Round the result when you display it:

```pycon
>>> conversions.molarity_to_moles(0.1, 3)
0.30000000000000004
>>> round(conversions.molarity_to_moles(0.1, 3), 4)
0.3
```
