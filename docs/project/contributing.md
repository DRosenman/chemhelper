# Contributing

Bug reports, corrections to the chemistry, documentation fixes and new
solvers are all welcome.

## Report a problem

Open an [issue](https://github.com/drosenman/chemhelper/issues) with:

- the code you ran,
- what you expected,
- what you got, including the full error message if there was one.

If chemhelper gives a wrong chemistry answer, a textbook reference for the
right one helps a great deal.

## Set up for development

```bash
git clone https://github.com/drosenman/chemhelper.git
cd chemhelper
pip install -e ".[test,docs]"
```

The `-e` flag installs the package in editable mode, so your changes take
effect without reinstalling.

## Project layout

```
chemhelper/
├── src/chemhelper/        the package
│   ├── elements.py        periodic table data
│   ├── compounds.py       formula parsing, molar mass, composition
│   ├── conversions.py     grams, moles, molarity
│   └── ideal_gas.py       PV = nRT
├── tests/                 the test suite
├── docs/                  this documentation, in Markdown
├── tools/
│   ├── docs_examples.py           runs every example in the docs
│   └── make_periodic_table.py     generates the periodic table page
├── mkdocs.yml             documentation site configuration
├── pyproject.toml         package metadata
└── CHANGELOG.md
```

## Run the tests

```bash
pytest
```

This runs the tests in `tests/` and every example in the docstrings.

## Work on the documentation

Preview the site locally. It reloads as you edit:

```bash
mkdocs serve
```

### Examples are executed, not typed

Every example in the docs is a fenced `pycon` block. You write only the input
lines, the ones that start with `>>>`. A script runs them against the real
package and fills in the output.

After adding or changing an example, or changing the code's behavior:

```bash
python tools/docs_examples.py --write
```

To check that every example is up to date without changing anything:

```bash
python tools/docs_examples.py
```

The check runs in CI, so documentation cannot drift from the code.

Each page gets one fresh Python session. An import at the top of a page is
available to every block below it.

### The periodic table page

`docs/periodic-table.md` is generated from the element data. After changing
`elements.py`, regenerate it:

```bash
python tools/make_periodic_table.py
```

## Add a solver

New solvers follow one pattern.

1. **Write the function that returns the answer.** Give it a NumPy-style
   docstring with `Parameters`, `Returns`, `Raises` and `Examples` sections.
   Validate the inputs and raise `ValueError` with a message that says what
   is wrong.
2. **Write the `_steps` twin.** It takes the same arguments, prints the
   solution with units, and returns nothing. Its final number must equal what
   the first function returns.
3. **Round only the final result.** Carry full precision through
   intermediate steps.
4. **Add tests** in `tests/` for typical values, edge cases and each error.
5. **Document it**: a section in the module's page under `docs/guide/`, a row
   in the tables in `docs/guide/index.md` and
   `docs/getting-started/steps.md`, and a line in `CHANGELOG.md`.

## Style

- Follow PEP 8. Lines up to 110 characters are fine.
- Name arguments after the chemistry: `mass`, `moles`, `volume`, `chemical`.
- Keep the dependencies small. The package needs only pandas.

## Send a pull request

1. Create a branch for your change.
2. Make sure `pytest`, `python tools/docs_examples.py` and
   `mkdocs build --strict` all pass.
3. Open a pull request describing what changed and why.

## Release checklist

For maintainers.

1. Update the version in `pyproject.toml` and `src/chemhelper/__init__.py`.
2. Add the release to `CHANGELOG.md`.
3. Run the tests and the documentation check.
4. Build and upload:

    ```bash
    python -m build
    python -m twine upload dist/*
    ```

5. Tag the release:

    ```bash
    git tag v1.0.0
    git push origin v1.0.0
    ```

The documentation site is rebuilt and published automatically on every push
to `master`.
