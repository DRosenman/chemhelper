# Worked examples

## Look up an element

```python
>>> print(elements.elements['Fe'])
Element: Iron, Fe
Atomic Number: 26
Mass: 55.85
>>> elements.element_table.head(3)
Atomic Number Symbol      Name  Mass
1                  H  Hydrogen  1.01
2                 He    Helium  4.00
3                 Li   Lithium  6.94
```

## Percent composition of glucose

```python
>>> compounds.percent_composition('C6H12O6')
C          39.999
H           6.714
O          53.287
Total:    100.000
Name: C6H12O6, dtype: float64
```

`compounds.percent_composition_steps('C6H12O6')` prints the molar mass
calculation, the mass contributed by each element, and each percentage.

## How many grams of NaCl for 2 L of a 0.5 M solution?

```python
>>> conversions.molarity_to_grams(0.5, 2, 'NaCl')
58.44
>>> conversions.molarity_to_grams_steps(0.5, 2, 'NaCl')
0.50 moles/L x 2.00 L = 1.00 moles
NaCl
Na: 22.99
Cl: 35.45

Mass NaCl = 22.99 + 35.45 = 58.44
1.00 moles x 58.44 grams/mole = 58.44 grams
```

## Molarity from a mass of solute

```python
>>> conversions.molarity(0.25, mass=10, chemical='NaOH')
1.0
```

## Ideal gas law

What pressure do 32 g of O₂ exert in a 500 mL flask at 25 °C?

```python
>>> ideal_gas.ideal_gas('P', substance='O2', m=32, V=500, Vunits='mL', T=25, Tunits='C')
48.96
>>> ideal_gas.ideal_gas_steps('P', substance='O2', m=32, V=500, Vunits='mL', T=25, Tunits='C')
n = 32g x 1 mole O2/32.0g O2 = 1 moles O2
V = 500 mL x 1 L/1000 mL = 0.5 L
T = (25 + 273.15) K = 298.15 K
PV = nRT
P = nRT/V
P = 1 moles x 0.0821 L*atm/(mol*K) x 298.15 K / 0.5 L = 48.96 atm
```

Solve for any of `'P'`, `'V'`, `'n'` or `'T'` by giving the other three.
