"""chemhelper: solve introductory chemistry problems, with step-by-step solutions.

Every solver has a ``*_steps`` twin that prints the worked solution.
"""

from chemhelper import compounds, conversions, elements, ideal_gas  # noqa: F401

__version__ = "1.0.0"
__all__ = ["compounds", "conversions", "elements", "ideal_gas", "__version__"]
