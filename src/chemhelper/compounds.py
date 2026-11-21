"""Molar mass and composition of chemical compounds.

Formulas are written the usual way, with case-sensitive symbols and optional
counts: ``'H2O'``, ``'C6H12O6'``, ``'Ca(OH)2'``, ``'CH3COOH'``. Parentheses
and square brackets may be nested.
"""

import re
from collections import OrderedDict

import pandas as pd

from chemhelper import elements

_TOKEN = re.compile(r"([A-Z][a-z]?)(\d*)|([(\[])|([)\]])(\d*)|(\s+)")


def parse_formula(chemical):
    """Count the atoms of each element in a formula.

    Parameters
    ----------
    chemical : str
        Chemical formula, e.g. ``'Ca(OH)2'``.

    Returns
    -------
    collections.OrderedDict
        Element symbol -> number of atoms, in order of first appearance.

    Raises
    ------
    ValueError
        If the formula contains an unknown element, unbalanced parentheses
        or characters that are not part of a formula.

    Examples
    --------
    >>> dict(parse_formula('Ca(OH)2'))
    {'Ca': 1, 'O': 2, 'H': 2}
    """
    stack = [OrderedDict()]
    pos = 0
    while pos < len(chemical):
        m = _TOKEN.match(chemical, pos)
        if not m:
            raise ValueError("Unexpected character {!r} in formula {!r}".format(chemical[pos], chemical))
        symbol, count, opening, closing, group_count, _ = m.groups()
        if symbol:
            if symbol not in elements.elements.index:
                raise ValueError("Unknown element {!r} in formula {!r}".format(symbol, chemical))
            stack[-1][symbol] = stack[-1].get(symbol, 0) + int(count or 1)
        elif opening:
            stack.append(OrderedDict())
        elif closing:
            if len(stack) == 1:
                raise ValueError("Unbalanced parentheses in formula {!r}".format(chemical))
            group = stack.pop()
            for sym, n in group.items():
                stack[-1][sym] = stack[-1].get(sym, 0) + n * int(group_count or 1)
        pos = m.end()
    if len(stack) != 1:
        raise ValueError("Unbalanced parentheses in formula {!r}".format(chemical))
    if not stack[0]:
        raise ValueError("Empty formula {!r}".format(chemical))
    return stack[0]


def _element_masses(chemical):
    """Unrounded mass contributed by each element, in g/mol."""
    return OrderedDict(
        (sym, elements.elements[sym].mass * n) for sym, n in parse_formula(chemical).items()
    )


def _molar_mass(chemical):
    return sum(_element_masses(chemical).values())


def mass(chemical):
    """Molar mass of a compound.

    Parameters
    ----------
    chemical : str
        Chemical formula, e.g. ``'H2O'``.

    Returns
    -------
    float
        Molar mass in g/mol, rounded to 2 decimals.

    Examples
    --------
    >>> mass('H2O')
    18.02
    >>> mass('Ca(OH)2')
    74.1
    """
    return round(_molar_mass(chemical), 2)


def mass_steps(chemical):
    """Print a step-by-step molar mass calculation.

    Parameters
    ----------
    chemical : str
        Chemical formula, e.g. ``'H2O'``.

    Examples
    --------
    >>> mass_steps('H2O')
    H2O
    H: 2 x 1.008 = 2.016
    O: 16.0
    <BLANKLINE>
    Mass H2O = 2.016 + 16.0 = 18.02
    """
    print(chemical)
    parts = []
    for sym, n in parse_formula(chemical).items():
        m = elements.elements[sym].mass
        if n == 1:
            print("{}: {}".format(sym, m))
            parts.append(m)
        else:
            print("{}: {} x {} = {}".format(sym, n, m, round(m * n, 4)))
            parts.append(round(m * n, 4))
    print("\nMass {} = {} = {}".format(chemical, " + ".join(str(p) for p in parts), mass(chemical)))


def composition(chemical):
    """Mass contributed by each element in one mole of a compound.

    Parameters
    ----------
    chemical : str
        Chemical formula, e.g. ``'H2O'``.

    Returns
    -------
    pandas.Series
        Grams of each element per mole of compound, plus a ``'Total:'`` entry
        holding the molar mass. Named after the formula.

    Examples
    --------
    >>> composition('H2O').to_dict()
    {'H': 2.016, 'O': 16.0, 'Total:': 18.02}
    """
    contrib = _element_masses(chemical)
    index = list(contrib) + ["Total:"]
    values = [round(v, 4) for v in contrib.values()] + [mass(chemical)]
    return pd.Series(values, index=index, name=chemical)


def composition_steps(chemical):
    """Print the molar mass calculation followed by :func:`composition`.

    Parameters
    ----------
    chemical : str
        Chemical formula, e.g. ``'H2O'``.
    """
    mass_steps(chemical)
    print("")
    print(composition(chemical))


def percent_composition(chemical):
    """Percent by mass of each element in a compound.

    Parameters
    ----------
    chemical : str
        Chemical formula, e.g. ``'H2O'``.

    Returns
    -------
    pandas.Series
        Percent of each element, rounded to 3 decimals, plus ``'Total:'``
        (always 100).

    Examples
    --------
    >>> percent_composition('H2O').to_dict()
    {'H': 11.19, 'O': 88.81, 'Total:': 100.0}
    """
    contrib = _element_masses(chemical)
    total = sum(contrib.values())
    values = [round(v / total * 100, 3) for v in contrib.values()] + [100.0]
    return pd.Series(values, index=list(contrib) + ["Total:"], name=chemical)


def percent_composition_steps(chemical):
    """Print a step-by-step percent composition calculation.

    Parameters
    ----------
    chemical : str
        Chemical formula, e.g. ``'H2O'``.
    """
    composition_steps(chemical)
    percents = percent_composition(chemical)
    total = mass(chemical)
    for sym, el_mass in _element_masses(chemical).items():
        print("{}: 100 x {}g {}/{}g {} = {:.2f}%".format(
            sym, round(el_mass, 4), sym, total, chemical, percents[sym]))
