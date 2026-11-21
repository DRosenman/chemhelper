"""Ideal gas law, PV = nRT."""

from chemhelper import compounds

R = 0.0821
"""Gas constant in L·atm/(mol·K)."""

_P_TO_ATM = {"atm": 1.0, "torr": 1 / 760, "mmHg": 1 / 760, "kPa": 1 / 101.325}
_V_TO_L = {"L": 1.0, "mL": 1 / 1000}


def _prepare(solve_for, substance, P, V, n, T, m, Tunits, Vunits, Punits, show):
    """Validate inputs and convert them to atm, L, K and moles."""
    if solve_for not in ("P", "V", "n", "T"):
        raise ValueError("solve_for must be 'P', 'V', 'n' or 'T', not {!r}".format(solve_for))
    if Punits not in _P_TO_ATM:
        raise ValueError("Punits must be one of {}".format(sorted(_P_TO_ATM)))
    if Vunits not in _V_TO_L:
        raise ValueError("Vunits must be one of {}".format(sorted(_V_TO_L)))
    if Tunits not in ("K", "C"):
        raise ValueError("Tunits must be 'K' or 'C'")

    if solve_for != "n" and n is None and m is not None:
        if substance is None:
            raise ValueError("substance is required when giving the mass m")
        n = m / compounds.mass(substance)
        if show:
            print("n = {}g x 1 mole {}/{}g {} = {:.6g} moles {}".format(
                m, substance, compounds.mass(substance), substance, n, substance))

    known = {"P": P, "V": V, "n": n, "T": T}
    missing = [k for k, v in known.items() if k != solve_for and v is None]
    if missing:
        raise ValueError("Missing value(s) for: {}".format(", ".join(missing)))

    if solve_for != "P" and Punits != "atm":
        atm = P * _P_TO_ATM[Punits]
        if show:
            print("P = {} {} = {:.6g} atm".format(P, Punits, atm))
        P = atm
    if solve_for != "V" and Vunits != "L":
        liters = V * _V_TO_L[Vunits]
        if show:
            print("V = {} {} x 1 L/1000 mL = {:.6g} L".format(V, Vunits, liters))
        V = liters
    if solve_for != "T" and Tunits == "C":
        kelvin = T + 273.15
        if show:
            print("T = ({} + 273.15) K = {:.2f} K".format(T, kelvin))
        T = kelvin
    return P, V, n, T


def _solve(solve_for, P, V, n, T):
    if solve_for == "P":
        return n * R * T / V
    if solve_for == "V":
        return n * R * T / P
    if solve_for == "n":
        return P * V / (R * T)
    return P * V / (n * R)


def ideal_gas(solve_for, substance=None, P=None, V=None, n=None, T=None, m=None, decimals=2,
              Tunits="K", Vunits="L", Punits="atm"):
    """Solve PV = nRT for one variable.

    Give every variable except ``solve_for``. Instead of ``n`` you may give the
    mass ``m`` together with ``substance``.

    Parameters
    ----------
    solve_for : {'P', 'V', 'n', 'T'}
        The variable to solve for.
    substance : str, optional
        Chemical formula of the gas; needed only with ``m``.
    P : float, optional
        Pressure, in ``Punits``.
    V : float, optional
        Volume, in ``Vunits``.
    n : float, optional
        Amount of gas in moles.
    T : float, optional
        Temperature, in ``Tunits``.
    m : float, optional
        Mass of gas in grams (used to compute ``n``).
    decimals : int, default 2
        Decimal places in the result.
    Tunits : {'K', 'C'}, default 'K'
        Units of the given ``T``.
    Vunits : {'L', 'mL'}, default 'L'
        Units of the given ``V``.
    Punits : {'atm', 'torr', 'mmHg', 'kPa'}, default 'atm'
        Units of the given ``P``.

    Returns
    -------
    float
        The solved value, in atm (P), L (V), mol (n) or K (T).

    Raises
    ------
    ValueError
        For an invalid ``solve_for`` or unit, or a missing input.

    Examples
    --------
    >>> ideal_gas('V', n=1, T=273.15, P=1)
    22.43
    >>> ideal_gas('P', substance='O2', m=32, V=500, Vunits='mL', T=25, Tunits='C')
    48.96
    """
    P, V, n, T = _prepare(solve_for, substance, P, V, n, T, m, Tunits, Vunits, Punits, show=False)
    return round(_solve(solve_for, P, V, n, T), decimals)


def ideal_gas_steps(solve_for, substance=None, P=None, V=None, n=None, T=None, m=None, decimals=2,
                    Tunits="K", Vunits="L", Punits="atm"):
    """Print a step-by-step ideal gas law solution.

    Takes the same arguments as :func:`ideal_gas`.

    Examples
    --------
    >>> ideal_gas_steps('V', n=1, T=273.15, P=1)
    PV = nRT
    V = nRT/P
    V = 1 moles x 0.0821 L*atm/(mol*K) x 273.15 K / 1 atm = 22.43 L
    """
    P, V, n, T = _prepare(solve_for, substance, P, V, n, T, m, Tunits, Vunits, Punits, show=True)
    result = round(_solve(solve_for, P, V, n, T), decimals)
    g = lambda x: "{:.6g}".format(x)  # noqa: E731
    print("PV = nRT")
    if solve_for == "P":
        print("P = nRT/V")
        print("P = {} moles x 0.0821 L*atm/(mol*K) x {} K / {} L = {} atm".format(g(n), g(T), g(V), result))
    elif solve_for == "V":
        print("V = nRT/P")
        print("V = {} moles x 0.0821 L*atm/(mol*K) x {} K / {} atm = {} L".format(g(n), g(T), g(P), result))
    elif solve_for == "n":
        print("n = PV/RT")
        print("n = ({} atm x {} L) / (0.0821 L*atm/(mol*K) x {} K) = {} moles".format(g(P), g(V), g(T), result))
    else:
        print("T = PV/nR")
        print("T = ({} atm x {} L) / ({} moles x 0.0821 L*atm/(mol*K)) = {} K".format(g(P), g(V), g(n), result))
