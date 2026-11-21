# A tutoring session

chemhelper was written for this situation: a student brings you a problem and
their attempt at it. You want to know quickly whether each answer is right,
and if not, exactly where the work went off course.

```pycon
>>> from chemhelper import compounds, conversions
```

## The problem

> Ammonium nitrate, NH₄NO₃, is a common fertilizer.
>
> 1. What is the percent by mass of nitrogen in ammonium nitrate?
> 2. How many moles are in a 25.0 g sample?
> 3. If that sample is dissolved in enough water to make 500 mL of solution,
>    what is the molarity?

The student's answers are **17.5 %**, **0.31 mol** and **0.62 M**.

## Part 1: percent nitrogen

Check the answer first.

```pycon
>>> compounds.percent_composition('NH4NO3')
N          35.002
H           5.037
O          59.961
Total:    100.000
Name: NH4NO3, dtype: float64
```

The student said 17.5 %, which is half of the correct value. That is a strong
hint. Print the solution to see the structure of the calculation:

```pycon
>>> compounds.percent_composition_steps('NH4NO3')
NH4NO3
N: 2 x 14.01 = 28.02
H: 4 x 1.008 = 4.032
O: 3 x 16.0 = 48.0

Mass NH4NO3 = 28.02 + 4.032 + 48.0 = 80.05

N         28.020
H          4.032
O         48.000
Total:    80.050
Name: NH4NO3, dtype: float64
N: 100 x 28.02g N/80.05g NH4NO3 = 35.00%
H: 100 x 4.032g H/80.05g NH4NO3 = 5.04%
O: 100 x 48.0g O/80.05g NH4NO3 = 59.96%
```

The first lines show it: nitrogen appears **twice** in NH₄NO₃, once in the
ammonium ion and once in the nitrate ion, so its contribution is
2 × 14.01. The student counted one nitrogen.

You can confirm how the formula is read:

```pycon
>>> dict(compounds.parse_formula('NH4NO3'))
{'N': 2, 'H': 4, 'O': 3}
```

!!! tip "Teaching point"
    Ask the student to count the atoms of each element before doing any
    arithmetic. `parse_formula` gives you the count to compare against.

## Part 2: grams to moles

```pycon
>>> conversions.grams_to_moles(25.0, 'NH4NO3')
0.31
```

The student's 0.31 mol is correct. If they want to see it laid out anyway:

```pycon
>>> conversions.grams_to_moles_steps(25.0, 'NH4NO3')
25.0g NH4NO3 x 1 mole NH4NO3/80.05g NH4NO3 = 0.31 moles NH4NO3
```

Notice that the molar mass in this step was right, even though part 1 was
wrong. The student can find a molar mass. The slip in part 1 was specific to
picking out nitrogen's share of it.

## Part 3: molarity

The volume must be in liters: 500 mL is 0.500 L.

```pycon
>>> conversions.molarity(0.500, mass=25.0, chemical='NH4NO3')
0.6246096189881324
>>> conversions.molarity_steps(0.500, mass=25.0, chemical='NH4NO3')
25.0g NH4NO3 x 1 mole NH4NO3/80.05g NH4NO3 = 0.3123 moles NH4NO3
0.3123 moles/0.5 L = 0.6246 M
```

The student's 0.62 M matches.

!!! note "Why 0.31 mol in part 2 but 0.3123 mol here"
    `grams_to_moles` rounds its answer to two decimals. `molarity` carries
    the unrounded moles through to the end, and its printed solution shows
    four significant figures. See
    [Units and rounding](../getting-started/units-and-rounding.md).

## What the session looked like

| Part | Student | Verdict |
| --- | --- | --- |
| 1. Percent N | 17.5 % | Wrong: counted one N, not two |
| 2. Moles | 0.31 mol | Correct |
| 3. Molarity | 0.62 M | Correct |

Three checks and one diagnosis took a handful of lines. The rest of the
session can go to the idea the student actually needs: reading a formula that
contains the same element in two places.

## The pattern

1. **Check** with the plain function.
2. If the answer is wrong, **print** the solution with the `_steps` twin.
3. **Compare** line by line with the student's work to find the first
   difference.
4. Use `parse_formula` when the disagreement starts at the formula itself.
