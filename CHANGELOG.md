# Changelog

## 1.0.0 — 2026-11-21

### Breaking / behavior changes
- `ideal_gas('T', ...)` now returns a number; it used to return the tuple `(T, 2)`.
- Celsius is converted with 273.15 (was 273.5).
- Intermediate values are no longer rounded, so some results change slightly.
- `moles_to_grams` now rounds to 2 decimals, like the other conversions.
- `composition` and `percent_composition` list each element once, even when it
  appears more than once in the formula (e.g. `CH3COOH`).
- Invalid input raises `ValueError` with a clear message instead of a `KeyError`
  or `TypeError`.

### Added
- A full documentation site: getting started, a guide to every function,
  tutorials, a cookbook, a periodic table page, FAQ and migration notes.
- `tools/docs_examples.py`, which runs every example in the docs and README
  and checks its output.
- Formulas with parentheses and brackets: `Ca(OH)2`, `Al2(SO4)3`, `K4[Fe(CN)6]`.
- `compounds.parse_formula`.
- `ideal_gas`: pressure in `mmHg` and `kPa`; the `decimals` argument now works.
- `chemhelper.__version__`.
- NumPy-style docstrings for every public function; documentation site.
- Test suite and CI.

### Fixed
- Printed solutions show moles, volumes and molarities to four significant
  figures, so small amounts no longer appear as `0.00`.
- Technetium's symbol (`'TC'` → `'Tc'`).
- Spelling of Beryllium, Holmium and Protactinium.
- `ideal_gas_steps` printed a wrongly rounded torr→atm value.

### Packaging
- Requires Python 3.10 or newer.
- `pyproject.toml` with a `src/` layout replaces `setup.py`. The previous
  layout shipped no code because `chemhelper/` did not exist in the repository.
- Old per-version folders (`chemhelper.0.1` … `chemhelper.0.4`) removed; they
  remain in git history.

## 0.4
Last release before 1.0.
