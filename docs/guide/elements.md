# elements

The `elements` module holds the periodic table data that the rest of
chemhelper is built on: the symbol, name, atomic number and atomic mass of
every element from hydrogen (1) to uranium (92).

```pycon
>>> from chemhelper import elements
```

!!! note "Two things are called `elements`"
    `elements` is the **module**. Inside it is a pandas Series that is also
    called `elements`. So `elements.Fe` is an attribute of the module, and
    `elements.elements['Fe']` is a lookup in the Series. Both give you the
    same object.

## The Element class

```python
class Element(symbol, name, atomic_number, mass)
```

An `Element` is a small record describing one element.

### Attributes

| Attribute | Type | Description | Example for iron |
| --- | --- | --- | --- |
| `symbol` | `str` | Chemical symbol | `'Fe'` |
| `name` | `str` | Element name | `'Iron'` |
| `atomic_number` | `int` | Number of protons | `26` |
| `mass` | `float` | Atomic mass in g/mol | `55.85` |

```pycon
>>> iron = elements.Fe
>>> iron.symbol
'Fe'
>>> iron.name
'Iron'
>>> iron.atomic_number
26
>>> iron.mass
55.85
```

!!! info "What `mass` means"
    `mass` is the molar mass of the element in grams per mole. The same
    number is the average mass of one atom in atomic mass units (amu).

### Printing an element

`print` gives a readable summary. Typing the name alone at a prompt gives a
compact form that shows how the object was built.

```pycon
>>> print(elements.Ca)
Element: Calcium, Ca
Atomic Number: 20
Mass: 40.08
>>> elements.Ca
Element('Ca', 'Calcium', 20, 40.08)
```

More examples:

```pycon
>>> print(elements.H)
Element: Hydrogen, H
Atomic Number: 1
Mass: 1.008
>>> elements.Ti.name
'Titanium'
>>> elements.Ag.mass
107.87
>>> elements.K.atomic_number
19
```

## Four ways to get an element

### By symbol, as a module attribute

Every element is a variable in the module, named by its symbol. This is the
shortest form when you know the element as you write the code.

```pycon
>>> elements.Na
Element('Na', 'Sodium', 11, 22.99)
>>> elements.Na.mass
22.99
```

### By symbol, from the `elements` Series

Use this when the symbol is in a variable.

```pycon
>>> symbol = 'Cl'
>>> elements.elements[symbol]
Element('Cl', 'Chlorine', 17, 35.45)
>>> elements.elements[symbol].mass
35.45
```

### By atomic number

`element_objects` is a list in order of atomic number. Lists count from zero,
so the element with atomic number *Z* is at position *Z* − 1.

```pycon
>>> elements.element_objects[0]
Element('H', 'Hydrogen', 1, 1.008)
>>> elements.element_objects[26 - 1]
Element('Fe', 'Iron', 26, 55.85)
```

`element_table` is indexed by atomic number directly:

```pycon
>>> elements.element_table.loc[26]
Atomic Number
Symbol       Fe
Name       Iron
Mass      55.85
Name: 26, dtype: object
```

### By name

Search the `Name` column of `element_table`:

```pycon
>>> table = elements.element_table
>>> table[table['Name'] == 'Gold']
Atomic Number Symbol  Name    Mass
79                Au  Gold  196.97
```

## The `elements` Series

`elements.elements` is a pandas Series of all 92 `Element` objects, indexed by
symbol.

```pycon
>>> len(elements.elements)
92
>>> elements.elements['O']
Element('O', 'Oxygen', 8, 16.0)
>>> 'Fe' in elements.elements.index
True
>>> 'Xx' in elements.elements.index
False
```

Look up several elements at once:

```pycon
>>> [e.name for e in elements.elements[['H', 'C', 'N', 'O']]]
['Hydrogen', 'Carbon', 'Nitrogen', 'Oxygen']
```

Loop over all of them:

```pycon
>>> [e.symbol for e in elements.elements if e.mass > 220]
['Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U']
```

## `element_index`

A list of the 92 symbols in order of atomic number.

```pycon
>>> elements.element_index[:10]
['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
>>> len(elements.element_index)
92
>>> elements.element_index.index('Fe') + 1
26
```

The last line finds an atomic number from a symbol: the position in the list,
plus one.

