# Answers and worked solutions

chemhelper is built around one idea: **every solver comes as a pair.**

- The plain function **returns** the answer, so you can store it or use it in
  another calculation.
- The function with `_steps` added to its name **prints** the worked solution
  and returns nothing.

Both take exactly the same arguments.

```pycon
>>> from chemhelper import compounds, conversions, ideal_gas

>>> conversions.grams_to_moles(36.04, 'H2O')
2.0

>>> conversions.grams_to_moles_steps(36.04, 'H2O')
36.04g H2O x 1 mole H2O/18.02g H2O = 2.0 moles H2O
```

## All the pairs

| Returns the answer | Prints the solution | What it solves |
| --- | --- | --- |
| [`compounds.mass`](../guide/compounds.md#mass) | [`compounds.mass_steps`](../guide/compounds.md#mass_steps) | Molar mass |
| [`compounds.composition`](../guide/compounds.md#composition) | [`compounds.composition_steps`](../guide/compounds.md#composition_steps) | Grams of each element per mole |
| [`compounds.percent_composition`](../guide/compounds.md#percent_composition) | [`compounds.percent_composition_steps`](../guide/compounds.md#percent_composition_steps) | Percent by mass of each element |
| [`conversions.grams_to_moles`](../guide/conversions.md#grams_to_moles) | [`conversions.grams_to_moles_steps`](../guide/conversions.md#grams_to_moles_steps) | Grams → moles |
| [`conversions.moles_to_grams`](../guide/conversions.md#moles_to_grams) | [`conversions.moles_to_grams_steps`](../guide/conversions.md#moles_to_grams_steps) | Moles → grams |
| [`conversions.molarity`](../guide/conversions.md#molarity) | [`conversions.molarity_steps`](../guide/conversions.md#molarity_steps) | Molarity of a solution |
| [`conversions.molarity_to_moles`](../guide/conversions.md#molarity_to_moles) | [`conversions.molarity_to_moles_steps`](../guide/conversions.md#molarity_to_moles_steps) | Moles of solute in a solution |
| [`conversions.molarity_to_grams`](../guide/conversions.md#molarity_to_grams) | [`conversions.molarity_to_grams_steps`](../guide/conversions.md#molarity_to_grams_steps) | Grams of solute in a solution |
| [`ideal_gas.ideal_gas`](../guide/ideal-gas.md#ideal_gas) | [`ideal_gas.ideal_gas_steps`](../guide/ideal-gas.md#ideal_gas_steps) | PV = nRT for any variable |

## Solutions build on each other

A `_steps` function shows every calculation the answer depends on. Asking for
the grams of solute in a solution prints the moles first, then the molar mass,
then the final conversion:

```pycon
>>> conversions.molarity_to_grams_steps(0.5, 2, 'NaCl')
0.5 moles/L x 2 L = 1 moles
NaCl
Na: 22.99
Cl: 35.45

Mass NaCl = 22.99 + 35.45 = 58.44
1 moles x 58.44 grams/mole = 58.44 grams
```

Percent composition prints the molar mass, then the mass each element
contributes, then each percentage:

```pycon
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

## `_steps` functions return nothing

They print. If you assign the result, you get `None`:

```pycon
>>> result = compounds.mass_steps('H2O')
H2O
H: 2 x 1.008 = 2.016
O: 16.0

Mass H2O = 2.016 + 16.0 = 18.02
>>> print(result)
None
```

To keep the number, call the plain function:

```pycon
>>> result = compounds.mass('H2O')
>>> result
18.02
```

## Capture a solution as text

To put a worked solution in a file, a web page or a message, capture what the
function prints with the standard library:

```pycon
>>> import contextlib, io
>>> buffer = io.StringIO()
>>> with contextlib.redirect_stdout(buffer):
...     conversions.grams_to_moles_steps(36.04, 'H2O')
>>> solution = buffer.getvalue()
>>> solution
'36.04g H2O x 1 mole H2O/18.02g H2O = 2.0 moles H2O\n'
```

The [Cookbook](../cookbook.md#capture-a-worked-solution-as-a-string) wraps
this in a reusable helper.

## A good way to use the pair

1. Ask the student for their answer.
2. Call the plain function to check it.
3. If it is wrong, call the `_steps` twin and compare line by line to find
   the first step where their work differs.

The [tutoring session tutorial](../tutorials/tutoring-session.md) walks
through this.
