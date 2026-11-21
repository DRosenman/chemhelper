# compounds

The `compounds` module answers three questions about a chemical formula:

1. What is its **molar mass**?
2. How much of that mass does **each element** contribute?
3. What **percent** of the mass is each element?

```pycon
>>> from chemhelper import compounds
```

Every function takes a formula string. See
[Writing formulas](../getting-started/formulas.md) for what is accepted.

| Function | Returns | Twin that prints the solution |
| --- | --- | --- |
| [`parse_formula`](#parse_formula) | atom counts | none |
| [`mass`](#mass) | molar mass | [`mass_steps`](#mass_steps) |
| [`composition`](#composition) | grams of each element per mole | [`composition_steps`](#composition_steps) |
| [`percent_composition`](#percent_composition) | percent by mass of each element | [`percent_composition_steps`](#percent_composition_steps) |

---

## `parse_formula`

```python
compounds.parse_formula(chemical)
```

Counts the atoms of each element in a formula. The other functions in this
module all start by calling it.

**Arguments**

| Name | Type | Description |
| --- | --- | --- |
| `chemical` | `str` | A chemical formula, such as `'Ca(OH)2'` |

**Returns**

An `OrderedDict` mapping each element symbol to its number of atoms, in the
order the elements first appear in the formula.

**Raises**

`ValueError` for an unknown element, unbalanced parentheses, an unexpected
character, or an empty formula. The message names the problem.

**Examples**

```pycon
>>> dict(compounds.parse_formula('H2O'))
{'H': 2, 'O': 1}
>>> dict(compounds.parse_formula('Ca(OH)2'))
{'Ca': 1, 'O': 2, 'H': 2}
>>> dict(compounds.parse_formula('Al2(SO4)3'))
{'Al': 2, 'S': 3, 'O': 12}
```

An element that appears more than once is counted together:

```pycon
>>> dict(compounds.parse_formula('CH3COOH'))
{'C': 2, 'H': 4, 'O': 2}
>>> dict(compounds.parse_formula('NH4NO3'))
{'N': 2, 'H': 4, 'O': 3}
```

Nested groups multiply through:

```pycon
>>> dict(compounds.parse_formula('K4[Fe(CN)6]'))
{'K': 4, 'Fe': 1, 'C': 6, 'N': 6}
```

Count the total number of atoms in a formula unit:

```pycon
>>> sum(compounds.parse_formula('C6H12O6').values())
24
```

Get the mole ratio of two elements:

```pycon
>>> counts = compounds.parse_formula('Al2(SO4)3')
>>> counts['O'] / counts['Al']
6.0
```

---

## `mass`

```python
compounds.mass(chemical)
```

The molar mass of a compound: the mass in grams of one mole of it.

**Arguments**

| Name | Type | Description |
| --- | --- | --- |
| `chemical` | `str` | A chemical formula |

**Returns**

A `float`: the molar mass in g/mol, rounded to 2 decimals.

**Raises**

`ValueError` if the formula cannot be read.

**How it is calculated**

For each element, multiply its atomic mass by its number of atoms, then add
the results:

\[
M = \sum_i n_i \, m_i
\]

where \(n_i\) is the number of atoms of element \(i\) and \(m_i\) is its
atomic mass. For water: \(2 \times 1.008 + 16.00 = 18.016\), which rounds to
18.02 g/mol.

**Examples**

```pycon
>>> compounds.mass('H2O')
18.02
>>> compounds.mass('NaCl')
58.44
>>> compounds.mass('C6H12O6')
180.16
>>> compounds.mass('Ca(OH)2')
74.1
>>> compounds.mass('Al2(SO4)3')
342.17
```

A single element works too. For a diatomic gas, write the molecule:

```pycon
>>> compounds.mass('O')
16.0
>>> compounds.mass('O2')
32.0
```

Molar masses of several compounds at once:

```pycon
>>> {formula: compounds.mass(formula) for formula in ['HCl', 'H2SO4', 'HNO3']}
{'HCl': 36.46, 'H2SO4': 98.09, 'HNO3': 63.02}
```

---

## `mass_steps`

```python
compounds.mass_steps(chemical)
```

Prints the molar mass calculation one element at a time, then the sum.

**Arguments**

The same as [`mass`](#mass).

**Prints**

1. The formula.
2. One line per element. If there is more than one atom, the line shows the
   count times the atomic mass.
3. The contributions added together, with the molar mass rounded to 2
   decimals.

**Examples**

```pycon
>>> compounds.mass_steps('H2O')
H2O
H: 2 x 1.008 = 2.016
O: 16.0

Mass H2O = 2.016 + 16.0 = 18.02
```

```pycon
>>> compounds.mass_steps('C6H12O6')
C6H12O6
C: 6 x 12.01 = 72.06
H: 12 x 1.008 = 12.096
O: 6 x 16.0 = 96.0

Mass C6H12O6 = 72.06 + 12.096 + 96.0 = 180.16
```

With parentheses, each line shows the total count of that element in the
whole formula. Calcium hydroxide has two oxygens and two hydrogens:

```pycon
>>> compounds.mass_steps('Ca(OH)2')
Ca(OH)2
Ca: 40.08
O: 2 x 16.0 = 32.0
H: 2 x 1.008 = 2.016

Mass Ca(OH)2 = 40.08 + 32.0 + 2.016 = 74.1
```

---

## `composition`

```python
compounds.composition(chemical)
```

The mass each element contributes to one mole of the compound.

**Arguments**

| Name | Type | Description |
| --- | --- | --- |
| `chemical` | `str` | A chemical formula |

**Returns**

A pandas Series named after the formula. There is one entry per element,
giving the grams of that element in one mole of the compound, followed by a
`'Total:'` entry with the molar mass.

**Raises**

`ValueError` if the formula cannot be read.

**Examples**

```pycon
>>> compounds.composition('H2O')
H          2.016
O         16.000
Total:    18.020
Name: H2O, dtype: float64
>>> compounds.composition('C6H12O6')
C          72.060
H          12.096
O          96.000
Total:    180.160
Name: C6H12O6, dtype: float64
```

Pick out one element, or the total:

```pycon
>>> comp = compounds.composition('C6H12O6')
>>> float(comp['C'])
72.06
>>> float(comp['Total:'])
180.16
```

Drop the total to keep only the elements:

```pycon
>>> comp.drop('Total:')
C    72.060
H    12.096
O    96.000
Name: C6H12O6, dtype: float64
```

Repeated elements are combined into one entry:

```pycon
>>> compounds.composition('CH3COOH')
C         24.020
H          4.032
O         32.000
Total:    60.050
Name: CH3COOH, dtype: float64
```

!!! tip "Why `float(...)`?"
    Values taken from a pandas Series are NumPy numbers. They calculate like
    ordinary numbers; wrapping one in `float()` only changes how it prints.

---

## `composition_steps`

```python
compounds.composition_steps(chemical)
```

Prints the molar mass calculation from [`mass_steps`](#mass_steps), then the
[`composition`](#composition) table.

**Example**

```pycon
>>> compounds.composition_steps('H2O')
H2O
H: 2 x 1.008 = 2.016
O: 16.0

Mass H2O = 2.016 + 16.0 = 18.02

H          2.016
O         16.000
Total:    18.020
Name: H2O, dtype: float64
```

---

## `percent_composition`

```python
compounds.percent_composition(chemical)
```

The percent by mass of each element in the compound.

**Arguments**

| Name | Type | Description |
| --- | --- | --- |
| `chemical` | `str` | A chemical formula |

**Returns**

A pandas Series named after the formula. There is one entry per element,
giving its percent of the compound's mass rounded to 3 decimals, followed by
a `'Total:'` entry that is always 100.

**Raises**

`ValueError` if the formula cannot be read.

**How it is calculated**

\[
\%\,\text{element} = \frac{\text{mass of the element in one mole}}{\text{molar mass of the compound}} \times 100
\]

For hydrogen in water: \(2.016 / 18.016 \times 100 = 11.19\%\).

**Examples**

```pycon
>>> compounds.percent_composition('H2O')
H          11.19
O          88.81
Total:    100.00
Name: H2O, dtype: float64
>>> compounds.percent_composition('C6H12O6')
C          39.999
H           6.714
O          53.287
Total:    100.000
Name: C6H12O6, dtype: float64
>>> compounds.percent_composition('Al2(SO4)3')
Al         15.770
S          28.118
O          56.112
Total:    100.000
Name: Al2(SO4)3, dtype: float64
```

The percent of one element:

```pycon
>>> float(compounds.percent_composition('NaCl')['Na'])
39.339
```

Which element makes up most of the mass?

```pycon
>>> compounds.percent_composition('Fe2O3').drop('Total:').idxmax()
'Fe'
```

Compare nitrogen content in three fertilizers:

```pycon
>>> for formula in ['NH3', 'NH4NO3', '(NH4)2SO4']:
...     print(formula, float(compounds.percent_composition(formula)['N']))
NH3 82.247
NH4NO3 35.002
(NH4)2SO4 21.203
```

!!! note "Percentages may not add to exactly 100"
    Each percentage is rounded separately, so the element entries can sum to
    99.999 or 100.001. The `'Total:'` entry is set to 100.

---

## `percent_composition_steps`

```python
compounds.percent_composition_steps(chemical)
```

Prints the complete solution: the molar mass calculation, the mass each
element contributes, and then each percentage.

**Example**

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

```pycon
>>> compounds.percent_composition_steps('CaCO3')
CaCO3
Ca: 40.08
C: 12.01
O: 3 x 16.0 = 48.0

Mass CaCO3 = 40.08 + 12.01 + 48.0 = 100.09

Ca         40.08
C          12.01
O          48.00
Total:    100.09
Name: CaCO3, dtype: float64
Ca: 100 x 40.08g Ca/100.09g CaCO3 = 40.04%
C: 100 x 12.01g C/100.09g CaCO3 = 12.00%
O: 100 x 48.0g O/100.09g CaCO3 = 47.96%
```

---

## Common mistakes

**Wrong capitalization.** `'CO'` is carbon monoxide and `'Co'` is cobalt.
`'co'` is an error.

**Forgetting the subscript on diatomic elements.** Oxygen gas is `'O2'`, not
`'O'`. The same goes for H₂, N₂, F₂, Cl₂, Br₂ and I₂.

**Writing a hydrate with a dot.** Use parentheses: `'CuSO4(H2O)5'`.

```pycon
>>> compounds.mass('CuSO4(H2O)5')
249.7
```

**Expecting `_steps` to return the number.** `_steps` functions print and
return `None`. Call the plain function to get a value.

See [Writing formulas](../getting-started/formulas.md) for the full list of
what the parser accepts and the error messages it gives.
