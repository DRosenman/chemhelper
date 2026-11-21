---
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# chemhelper

<p class="hero-tagline">General chemistry answers in one line of Python,<br>and the worked solution in one more.</p>

[Get started](getting-started/installation.md){ .md-button .md-button--primary }
[User guide](guide/index.md){ .md-button }
[API reference](reference/compounds.md){ .md-button }

</div>

**chemhelper** solves the problems that fill the first semester of general
chemistry: molar mass, percent composition, converting between grams, moles
and molarity, and the ideal gas law. Every solver has a twin whose name ends
in `_steps` that prints the solution the way you would write it on a
whiteboard.

It was written by a chemistry tutor, for tutoring. Check a student's answer in
a second, show exactly where it came from, and spend the rest of the session
on understanding.

=== "Just the answer"

    ```pycon
    >>> from chemhelper import compounds
    >>> compounds.mass('Ca(OH)2')
    74.1
    ```

=== "The worked solution"

    ```pycon
    >>> from chemhelper import compounds
    >>> compounds.mass_steps('Ca(OH)2')
    Ca(OH)2
    Ca: 40.08
    O: 2 x 16.0 = 32.0
    H: 2 x 1.008 = 2.016

    Mass Ca(OH)2 = 40.08 + 32.0 + 2.016 = 74.1
    ```

=== "A whole problem"

    How many grams of NaCl do you need for 2 L of a 0.5 M solution?

    ```pycon
    >>> from chemhelper import conversions
    >>> conversions.molarity_to_grams_steps(0.5, 2, 'NaCl')
    0.5 moles/L x 2 L = 1 moles
    NaCl
    Na: 22.99
    Cl: 35.45

    Mass NaCl = 22.99 + 35.45 = 58.44
    1 moles x 58.44 grams/mole = 58.44 grams
    ```

## What's inside

<div class="grid cards" markdown>

-   :material-atom:{ .lg .middle } **elements**

    ---

    Symbol, name, atomic number and mass for elements 1 to 92, as objects and
    as a pandas table.

    [:octicons-arrow-right-24: Elements guide](guide/elements.md)

-   :material-molecule:{ .lg .middle } **compounds**

    ---

    Parse formulas like `Al2(SO4)3`, then get molar mass, mass composition and
    percent composition.

    [:octicons-arrow-right-24: Compounds guide](guide/compounds.md)

-   :material-scale-balance:{ .lg .middle } **conversions**

    ---

    Grams to moles and back, molarity from mass or moles, and solute needed
    for a target concentration.

    [:octicons-arrow-right-24: Conversions guide](guide/conversions.md)

-   :material-gauge:{ .lg .middle } **ideal_gas**

    ---

    Solve PV = nRT for any variable, with inputs in atm, torr, mmHg, kPa, L,
    mL, K or °C.

    [:octicons-arrow-right-24: Ideal gas guide](guide/ideal-gas.md)

</div>

## Why use it

<div class="grid cards" markdown>

-   :material-format-list-numbered:{ .lg .middle } **Shows its work**

    ---

    Every solver has a `_steps` twin. The printed solution includes units and
    each intermediate value.

-   :material-text-box-check-outline:{ .lg .middle } **Reads like chemistry**

    ---

    Formulas are written the way they appear in a textbook, parentheses and
    all. Arguments are named after the quantities.

-   :material-alert-circle-check-outline:{ .lg .middle } **Tells you what went wrong**

    ---

    A typo in a formula or a missing value raises an error that names the
    problem, not a cryptic traceback.

-   :material-test-tube:{ .lg .middle } **Tested examples**

    ---

    Every example on this site is run against the real package before the
    site is published.

</div>

## Where to go next

| If you want to… | Read |
| --- | --- |
| Install the package and run your first calculation | [Installation](getting-started/installation.md), then the [Quickstart](getting-started/quickstart.md) |
| Learn how formulas must be written | [Writing formulas](getting-started/formulas.md) |
| See every function in a module, with examples | The [User guide](guide/index.md) |
| Work through complete problems | The [Tutorials](tutorials/index.md) |
| Copy a short recipe | The [Cookbook](cookbook.md) |
| Look up the atomic masses chemhelper uses | The [Periodic table](periodic-table.md) |
| Upgrade code written for version 0.4 | [Migrating from 0.4](project/migrating.md) |
| See what's planned or help out | [Roadmap](project/roadmap.md) and [Contributing](project/contributing.md) |
