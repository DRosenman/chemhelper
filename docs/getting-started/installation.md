# Installation

## Requirements

| Requirement | Version |
| --- | --- |
| Python | 3.10 or newer |
| pandas | 1.3 or newer (installed automatically) |

chemhelper is pure Python and runs anywhere pandas does: Windows, macOS and
Linux.

## Install from PyPI

```bash
pip install chemhelper
```

To upgrade an existing installation:

```bash
pip install --upgrade chemhelper
```

!!! info "Version 1.0 is new"
    If `pip` gives you version 0.4, the 1.0 release has not reached PyPI yet.
    Install it from GitHub as shown below.

## Install from GitHub

This installs the latest code on the `master` branch:

```bash
pip install git+https://github.com/drosenman/chemhelper.git
```

## Install in a notebook

In Jupyter or Google Colab, run this in a cell:

```
%pip install chemhelper
```

## Check the installation

```pycon
>>> import chemhelper
>>> chemhelper.__version__
'1.0.0'
>>> from chemhelper import compounds
>>> compounds.mass('H2O')
18.02
```

If you see a version number and a molar mass for water, you're ready for the
[Quickstart](quickstart.md).

## Import the modules

chemhelper has four modules. Import the ones you need:

```python
from chemhelper import elements, compounds, conversions, ideal_gas
```

Importing the package also loads all four, so this works too:

```python
import chemhelper

chemhelper.compounds.mass('H2O')
```

| Module | What it does | Guide |
| --- | --- | --- |
| `elements` | Periodic table data | [elements](../guide/elements.md) |
| `compounds` | Molar mass and composition | [compounds](../guide/compounds.md) |
| `conversions` | Grams, moles and molarity | [conversions](../guide/conversions.md) |
| `ideal_gas` | PV = nRT | [ideal_gas](../guide/ideal-gas.md) |

## Install for development

To change chemhelper itself, clone the repository and install it in editable
mode with the test and documentation tools:

```bash
git clone https://github.com/drosenman/chemhelper.git
cd chemhelper
pip install -e ".[test,docs]"
```

See [Contributing](../project/contributing.md) for the rest of the workflow.
