# ideal_gas

The `ideal_gas` module solves the ideal gas law for any one of its four
variables.

\[
PV = nRT
\]

```pycon
>>> from chemhelper import ideal_gas
```

| Symbol | Quantity | Argument | Default unit |
| --- | --- | --- | --- |
| \(P\) | pressure | `P` | atm |
| \(V\) | volume | `V` | L |
| \(n\) | amount of gas | `n` | mol |
| \(T\) | absolute temperature | `T` | K |
| \(R\) | gas constant | fixed | 0.0821 L·atm/(mol·K) |

The module has two functions, which take the same arguments:

| Function | What it does |
| --- | --- |
| [`ideal_gas`](#ideal_gas) | Returns the answer |
| [`ideal_gas_steps`](#ideal_gas_steps) | Prints the worked solution |

---

## `ideal_gas`

```python
ideal_gas.ideal_gas(solve_for, substance=None, P=None, V=None, n=None, T=None,
                    m=None, decimals=2, Tunits='K', Vunits='L', Punits='atm')
```

Name the variable you want with `solve_for`, and give the other three.

**Arguments**

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `solve_for` | `'P'`, `'V'`, `'n'` or `'T'` | required | The variable to solve for |
| `substance` | `str` | `None` | Formula of the gas. Needed only when you give `m`. |
| `P` | number | `None` | Pressure, in `Punits` |
| `V` | number | `None` | Volume, in `Vunits` |
| `n` | number | `None` | Amount of gas in moles |
| `T` | number | `None` | Temperature, in `Tunits` |
| `m` | number | `None` | Mass of gas in grams. Used to find `n`. |
| `decimals` | `int` | `2` | Decimal places in the result |
| `Tunits` | `'K'` or `'C'` | `'K'` | Units of the `T` you give |
| `Vunits` | `'L'` or `'mL'` | `'L'` | Units of the `V` you give |
| `Punits` | `'atm'`, `'torr'`, `'mmHg'` or `'kPa'` | `'atm'` | Units of the `P` you give |

**Returns**

A `float`, rounded to `decimals` places, in the base unit of the solved
variable:

| `solve_for` | Formula used | Result unit |
| --- | --- | --- |
| `'P'` | \(P = nRT / V\) | atm |
| `'V'` | \(V = nRT / P\) | L |
| `'n'` | \(n = PV / RT\) | mol |
| `'T'` | \(T = PV / nR\) | K |

**Raises**

`ValueError` when:

- `solve_for` is not one of `'P'`, `'V'`, `'n'`, `'T'`
- a unit option is not one of the allowed values
- one of the three needed values is missing
- `m` is given without `substance`
- `substance` cannot be read as a formula

### Solve for pressure

What pressure do 4 mol of gas exert in a 5 L container at 300 K?

```pycon
>>> ideal_gas.ideal_gas('P', V=5, n=4, T=300)
19.7
```

### Solve for volume

What volume does 1 mol of gas occupy at 273.15 K and 1 atm?

```pycon
>>> ideal_gas.ideal_gas('V', n=1, T=273.15, P=1)
22.43
```

### Solve for moles

How many moles of gas are in a 10 L tank at 2.5 atm and 298 K?

```pycon
>>> ideal_gas.ideal_gas('n', P=2.5, V=10, T=298)
1.02
```

### Solve for temperature

At what temperature does 0.5 mol of gas occupy 12 L at 1 atm?

```pycon
>>> ideal_gas.ideal_gas('T', P=1, V=12, n=0.5)
292.33
```

### Give a mass in place of moles

If you know the mass of the gas, pass it as `m` and name the gas with
`substance`. The moles are worked out from the molar mass.

What volume do 10.2 g of water vapor occupy at 1.5 atm and 300 K?

```pycon
>>> ideal_gas.ideal_gas('V', substance='H2O', m=10.2, P=1.5, T=300)
9.29
```

What pressure do 64 g of O₂ exert in a 10 L tank at 298 K?

```pycon
>>> ideal_gas.ideal_gas('P', substance='O2', m=64, V=10, T=298)
4.89
```

If you give both `n` and `m`, `n` is used and `m` is ignored.

### Use other units for the inputs

`Punits`, `Vunits` and `Tunits` describe the values you pass in. They are
converted before the equation is solved.

```pycon
>>> ideal_gas.ideal_gas('n', P=740, Punits='torr', V=250, Vunits='mL', T=22, Tunits='C', decimals=4)
0.01
>>> ideal_gas.ideal_gas('V', n=2, P=101.325, Punits='kPa', T=0, Tunits='C')
44.85
>>> ideal_gas.ideal_gas('V', n=2, P=760, Punits='mmHg', T=0, Tunits='C')
44.85
```

!!! warning "The answer is always in atm, L, mol or K"
    A unit option applies only to an input. When you solve for pressure, the
    result is in atm whatever `Punits` says, because there is no pressure
    input to describe. Convert the result yourself:

    ```pycon
    >>> p = ideal_gas.ideal_gas('P', n=2, V=10, T=300)
    >>> p
    4.93
    >>> round(p * 760, 1)
    3746.8
    >>> round(p * 101.325, 1)
    499.5
    ```

    Likewise, a temperature answer is in kelvin. Subtract 273.15 for Celsius.

    ```pycon
    >>> round(ideal_gas.ideal_gas('T', P=1, V=12, n=0.5) - 273.15, 2)
    19.18
    ```

| Option | Value | Conversion applied |
| --- | --- | --- |
| `Punits` | `'atm'` | none |
| | `'torr'` or `'mmHg'` | divide by 760 |
| | `'kPa'` | divide by 101.325 |
| `Vunits` | `'L'` | none |
| | `'mL'` | divide by 1000 |
| `Tunits` | `'K'` | none |
| | `'C'` | add 273.15 |

### Choose the number of decimals

```pycon
>>> ideal_gas.ideal_gas('V', n=1, T=273.15, P=1, decimals=4)
22.4256
>>> ideal_gas.ideal_gas('V', n=1, T=273.15, P=1, decimals=1)
22.4
```

### Errors

A missing value:

```pycon
>>> ideal_gas.ideal_gas('P', V=5, T=300)
Traceback (most recent call last):
  ...
ValueError: Missing value(s) for: n
```

A mass without a substance:

```pycon
>>> ideal_gas.ideal_gas('P', m=64, V=10, T=298)
Traceback (most recent call last):
  ...
ValueError: substance is required when giving the mass m
```

An unknown variable or unit:

```pycon
>>> ideal_gas.ideal_gas('X', P=1, V=1, T=300)
Traceback (most recent call last):
  ...
ValueError: solve_for must be 'P', 'V', 'n' or 'T', not 'X'
>>> ideal_gas.ideal_gas('n', P=1, Punits='bar', V=1, T=300)
Traceback (most recent call last):
  ...
ValueError: Punits must be one of ['atm', 'kPa', 'mmHg', 'torr']
```

---

## `ideal_gas_steps`

```python
ideal_gas.ideal_gas_steps(solve_for, substance=None, P=None, V=None, n=None, T=None,
                          m=None, decimals=2, Tunits='K', Vunits='L', Punits='atm')
```

Prints the worked solution. It takes exactly the same arguments as
[`ideal_gas`](#ideal_gas).

**Prints**

1. Any conversions needed first: mass to moles, then pressure, volume and
   temperature into atm, L and K.
2. The ideal gas law.
3. The law rearranged for the variable being solved.
4. The values substituted in, with units, and the answer.

**Examples**

A direct calculation:

```pycon
>>> ideal_gas.ideal_gas_steps('P', V=5, n=4, T=300)
PV = nRT
P = nRT/V
P = 4 moles x 0.0821 L*atm/(mol*K) x 300 K / 5 L = 19.7 atm
```

Starting from a mass:

```pycon
>>> ideal_gas.ideal_gas_steps('V', substance='H2O', m=10.2, P=1.5, T=300)
n = 10.2g x 1 mole H2O/18.02g H2O = 0.566038 moles H2O
PV = nRT
V = nRT/P
V = 0.566038 moles x 0.0821 L*atm/(mol*K) x 300 K / 1.5 atm = 9.29 L
```

With unit conversions:

```pycon
>>> ideal_gas.ideal_gas_steps('n', P=740, Punits='torr', V=250, Vunits='mL', T=22, Tunits='C', decimals=4)
P = 740 torr = 0.973684 atm
V = 250 mL x 1 L/1000 mL = 0.25 L
T = (22 + 273.15) K = 295.15 K
PV = nRT
n = PV/RT
n = (0.973684 atm x 0.25 L) / (0.0821 L*atm/(mol*K) x 295.15 K) = 0.01 moles
```

Solving for temperature:

```pycon
>>> ideal_gas.ideal_gas_steps('T', P=1, V=12, n=0.5)
PV = nRT
T = PV/nR
T = (1 atm x 12 L) / (0.5 moles x 0.0821 L*atm/(mol*K)) = 292.33 K
```

Everything at once:

```pycon
>>> ideal_gas.ideal_gas_steps('P', substance='O2', m=32, V=500, Vunits='mL', T=25, Tunits='C')
n = 32g x 1 mole O2/32.0g O2 = 1 moles O2
V = 500 mL x 1 L/1000 mL = 0.5 L
T = (25 + 273.15) K = 298.15 K
PV = nRT
P = nRT/V
P = 1 moles x 0.0821 L*atm/(mol*K) x 298.15 K / 0.5 L = 48.96 atm
```

!!! note "Numbers in the printed steps"
    Intermediate values in the printed solution are shown to about six
    significant figures. The calculation itself carries full precision, so
    the final answer matches `ideal_gas` exactly.

---

## The gas constant

```pycon
>>> ideal_gas.R
0.0821
```

`R` is 0.0821 L·atm/(mol·K), the value used in most general chemistry
courses. It has three significant figures, so answers are good to about three
significant figures. This is why the molar volume at 0 °C and 1 atm comes out
as 22.43 L here, where a more precise R gives 22.41 L.

## Getting a mass as the answer

`ideal_gas` cannot solve for mass directly. Solve for moles, keeping extra
decimals, then convert:

```pycon
>>> from chemhelper import conversions
>>> n = ideal_gas.ideal_gas('n', P=1, V=5, T=298, decimals=4)
>>> n
0.2044
>>> conversions.moles_to_grams(n, 'CO2')
9.0
```

## When the ideal gas law applies

The ideal gas law assumes gas particles have no volume and do not attract one
another. It works well for most gases near room temperature and atmospheric
pressure. It becomes inaccurate at high pressure, at low temperature, and
near the point where a gas condenses. chemhelper does not check for this.

## Common mistakes

**Temperature in Celsius without saying so.** The law needs kelvin. Either
convert first or pass `Tunits='C'`.

```pycon
>>> ideal_gas.ideal_gas('V', n=1, P=1, T=25)
2.05
>>> ideal_gas.ideal_gas('V', n=1, P=1, T=25, Tunits='C')
24.48
```

The first answer is wrong for a gas at 25 °C. It treats the temperature as
25 K.

**Expecting the answer in your input units.** Results are always atm, L, mol
or K.

**Forgetting `substance` with `m`.** The mass can only become moles if the
gas is named.

**Writing a diatomic gas as a single atom.** Oxygen gas is `'O2'`. Using
`'O'` halves the molar mass and doubles the moles.

More worked problems are in the [gas laws tutorial](../tutorials/gases.md).
