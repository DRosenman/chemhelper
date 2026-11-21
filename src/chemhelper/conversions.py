"""Conversions between grams, moles and molarity."""

from chemhelper import compounds


def _fmt(value):
    """Format a quantity for a printed solution, to 4 significant figures."""
    return "{:.4g}".format(value)


def grams_to_moles(mass, chemical):
    """Convert a mass of a substance to moles.

    Parameters
    ----------
    mass : float
        Mass of the sample in grams.
    chemical : str
        Chemical formula of the substance.

    Returns
    -------
    float
        Moles, rounded to 2 decimals.

    Examples
    --------
    >>> grams_to_moles(36.04, 'H2O')
    2.0
    """
    return round(mass / compounds.mass(chemical), 2)


def grams_to_moles_steps(mass, chemical):
    """Print the grams-to-moles conversion.

    Parameters
    ----------
    mass : float
        Mass of the sample in grams.
    chemical : str
        Chemical formula of the substance.

    Examples
    --------
    >>> grams_to_moles_steps(36.04, 'H2O')
    36.04g H2O x 1 mole H2O/18.02g H2O = 2.0 moles H2O
    """
    print("{}g {} x 1 mole {}/{}g {} = {} moles {}".format(
        mass, chemical, chemical, compounds.mass(chemical), chemical,
        grams_to_moles(mass, chemical), chemical))


def moles_to_grams(moles, chemical):
    """Convert moles of a substance to grams.

    Parameters
    ----------
    moles : float
        Amount of substance in moles.
    chemical : str
        Chemical formula of the substance.

    Returns
    -------
    float
        Mass in grams, rounded to 2 decimals.

    Examples
    --------
    >>> moles_to_grams(2, 'H2O')
    36.04
    """
    return round(moles * compounds.mass(chemical), 2)


def moles_to_grams_steps(moles, chemical):
    """Print the molar mass calculation and the moles-to-grams conversion.

    Parameters
    ----------
    moles : float
        Amount of substance in moles.
    chemical : str
        Chemical formula of the substance.
    """
    compounds.mass_steps(chemical)
    print("{} moles x {:.2f} grams/mole = {:.2f} grams".format(
        _fmt(moles), compounds.mass(chemical), moles_to_grams(moles, chemical)))


def molarity(volume, mass=None, chemical=None, moles=None):
    """Molarity (moles of solute per liter of solution).

    Give either ``moles``, or ``mass`` together with ``chemical``.

    Parameters
    ----------
    volume : float
        Volume of solution in liters.
    mass : float, optional
        Mass of solute in grams.
    chemical : str, optional
        Chemical formula of the solute (required with ``mass``).
    moles : float, optional
        Moles of solute.

    Returns
    -------
    float
        Molarity in mol/L.

    Raises
    ------
    ValueError
        If neither ``moles`` nor both ``mass`` and ``chemical`` are given.

    Examples
    --------
    >>> molarity(0.5, moles=1)
    2.0
    >>> molarity(2, mass=58.44, chemical='NaCl')
    0.5
    """
    if moles is None:
        if mass is None or chemical is None:
            raise ValueError("Give either moles, or both mass and chemical.")
        moles = mass / compounds.mass(chemical)
    return moles / volume


def molarity_steps(volume, mass=None, chemical=None, moles=None):
    """Print a step-by-step molarity calculation.

    Takes the same arguments as :func:`molarity`.
    """
    M = molarity(volume, mass, chemical, moles)
    if moles is None:
        moles = mass / compounds.mass(chemical)
        print("{}g {} x 1 mole {}/{}g {} = {} moles {}".format(
            mass, chemical, chemical, compounds.mass(chemical), chemical, _fmt(moles), chemical))
    print("{} moles/{} L = {} M".format(_fmt(moles), _fmt(volume), _fmt(M)))


def molarity_to_moles(M, volume):
    """Moles of solute in a volume of solution.

    Parameters
    ----------
    M : float
        Concentration in mol/L.
    volume : float
        Volume of solution in liters.

    Returns
    -------
    float
        Moles of solute.

    Examples
    --------
    >>> molarity_to_moles(2, 0.5)
    1.0
    """
    return M * volume


def molarity_to_moles_steps(M, volume):
    """Print the molarity-to-moles conversion.

    Takes the same arguments as :func:`molarity_to_moles`.
    """
    print("{} moles/L x {} L = {} moles".format(_fmt(M), _fmt(volume), _fmt(molarity_to_moles(M, volume))))


def molarity_to_grams(molarity, volume, chemical):
    """Grams of solute in a volume of solution.

    Parameters
    ----------
    molarity : float
        Concentration in mol/L.
    volume : float
        Volume of solution in liters.
    chemical : str
        Chemical formula of the solute.

    Returns
    -------
    float
        Mass of solute in grams, rounded to 2 decimals.

    Examples
    --------
    >>> molarity_to_grams(0.5, 2, 'NaCl')
    58.44
    """
    return round(compounds.mass(chemical) * molarity * volume, 2)


def molarity_to_grams_steps(molarity, volume, chemical):
    """Print the molarity-to-grams conversion.

    Takes the same arguments as :func:`molarity_to_grams`.
    """
    molarity_to_moles_steps(molarity, volume)
    moles_to_grams_steps(molarity_to_moles(molarity, volume), chemical)