## `element_objects`

A list of the 92 `Element` objects in order of atomic number.

```pycon
>>> elements.element_objects[:3]
[Element('H', 'Hydrogen', 1, 1.008), Element('He', 'Helium', 2, 4.0026), Element('Li', 'Lithium', 3, 6.94)]
>>> elements.element_objects[-1]
Element('U', 'Uranium', 92, 238.03)
```

## `element_table`

A pandas DataFrame with one row per element. The index is the atomic number
and the columns are `Symbol`, `Name` and `Mass`.

```pycon
>>> elements.element_table.head()
Atomic Number Symbol       Name   Mass
1                  H   Hydrogen   1.01
2                 He     Helium   4.00
3                 Li    Lithium   6.94
4                 Be  Beryllium   9.01
5                  B      Boron  10.81
>>> elements.element_table.shape
(92, 3)
```

!!! warning "Masses in the table are rounded to two decimals"
    `element_table` is meant for display, so its `Mass` column is rounded to
    two decimals. The `Element` objects keep the stored value, and that is
    what calculations use.

    ```pycon
    >>> elements.H.mass
    1.008
    >>> float(elements.element_table.loc[1, 'Mass'])
    1.01
    ```

Because it is a DataFrame, all of pandas is available.

The five heaviest elements:

```pycon
>>> elements.element_table.sort_values('Mass', ascending=False).head()
Atomic Number Symbol          Name    Mass
92                 U       Uranium  238.03
90                Th       Thorium  232.04
91                Pa  Protactinium  231.04
89                Ac      Actinium  227.00
88                Ra        Radium  226.00
```

The noble gases:

```pycon
>>> table = elements.element_table
>>> table[table['Symbol'].isin(['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn'])]
Atomic Number Symbol     Name    Mass
2                 He   Helium    4.00
10                Ne     Neon   20.18
18                Ar    Argon   39.95
36                Kr  Krypton   83.80
54                Xe    Xenon  131.29
86                Rn    Radon  222.00
```

Elements whose names start with "C":

```pycon
>>> table[table['Name'].str.startswith('C')]['Name'].tolist()
['Carbon', 'Chlorine', 'Calcium', 'Chromium', 'Cobalt', 'Copper', 'Cadmium', 'Cesium', 'Cerium']
```

The period 2 elements, by atomic number:

```pycon
>>> table.loc[3:10]
Atomic Number Symbol       Name   Mass
3                 Li    Lithium   6.94
4                 Be  Beryllium   9.01
5                  B      Boron  10.81
6                  C     Carbon  12.01
7                  N   Nitrogen  14.01
8                  O     Oxygen  16.00
9                  F   Fluorine  19.00
10                Ne       Neon  20.18
```

Save the whole table to a spreadsheet-friendly file:

```python
elements.element_table.to_csv('elements.csv')
```

## About the data

- **Coverage.** Elements 1 to 92. Elements past uranium are not included yet.
- **Masses.** The rounded values printed on most classroom periodic tables,
  usually two decimal places. Hydrogen (1.008) and helium (4.0026) carry
  more.
- **Radioactive elements.** Elements with no stable isotope (Tc, Pm, and Po
  through Ac) use the mass number of a long-lived isotope, as periodic tables
  do.
- **Your textbook may differ slightly.** Standard atomic masses are revised
  from time to time, so a recent table can differ from these values in the
  last digit. The [periodic table page](../periodic-table.md) lists every
  value chemhelper uses.

## Add your own element

The `Element` class is public, so you can create elements that are not in the
table. A common reason is an isotope, such as deuterium.

```pycon
>>> D = elements.Element('D', 'Deuterium', 1, 2.014)
>>> print(D)
Element: Deuterium, D
Atomic Number: 1
Mass: 2.014
```

To use a new element inside formulas, add it to the `elements` Series. The
formula parser looks symbols up there.

```pycon
>>> from chemhelper import compounds
>>> elements.elements['D'] = D
>>> compounds.mass('D2O')
20.03
>>> compounds.mass('H2O')
18.02
```

!!! warning "This lasts until Python restarts"
    The addition lives in memory only, and it does not update
    `element_index`, `element_objects` or `element_table`. A symbol must be
    one capital letter optionally followed by one lowercase letter, or the
    parser will not recognize it.
