# FAQ and troubleshooting

## About the project

### Is chemhelper still maintained?

Yes. The package was first written in 2017 for tutoring and then sat for a
while. Version 1.0 is a full overhaul, and development is active again. See
the [roadmap](roadmap.md) for what is being considered next.

### Who is it for?

Tutors, teachers and students in a first-year general chemistry course, and
anyone who wants a quick, checkable answer to a routine chemistry
calculation.

### Can I use it to do my homework?

It will give you answers, and the `_steps` functions will show the work. It
is most useful for checking work you have already done and finding the step
where yours differs.

### What license is it under?

MIT. You can use it, change it and share it, including commercially.

## Installing

### `pip install chemhelper` gave me version 0.4

Version 1.0 may not be on PyPI yet. Install from GitHub:

```bash
pip install git+https://github.com/drosenman/chemhelper.git
```

### `ModuleNotFoundError: No module named 'chemhelper'`

The package is installed for a different Python than the one you are
running. In a notebook, install with `%pip install chemhelper` in a cell so
it goes to the notebook's own Python.

### Which Python versions are supported?

Python 3.10 and newer.

### Why does it need pandas?

Element data and composition results are returned as pandas objects so they
print as tidy tables and can be filtered and sorted.

## Formulas

### Why do I get `Unknown element`?

A symbol in your formula is not one of the 92 elements chemhelper knows.
Usually it is a capitalization problem: `'NACL'` should be `'NaCl'`, and
`'CL2'` should be `'Cl2'`. See
[Writing formulas](../getting-started/formulas.md).

### Why do I get `Unexpected character`?

The formula contains something that is not a symbol, a digit, a parenthesis
or a bracket. Lowercase first letters (`'h2o'`), dots (`'CuSO4.5H2O'`) and
charges (`'Na+'`) all cause this.

### How do I write a hydrate?

Put the water in parentheses: `'CuSO4(H2O)5'`.

### How do I write an ion?

Leave the charge off. The mass of the missing or extra electrons is far
smaller than the rounding in the atomic masses.

### Can I use isotopes such as deuterium?

Not out of the box. You can
[add your own element](../guide/elements.md#add-your-own-element).

### Why are elements past uranium missing?

The original table stopped at the naturally abundant elements. Adding the
rest is on the [roadmap](roadmap.md).

### chemhelper accepted a formula that is not a real compound

The parser checks that the symbols are real elements. It does not know which
compounds exist. Use `parse_formula` to see how your string was read.

## Results

### My answer differs slightly from the textbook

Three things can cause a difference in the last digit:

1. **Atomic masses.** chemhelper uses masses rounded to two decimals for most
   elements. Your table may use more digits or newer values.
2. **The gas constant.** `ideal_gas` uses R = 0.0821. Books that use 0.08206
   get slightly different answers.
3. **Rounding.** chemhelper rounds only the final result. Working a problem
   by hand with rounded intermediate values gives a slightly different
   answer.

### My answer differs from chemhelper 0.4

Version 1.0 fixed several bugs, and some results changed. See
[Migrating from 0.4](migrating.md).

### Why did `grams_to_moles` return `0.0`?

It rounds to two decimals, so anything under 0.005 mol rounds to zero. Divide
by `compounds.mass(...)` yourself for small samples. See
[Units and rounding](../getting-started/units-and-rounding.md#very-small-amounts).

### Why does a result look like `0.30000000000000004`?

Functions that do not round return raw floating-point values. Wrap the call
in `round(..., 4)`.

### Why does a value print as `np.float64(18.02)`?

Values taken out of a pandas Series are NumPy numbers. They behave like
ordinary numbers. Wrap one in `float()` to print it plainly.

### Does chemhelper handle significant figures?

No. It rounds to a fixed number of decimals. Apply significant-figure rules
to the final answer yourself.

### The ideal gas answer is in the wrong units

`Punits`, `Vunits` and `Tunits` describe your inputs only. Results are always
in atm, L, mol or K. See the
[ideal gas guide](../guide/ideal-gas.md#use-other-units-for-the-inputs).

### My gas answer is wildly off

Check the temperature. If you passed Celsius without `Tunits='C'`, it was
treated as kelvin.

## Worked solutions

### A `_steps` function returned `None`

That is expected. `_steps` functions print the solution and return nothing.
Call the function without `_steps` to get the number.

### How do I get the solution as text?

Capture the printed output. The
[Cookbook](../cookbook.md#capture-a-worked-solution-as-a-string) has a
helper.

### Can it show steps with more decimal places?

Not yet. The number of decimals in printed solutions is fixed, apart from the
final answer of `ideal_gas_steps`, which follows `decimals`.

## What it does not do

chemhelper does not yet balance equations, read mole ratios from an equation,
find limiting reagents automatically, handle pH or equilibrium, or do
thermochemistry. Several of these are on the [roadmap](roadmap.md), and the
[Cookbook](../cookbook.md) shows how to do some of them with the functions
that exist today.

## Getting help

Open an issue on
[GitHub](https://github.com/drosenman/chemhelper/issues) with the code you
ran, what you expected and what you got.
