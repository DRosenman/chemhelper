# Gas law problems

Six problems that cover the common shapes an ideal gas question takes. Each
uses `ideal_gas` and, where the question involves a mass, a function from
`conversions` or `compounds`.

```pycon
>>> from chemhelper import compounds, conversions, ideal_gas
```

## 1. Volume at standard temperature and pressure

> What volume do 2.50 mol of nitrogen gas occupy at 0 °C and 1 atm?

```pycon
>>> ideal_gas.ideal_gas('V', n=2.50, P=1, T=0, Tunits='C')
56.06
>>> ideal_gas.ideal_gas_steps('V', n=2.50, P=1, T=0, Tunits='C')
T = (0 + 273.15) K = 273.15 K
PV = nRT
V = nRT/P
V = 2.5 moles x 0.0821 L*atm/(mol*K) x 273.15 K / 1 atm = 56.06 L
```

The identity of the gas does not matter here. For an ideal gas, the volume
depends only on the number of moles.

## 2. Pressure from a mass of gas

> A 10.0 L tank holds 64.0 g of oxygen gas at 25 °C. What is the pressure?

The amount is given as a mass, so pass it as `m` and name the gas. Oxygen gas
is O₂.

```pycon
>>> ideal_gas.ideal_gas('P', substance='O2', m=64.0, V=10.0, T=25, Tunits='C')
4.9
>>> ideal_gas.ideal_gas_steps('P', substance='O2', m=64.0, V=10.0, T=25, Tunits='C')
n = 64.0g x 1 mole O2/32.0g O2 = 2 moles O2
T = (25 + 273.15) K = 298.15 K
PV = nRT
P = nRT/V
P = 2 moles x 0.0821 L*atm/(mol*K) x 298.15 K / 10 L = 4.9 atm
```

The answer is in atm. In kilopascals:

```pycon
>>> p = ideal_gas.ideal_gas('P', substance='O2', m=64.0, V=10.0, T=25, Tunits='C')
>>> round(p * 101.325, 1)
496.5
```

## 3. Mass of gas from pressure, volume and temperature

> How many grams of carbon dioxide are in a 5.00 L flask at 740 torr and
> 22 °C?

`ideal_gas` solves for moles, not mass. Solve for moles first, asking for
extra decimals so the next step is not working from a rounded number:

```pycon
>>> n = ideal_gas.ideal_gas('n', P=740, Punits='torr', V=5.00, T=22, Tunits='C', decimals=4)
>>> n
0.2009
```

Then convert moles to grams:

```pycon
>>> conversions.moles_to_grams(n, 'CO2')
8.84
```

The two worked solutions, one after the other:

```pycon
>>> ideal_gas.ideal_gas_steps('n', P=740, Punits='torr', V=5.00, T=22, Tunits='C', decimals=4)
P = 740 torr = 0.973684 atm
T = (22 + 273.15) K = 295.15 K
PV = nRT
n = PV/RT
n = (0.973684 atm x 5 L) / (0.0821 L*atm/(mol*K) x 295.15 K) = 0.2009 moles
>>> conversions.moles_to_grams_steps(n, 'CO2')
CO2
C: 12.01
O: 2 x 16.0 = 32.0

Mass CO2 = 12.01 + 32.0 = 44.01
0.2009 moles x 44.01 grams/mole = 8.84 grams
```

## 4. Temperature

> To what temperature must 0.500 mol of gas be heated to fill a 15.0 L
> container at 1.00 atm?

```pycon
>>> t = ideal_gas.ideal_gas('T', P=1.00, V=15.0, n=0.500)
>>> t
365.41
```

The result is in kelvin. In Celsius:

```pycon
>>> round(t - 273.15, 2)
92.26
```

## 5. Identify an unknown gas

> 1.25 g of an unknown gas occupies 1.00 L at 0 °C and 1.00 atm. Is the gas
> N₂, O₂ or CO₂?

Find the moles of gas from P, V and T. Then the molar mass is the mass
divided by the moles.

```pycon
>>> n = ideal_gas.ideal_gas('n', P=1.00, V=1.00, T=0, Tunits='C', decimals=5)
>>> n
0.04459
>>> round(1.25 / n, 1)
28.0
```

Compare with the candidates:

```pycon
>>> {gas: compounds.mass(gas) for gas in ['N2', 'O2', 'CO2']}
{'N2': 28.02, 'O2': 32.0, 'CO2': 44.01}
```

The unknown gas is nitrogen.

!!! note "Carbon monoxide has the same molar mass"
    CO would match as well:

    ```pycon
    >>> compounds.mass('CO')
    28.01
    ```

    A molar mass narrows the options but cannot always decide between them.

## 6. Changing conditions

> A balloon holds 2.00 L of helium at 25 °C and 1.00 atm. What is its volume
> at −10 °C and 0.700 atm?

The amount of gas is constant. Find it from the first set of conditions, then
use it with the second:

```pycon
>>> n = ideal_gas.ideal_gas('n', P=1.00, V=2.00, T=25, Tunits='C', decimals=5)
>>> ideal_gas.ideal_gas('V', n=n, P=0.700, T=-10, Tunits='C')
2.52
```

This is the combined gas law, \(P_1 V_1 / T_1 = P_2 V_2 / T_2\), done by way
of the moles.

## Checklist for gas problems

1. **Decide what you are solving for.** That is `solve_for`.
2. **List the three known quantities.** If one is a mass, use `m` and
   `substance`.
3. **Note the units of each input** and set `Punits`, `Vunits` and `Tunits`
   if they are not atm, L and K.
4. **Read the answer in atm, L, mol or K** and convert if the question asks
   for something else.
5. **Keep extra decimals** with `decimals=` when the result feeds another
   calculation.
