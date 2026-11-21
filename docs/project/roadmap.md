# Roadmap

chemhelper is under active development. Version 1.0 put the foundations in
order: a working package layout, a correct formula parser, tests, and this
documentation. The plan now is to grow the range of problems it can solve.

!!! note "Ideas, not promises"
    Everything on this page is a direction being considered. Nothing here has
    a release date. If one of these matters to you, say so in an
    [issue](https://github.com/drosenman/chemhelper/issues), because interest
    decides the order.

## Smaller improvements

| Idea | Why |
| --- | --- |
| A `decimals` argument on every function | Rounding to two decimals is too coarse for small samples |
| Significant-figure handling | Course answers are graded on significant figures |
| `_steps` functions that can return text | Makes it easier to use solutions in web pages and files |
| Volume units (`'mL'`) in `conversions` | Matches what `ideal_gas` already offers |
| Result units in `ideal_gas` | Ask for the answer in torr, kPa, mL or °C directly |
| Elements 93 to 118 | Complete the periodic table |
| More element data | Group, period, electron configuration, electronegativity |
| Hydrate notation (`'CuSO4·5H2O'`) | Write hydrates the way textbooks do |
| A more precise gas constant option | Match courses that use 0.08206 or 8.314 |

## New kinds of problems

| Area | What it would cover |
| --- | --- |
| Chemical equations | Parsing and balancing equations |
| Stoichiometry | Mole ratios, limiting reagent, theoretical and percent yield |
| Empirical formulas | From percent composition or from masses |
| Dilution | \(M_1 V_1 = M_2 V_2\) as a function with steps |
| More gas laws | Combined gas law, partial pressures, gas density, molar mass of a gas |
| Solutions | Molality, mass percent, mole fraction |
| Acids and bases | pH, pOH, strong acid and base calculations, titration |
| Thermochemistry | \(q = mc\Delta T\), heats of reaction |

Each new solver will follow the pattern the existing ones use: a function
that returns the answer and a `_steps` twin that prints the work.

## Not planned

chemhelper is a teaching and checking tool for general chemistry. It is not
meant to become a cheminformatics library. Molecular structures, SMILES
strings, quantum chemistry and reaction databases are out of scope; libraries
such as RDKit serve those needs.

## Suggest something

Open an [issue](https://github.com/drosenman/chemhelper/issues) describing the
kind of problem you want solved, ideally with one worked example. If you
would like to build it yourself, see [Contributing](contributing.md).
