# User guide

The user guide documents every public name in chemhelper, one module per
page. Each function has its signature, its arguments, what it returns, the
errors it can raise, the formula behind it, and runnable examples.

<div class="grid cards" markdown>

-   :material-atom:{ .lg .middle } [**elements**](elements.md)

    ---

    The `Element` class and four ways to reach the periodic table data.

-   :material-molecule:{ .lg .middle } [**compounds**](compounds.md)

    ---

    `parse_formula`, `mass`, `composition`, `percent_composition` and their
    `_steps` twins.

-   :material-scale-balance:{ .lg .middle } [**conversions**](conversions.md)

    ---

    `grams_to_moles`, `moles_to_grams`, `molarity`, `molarity_to_moles`,
    `molarity_to_grams` and their `_steps` twins.

-   :material-gauge:{ .lg .middle } [**ideal_gas**](ideal-gas.md)

    ---

    `ideal_gas` and `ideal_gas_steps`, with unit options.

</div>

## Everything at a glance

### elements

| Name | Kind | Description |
| --- | --- | --- |
| [`Element`](elements.md#the-element-class) | class | One element: symbol, name, atomic number, mass |
| [`H`, `He`, … `U`](elements.md#by-symbol-as-a-module-attribute) | `Element` objects | One per element, named by symbol |
| [`elements`](elements.md#the-elements-series) | pandas Series | `Element` objects indexed by symbol |
| [`element_index`](elements.md#element_index) | list | Symbols in order of atomic number |
| [`element_objects`](elements.md#element_objects) | list | `Element` objects in order of atomic number |
| [`element_table`](elements.md#element_table) | pandas DataFrame | Symbol, name and mass indexed by atomic number |

### compounds

| Function | Returns | Description |
| --- | --- | --- |
| [`parse_formula(chemical)`](compounds.md#parse_formula) | `OrderedDict` | Atom counts in a formula |
| [`mass(chemical)`](compounds.md#mass) | `float` | Molar mass in g/mol |
| [`mass_steps(chemical)`](compounds.md#mass_steps) | prints | Molar mass, worked |
| [`composition(chemical)`](compounds.md#composition) | Series | Grams of each element per mole |
| [`composition_steps(chemical)`](compounds.md#composition_steps) | prints | Composition, worked |
| [`percent_composition(chemical)`](compounds.md#percent_composition) | Series | Percent by mass of each element |
| [`percent_composition_steps(chemical)`](compounds.md#percent_composition_steps) | prints | Percent composition, worked |

### conversions

| Function | Returns | Description |
| --- | --- | --- |
| [`grams_to_moles(mass, chemical)`](conversions.md#grams_to_moles) | `float` | Grams → moles |
| [`moles_to_grams(moles, chemical)`](conversions.md#moles_to_grams) | `float` | Moles → grams |
| [`molarity(volume, mass, chemical, moles)`](conversions.md#molarity) | `float` | Molarity from moles, or from mass |
| [`molarity_to_moles(M, volume)`](conversions.md#molarity_to_moles) | `float` | Moles of solute in a solution |
| [`molarity_to_grams(molarity, volume, chemical)`](conversions.md#molarity_to_grams) | `float` | Grams of solute in a solution |

Each has a `_steps` twin with the same arguments.

### ideal_gas

| Name | Returns | Description |
| --- | --- | --- |
| [`ideal_gas(solve_for, ...)`](ideal-gas.md#ideal_gas) | `float` | Solve PV = nRT for P, V, n or T |
| [`ideal_gas_steps(solve_for, ...)`](ideal-gas.md#ideal_gas_steps) | prints | The same, worked |
| [`R`](ideal-gas.md#the-gas-constant) | `float` | The gas constant, 0.0821 L·atm/(mol·K) |

## Conventions used in the guide

- Examples start from the imports shown at the top of each page.
- Lines beginning with `>>>` are what you type. The lines below them are what
  Python prints.
- "Returns" means the function gives a value back. "Prints" means it writes
  to the screen and returns `None`. See
  [Answers and worked solutions](../getting-started/steps.md).

For the same information in compact, generated form, see the
[API reference](../reference/compounds.md).
