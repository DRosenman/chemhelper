# Preparing solutions

Three tasks come up again and again at the bench: making a solution of a
known concentration, checking the concentration of a solution you made, and
diluting a stock solution.

```pycon
>>> from chemhelper import compounds, conversions
```

All volumes in `conversions` are in **liters**.

## Make a solution of a target concentration

> You need 250 mL of 0.100 M sodium hydroxide. How many grams of NaOH do you
> weigh out?

Convert the volume to liters (0.250 L), then ask for the grams of solute:

```pycon
>>> conversions.molarity_to_grams(0.100, 0.250, 'NaOH')
1.0
```

The worked solution shows the three steps: moles needed, the molar mass of
NaOH, and the mass:

```pycon
>>> conversions.molarity_to_grams_steps(0.100, 0.250, 'NaOH')
0.1 moles/L x 0.25 L = 0.025 moles
NaOH
Na: 22.99
O: 16.0
H: 1.008

Mass NaOH = 22.99 + 16.0 + 1.008 = 40.0
0.025 moles x 40.00 grams/mole = 1.00 grams
```

So you would dissolve that mass of NaOH and add water until the total volume
is 250 mL.

!!! warning "Fill to the mark"
    Molarity is moles per liter of **solution**. Add water up to a final
    volume of 250 mL. Do not add 250 mL of water to the solid.

## Check the concentration of a solution

> You dissolved 5.85 g of NaCl and made the volume up to 500 mL. What is the
> molarity?

```pycon
>>> conversions.molarity(0.500, mass=5.85, chemical='NaCl')
0.2002053388090349
>>> conversions.molarity_steps(0.500, mass=5.85, chemical='NaCl')
5.85g NaCl x 1 mole NaCl/58.44g NaCl = 0.1001 moles NaCl
0.1001 moles/0.5 L = 0.2002 M
```

`molarity` returns the unrounded value. Round it for reporting:

```pycon
>>> round(conversions.molarity(0.500, mass=5.85, chemical='NaCl'), 3)
0.2
```

## How many moles are in a sample of solution?

> How many moles of HCl are in 25.0 mL of 0.150 M hydrochloric acid?

```pycon
>>> round(conversions.molarity_to_moles(0.150, 0.0250), 5)
0.00375
>>> conversions.molarity_to_moles_steps(0.150, 0.0250)
0.15 moles/L x 0.025 L = 0.00375 moles
```

This is the first step of most titration calculations.

## Dilute a stock solution

> 50.0 mL of 2.00 M HCl is diluted to a final volume of 400 mL. What is the
> new concentration?

Dilution adds water but not solute, so the moles of HCl stay the same. Find
them from the stock solution, then divide by the new volume:

```pycon
>>> moles = conversions.molarity_to_moles(2.00, 0.0500)
>>> moles
0.1
>>> conversions.molarity(0.400, moles=moles)
0.25
```

This is the same calculation as the dilution equation
\(M_1 V_1 = M_2 V_2\), done in two visible steps.

### How much stock do I need?

> What volume of 12.0 M HCl is needed to make 1.00 L of 0.500 M HCl?

Work backwards: find the moles the final solution must contain, then the
volume of stock that holds that many moles.

```pycon
>>> moles_needed = conversions.molarity_to_moles(0.500, 1.00)
>>> moles_needed
0.5
>>> liters_of_stock = moles_needed / 12.0
>>> round(liters_of_stock * 1000, 1)
41.7
```

That is the volume of concentrated acid, in milliliters, to dilute to 1.00 L.

## A titration, start to finish

> 25.0 mL of sulfuric acid is neutralized by 32.4 mL of 0.100 M NaOH. What is
> the concentration of the acid?
>
> H₂SO₄ + 2 NaOH → Na₂SO₄ + 2 H₂O

Moles of base used:

```pycon
>>> moles_naoh = conversions.molarity_to_moles(0.100, 0.0324)
>>> round(moles_naoh, 5)
0.00324
```

The balanced equation says one mole of acid reacts with two moles of base.
chemhelper does not read equations, so apply that ratio yourself:

```pycon
>>> moles_h2so4 = moles_naoh / 2
```

Concentration of the acid:

```pycon
>>> round(conversions.molarity(0.0250, moles=moles_h2so4), 4)
0.0648
```

## Mass of solute in a bottle

> A 2.00 L bottle is labeled 0.250 M glucose, C₆H₁₂O₆. How many grams of
> glucose does it contain?

```pycon
>>> conversions.molarity_to_grams(0.250, 2.00, 'C6H12O6')
90.08
```

## Summary

| Question | Function |
| --- | --- |
| How many grams for this concentration and volume? | `molarity_to_grams` |
| What is the molarity of what I made? | `molarity` with `mass` and `chemical` |
| How many moles are in this volume? | `molarity_to_moles` |
| What is the concentration after dilution? | `molarity_to_moles`, then `molarity` with `moles` |
