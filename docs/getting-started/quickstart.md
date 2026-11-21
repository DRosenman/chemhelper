# Quickstart

This page takes about five minutes and touches every module. Each example can
be pasted into a Python prompt or a notebook cell.

```pycon
>>> from chemhelper import elements, compounds, conversions, ideal_gas
```

## 1. Look up an element

Every element from hydrogen to uranium is available by its symbol.

```pycon
>>> print(elements.Fe)
Element: Iron, Fe
Atomic Number: 26
Mass: 55.85
>>> elements.Fe.mass
55.85
>>> elements.elements['Na'].name
'Sodium'
```

More in the [elements guide](../guide/elements.md).

## 2. Find a molar mass

Write the formula as a string, the way it appears in a textbook.

```pycon
>>> compounds.mass('H2O')
18.02
>>> compounds.mass('C6H12O6')
180.16
>>> compounds.mass('Al2(SO4)3')
342.17
```

## 3. Show the work

Add `_steps` to the function name to print the worked solution.

```pycon
>>> compounds.mass_steps('Al2(SO4)3')
Al2(SO4)3
Al: 2 x 26.98 = 53.96
S: 3 x 32.07 = 96.21
O: 12 x 16.0 = 192.0

Mass Al2(SO4)3 = 53.96 + 96.21 + 192.0 = 342.17
```

Every solver in chemhelper has a `_steps` twin. See
[Answers and worked solutions](steps.md).

## 4. Percent composition

```pycon
>>> compounds.percent_composition('C6H12O6')
C          39.999
H           6.714
O          53.287
Total:    100.000
Name: C6H12O6, dtype: float64
```

The result is a pandas Series, so you can pull out one element:

```pycon
>>> float(compounds.percent_composition('C6H12O6')['C'])
39.999
```

## 5. Convert grams and moles

```pycon
>>> conversions.grams_to_moles(90.1, 'H2O')
5.0
>>> conversions.moles_to_grams(0.25, 'NaCl')
14.61
>>> conversions.grams_to_moles_steps(90.1, 'H2O')
90.1g H2O x 1 mole H2O/18.02g H2O = 5.0 moles H2O
```

## 6. Work with solutions

What is the molarity when 10 g of NaOH is dissolved to make 0.25 L of
solution?

```pycon
>>> conversions.molarity(0.25, mass=10, chemical='NaOH')
1.0
>>> conversions.molarity_steps(0.25, mass=10, chemical='NaOH')
10g NaOH x 1 mole NaOH/40.0g NaOH = 0.25 moles NaOH
0.25 moles/0.25 L = 1 M
```

How many grams of NaCl are in 2 L of a 0.5 M solution?

```pycon
>>> conversions.molarity_to_grams(0.5, 2, 'NaCl')
58.44
```

## 7. Solve the ideal gas law

Name the variable you want and give the other three.

```pycon
>>> ideal_gas.ideal_gas('P', V=5, n=4, T=300)
19.7
>>> ideal_gas.ideal_gas_steps('P', V=5, n=4, T=300)
PV = nRT
P = nRT/V
P = 4 moles x 0.0821 L*atm/(mol*K) x 300 K / 5 L = 19.7 atm
```

Inputs can use other units, and a mass can stand in for moles:

```pycon
>>> ideal_gas.ideal_gas('V', substance='CO2', m=44.01, P=740, Punits='torr', T=25, Tunits='C')
25.14
```

## What to read next

- [Writing formulas](formulas.md): what the formula parser accepts.
- [Units and rounding](units-and-rounding.md): what units go in, and how
  results are rounded.
- The [User guide](../guide/index.md): every function, in detail.
- The [Tutorials](../tutorials/index.md): complete problems from start to
  finish.
