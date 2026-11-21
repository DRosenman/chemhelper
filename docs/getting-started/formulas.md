# Writing formulas

Every function that takes a compound takes it as a **formula string** such as
`'H2O'`. This page describes exactly what the parser accepts.

```pycon
>>> from chemhelper import compounds
```

## The rules

1. **Element symbols are case-sensitive.** A symbol is one capital letter,
   optionally followed by one lowercase letter: `C`, `Co`, `Ca`, `Cl`.
2. **A number after a symbol is its count.** No number means one: `H2O` is two
   hydrogens and one oxygen.
3. **Groups go in parentheses or square brackets**, followed by an optional
   count: `Ca(OH)2`, `[Fe(CN)6]`.
4. **Groups can be nested** to any depth: `K4[Fe(CN)6]`.
5. **An element may appear more than once.** Its counts are added together:
   `CH3COOH` is C₂H₄O₂.
6. **Spaces are ignored.**

Only elements 1 to 92 (H to U) are known. See the
[periodic table](../periodic-table.md).

## Examples that work

| You write | Meaning | Counted as |
| --- | --- | --- |
| `'H2O'` | water | H 2, O 1 |
| `'NaCl'` | sodium chloride | Na 1, Cl 1 |
| `'C6H12O6'` | glucose | C 6, H 12, O 6 |
| `'Ca(OH)2'` | calcium hydroxide | Ca 1, O 2, H 2 |
| `'Al2(SO4)3'` | aluminum sulfate | Al 2, S 3, O 12 |
| `'CH3COOH'` | acetic acid | C 2, H 4, O 2 |
| `'(NH4)3PO4'` | ammonium phosphate | N 3, H 12, P 1, O 4 |
| `'K4[Fe(CN)6]'` | potassium ferrocyanide | K 4, Fe 1, C 6, N 6 |
| `'O2'` | oxygen gas | O 2 |
| `'Fe'` | a single element | Fe 1 |

## See how a formula was read

[`parse_formula`](../guide/compounds.md#parse_formula) returns the atom counts
chemhelper will use. It is the quickest way to check that a formula means what
you intended.

```pycon
>>> dict(compounds.parse_formula('Al2(SO4)3'))
{'Al': 2, 'S': 3, 'O': 12}
>>> dict(compounds.parse_formula('CH3COOH'))
{'C': 2, 'H': 4, 'O': 2}
>>> dict(compounds.parse_formula('K4[Fe(CN)6]'))
{'K': 4, 'Fe': 1, 'C': 6, 'N': 6}
```

## Capitalization matters

`Co` is cobalt. `CO` is carbon monoxide. The parser cannot guess which you
meant, so type symbols exactly as they appear on the periodic table.

```pycon
>>> compounds.mass('Co')
58.93
>>> compounds.mass('CO')
28.01
```

## What is not supported

| You might write | Problem | Write this instead |
| --- | --- | --- |
| `'CuSO4·5H2O'` or `'CuSO4.5H2O'` | The hydrate dot is not understood. | `'CuSO4(H2O)5'` |
| `'2H2O'` | Leading coefficients are not understood. | Use `'H2O'` and multiply the result by 2. |
| `'SO4 2-'` or `'Na+'` | Charges are not understood. | Leave the charge off: `'SO4'`, `'Na'`. An electron's mass is negligible here. |
| `'h2o'` or `'NACL'` | Symbols must be capitalized correctly. | `'H2O'`, `'NaCl'` |
| `'H₂O'` | Unicode subscripts are not understood. | `'H2O'` |
| `'Pu'` | Elements past uranium are not included. | Not available yet; see the [roadmap](../project/roadmap.md). |
| Isotopes such as deuterium | No isotope data. | See [adding your own element](../guide/elements.md#add-your-own-element). |

## Error messages

A formula the parser cannot read raises `ValueError` with a message that says
what is wrong.

An unknown or mis-capitalized element:

```pycon
>>> compounds.mass('Xy2')
Traceback (most recent call last):
  ...
ValueError: Unknown element 'Xy' in formula 'Xy2'
>>> compounds.mass('NACL')
Traceback (most recent call last):
  ...
ValueError: Unknown element 'A' in formula 'NACL'
```

!!! tip "Reading the second error"
    In `'NACL'` the parser reads `N` (nitrogen), then `A`, which is not an
    element. All-caps formulas usually fail on the first letter that is not
    itself a one-letter element.

Unbalanced parentheses:

```pycon
>>> compounds.mass('Ca(OH2')
Traceback (most recent call last):
  ...
ValueError: Unbalanced parentheses in formula 'Ca(OH2'
```

A character that does not belong in a formula:

```pycon
>>> compounds.mass('h2o')
Traceback (most recent call last):
  ...
ValueError: Unexpected character 'h' in formula 'h2o'
>>> compounds.mass('CuSO4.5H2O')
Traceback (most recent call last):
  ...
ValueError: Unexpected character '.' in formula 'CuSO4.5H2O'
```

An empty string:

```pycon
>>> compounds.mass('')
Traceback (most recent call last):
  ...
ValueError: Empty formula ''
```

## A caution about look-alike formulas

The parser checks that every symbol is a real element. It does not check that
the compound exists. A typo that happens to spell real elements is accepted:

```pycon
>>> compounds.mass('HO2')
33.01
```

When an answer looks wrong, run `parse_formula` on your string first.
