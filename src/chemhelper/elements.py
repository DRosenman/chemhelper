"""Periodic table data for elements 1 (hydrogen) through 92 (uranium).

Attributes
----------
elements : pandas.Series
    :class:`Element` objects indexed by chemical symbol, e.g. ``elements['O']``.
element_index : list of str
    Chemical symbols in order of atomic number.
element_objects : list of Element
    :class:`Element` objects in order of atomic number.
element_table : pandas.DataFrame
    Symbol, name and mass (rounded to 2 decimals), indexed by atomic number.

Every element is also available as a module-level name, e.g. ``elements.Fe``.
"""

import pandas as pd


class Element:
    """A chemical element.

    Parameters
    ----------
    symbol : str
        Chemical symbol, e.g. ``'Na'``.
    name : str
        Element name, e.g. ``'Sodium'``.
    atomic_number : int
        Number of protons.
    mass : float
        Standard atomic mass in g/mol.

    Examples
    --------
    >>> from chemhelper import elements
    >>> elements.elements['Na'].mass
    22.99
    >>> print(elements.Na)
    Element: Sodium, Na
    Atomic Number: 11
    Mass: 22.99
    """

    def __init__(self, symbol, name, atomic_number, mass):
        self.symbol = symbol
        self.name = name
        self.atomic_number = atomic_number
        self.mass = mass

    def __str__(self):
        return "Element: {}, {}\nAtomic Number: {}\nMass: {}".format(
            self.name, self.symbol, self.atomic_number, self.mass
        )

    def __repr__(self):
        return "Element({!r}, {!r}, {}, {})".format(
            self.symbol, self.name, self.atomic_number, self.mass
        )


_DATA = [
    ("H", "Hydrogen", 1.008), ("He", "Helium", 4.0026), ("Li", "Lithium", 6.94),
    ("Be", "Beryllium", 9.01), ("B", "Boron", 10.81), ("C", "Carbon", 12.01),
    ("N", "Nitrogen", 14.01), ("O", "Oxygen", 16.00), ("F", "Fluorine", 19.00),
    ("Ne", "Neon", 20.18), ("Na", "Sodium", 22.99), ("Mg", "Magnesium", 24.31),
    ("Al", "Aluminum", 26.98), ("Si", "Silicon", 28.09), ("P", "Phosphorus", 30.97),
    ("S", "Sulfur", 32.07), ("Cl", "Chlorine", 35.45), ("Ar", "Argon", 39.95),
    ("K", "Potassium", 39.10), ("Ca", "Calcium", 40.08), ("Sc", "Scandium", 44.96),
    ("Ti", "Titanium", 47.87), ("V", "Vanadium", 50.94), ("Cr", "Chromium", 52.00),
    ("Mn", "Manganese", 54.94), ("Fe", "Iron", 55.85), ("Co", "Cobalt", 58.93),
    ("Ni", "Nickel", 58.69), ("Cu", "Copper", 63.55), ("Zn", "Zinc", 65.39),
    ("Ga", "Gallium", 69.72), ("Ge", "Germanium", 72.64), ("As", "Arsenic", 74.92),
    ("Se", "Selenium", 78.96), ("Br", "Bromine", 79.90), ("Kr", "Krypton", 83.80),
    ("Rb", "Rubidium", 85.47), ("Sr", "Strontium", 87.62), ("Y", "Yttrium", 88.91),
    ("Zr", "Zirconium", 91.22), ("Nb", "Niobium", 92.91), ("Mo", "Molybdenum", 95.94),
    ("Tc", "Technetium", 98), ("Ru", "Ruthenium", 101.07), ("Rh", "Rhodium", 102.91),
    ("Pd", "Palladium", 106.42), ("Ag", "Silver", 107.87), ("Cd", "Cadmium", 112.41),
    ("In", "Indium", 114.82), ("Sn", "Tin", 118.71), ("Sb", "Antimony", 121.76),
    ("Te", "Tellurium", 127.60), ("I", "Iodine", 126.90), ("Xe", "Xenon", 131.29),
    ("Cs", "Cesium", 132.91), ("Ba", "Barium", 137.33), ("La", "Lanthanum", 138.91),
    ("Ce", "Cerium", 140.12), ("Pr", "Praseodymium", 140.91), ("Nd", "Neodymium", 144.24),
    ("Pm", "Promethium", 145), ("Sm", "Samarium", 150.36), ("Eu", "Europium", 151.96),
    ("Gd", "Gadolinium", 157.25), ("Tb", "Terbium", 158.93), ("Dy", "Dysprosium", 162.50),
    ("Ho", "Holmium", 164.93), ("Er", "Erbium", 167.26), ("Tm", "Thulium", 168.93),
    ("Yb", "Ytterbium", 173.04), ("Lu", "Lutetium", 174.97), ("Hf", "Hafnium", 178.49),
    ("Ta", "Tantalum", 180.95), ("W", "Tungsten", 183.84), ("Re", "Rhenium", 186.21),
    ("Os", "Osmium", 190.23), ("Ir", "Iridium", 192.22), ("Pt", "Platinum", 195.08),
    ("Au", "Gold", 196.97), ("Hg", "Mercury", 200.59), ("Tl", "Thallium", 204.38),
    ("Pb", "Lead", 207.2), ("Bi", "Bismuth", 208.98), ("Po", "Polonium", 209),
    ("At", "Astatine", 210), ("Rn", "Radon", 222), ("Fr", "Francium", 223),
    ("Ra", "Radium", 226), ("Ac", "Actinium", 227), ("Th", "Thorium", 232.04),
    ("Pa", "Protactinium", 231.04), ("U", "Uranium", 238.03),
]

element_objects = [Element(s, n, i, m) for i, (s, n, m) in enumerate(_DATA, start=1)]
element_index = [e.symbol for e in element_objects]
globals().update({e.symbol: e for e in element_objects})

elements = pd.Series(element_objects, index=element_index)

element_table = pd.DataFrame(
    {
        "Symbol": element_index,
        "Name": [e.name for e in element_objects],
        "Mass": [round(e.mass, 2) for e in element_objects],
    },
    index=range(1, len(element_objects) + 1),
)
element_table.columns.name = "Atomic Number"
