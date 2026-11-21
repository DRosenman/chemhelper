import pytest

from chemhelper import compounds, conversions, elements, ideal_gas


def test_element_lookup_and_fixes():
    assert elements.elements["O"].mass == 16.00
    assert elements.Tc.symbol == "Tc"
    assert elements.elements["Be"].name == "Beryllium"
    assert len(elements.element_table) == 92
    assert elements.element_table.loc[26, "Symbol"] == "Fe"


@pytest.mark.parametrize("formula, expected", [
    ("H2O", 18.02), ("NaCl", 58.44), ("C6H12O6", 180.16),
    ("Ca(OH)2", 74.10), ("Al2(SO4)3", 342.17), ("CH3COOH", 60.05),
])
def test_mass(formula, expected):
    assert compounds.mass(formula) == pytest.approx(expected, abs=0.01)


def test_parse_merges_repeated_elements():
    assert dict(compounds.parse_formula("CH3COOH")) == {"C": 2, "H": 4, "O": 2}
    assert dict(compounds.parse_formula("K4[Fe(CN)6]")) == {"K": 4, "Fe": 1, "C": 6, "N": 6}


@pytest.mark.parametrize("bad", ["Xx2", "Ca(OH", "H2O)", "h2o", "", "H2O!"])
def test_parse_errors(bad):
    with pytest.raises(ValueError):
        compounds.parse_formula(bad)


def test_composition_unique_index():
    comp = compounds.composition("CH3COOH")
    assert list(comp.index) == ["C", "H", "O", "Total:"]
    assert comp.drop("Total:").sum() == pytest.approx(comp["Total:"], abs=0.01)


def test_percent_composition_sums_to_100():
    pc = compounds.percent_composition("C6H12O6")
    assert pc.drop("Total:").sum() == pytest.approx(100, abs=0.01)


def test_conversions():
    assert conversions.grams_to_moles(36.04, "H2O") == 2.0
    assert conversions.moles_to_grams(2, "H2O") == 36.04
    assert conversions.molarity(2, mass=58.44, chemical="NaCl") == pytest.approx(0.5)
    assert conversions.molarity_to_grams(0.5, 2, "NaCl") == 58.44
    with pytest.raises(ValueError):
        conversions.molarity(1, mass=10)


def test_ideal_gas_solves_each_variable():
    assert ideal_gas.ideal_gas("V", n=1, T=273.15, P=1) == 22.43
    assert ideal_gas.ideal_gas("P", n=1, T=273.15, V=22.43) == pytest.approx(1, abs=0.01)
    assert ideal_gas.ideal_gas("n", P=1, V=22.43, T=273.15) == pytest.approx(1, abs=0.01)
    t = ideal_gas.ideal_gas("T", P=1, V=22.43, n=1)
    assert isinstance(t, float) and t == pytest.approx(273.2, abs=0.1)


def test_ideal_gas_units():
    base = ideal_gas.ideal_gas("n", P=1, V=1, T=298.15)
    assert ideal_gas.ideal_gas("n", P=760, Punits="torr", V=1000, Vunits="mL", T=25, Tunits="C") == base
    assert ideal_gas.ideal_gas("n", P=101.325, Punits="kPa", V=1, T=298.15) == base


def test_ideal_gas_errors():
    with pytest.raises(ValueError):
        ideal_gas.ideal_gas("X", P=1, V=1, T=1)
    with pytest.raises(ValueError):
        ideal_gas.ideal_gas("P", V=1, T=300)


def test_steps_functions_print(capsys):
    compounds.percent_composition_steps("H2O")
    conversions.molarity_steps(1, mass=58.44, chemical="NaCl")
    conversions.molarity_to_grams_steps(0.5, 2, "NaCl")
    ideal_gas.ideal_gas_steps("T", P=760, Punits="torr", V=22430, Vunits="mL", n=1)
    out = capsys.readouterr().out
    assert "Mass H2O" in out and "= 1 M" in out and "K" in out


def test_steps_show_small_amounts(capsys):
    conversions.molarity_to_moles_steps(0.150, 0.0250)
    conversions.molarity_to_grams_steps(0.100, 0.250, "NaOH")
    conversions.molarity_steps(0.5, mass=25.0, chemical="NH4NO3")
    out = capsys.readouterr().out
    assert "0.15 moles/L x 0.025 L = 0.00375 moles" in out
    assert "0.025 moles x 40.00 grams/mole = 1.00 grams" in out
    assert "0.3123 moles/0.5 L = 0.6246 M" in out
