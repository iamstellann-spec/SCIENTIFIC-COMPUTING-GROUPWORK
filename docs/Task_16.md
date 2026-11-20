# Task 16: Numerical Integration

Programs: [`code/Task_16_numerical_integration.py`](../code/Task_16_numerical_integration.py) (original) and [`code/Task_16_numerical_integration_modified.py`](../code/Task_16_numerical_integration_modified.py) (modified)

## Original program output

```text
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule: 15.800 kWh
Difference between estimates: 0.100 kWh
```

## B. Inputs and mathematical operation

**Input values:** smart-meter power readings in kW [0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9] taken every 2 hours from 0 to 12 h.

**Mathematical operations:** energy is the integral of power over time. The trapezoidal rule adds up trapezoids; Simpson's rule fits parabolas through groups of points.

## C. Changing a parameter

**Change made:** the peak reading was changed from 1.8 kW to 2.5 kW.

**Effect:** the energy rose from 15.700 to 17.100 kWh (trapezoid) and from 15.800 to 17.667 kWh (Simpson). The difference between the two methods grew from 0.1 to 0.57 kWh, because a sharper peak is more curved and the trapezoids cut the corner.

## D. Meaning of the output

The household used about 15.7 kWh (trapezoid) or 15.8 kWh (Simpson) over the 12 hours. The two methods differ by only 0.1 kWh (about 0.6%), so either is acceptable. Simpson's rule is usually more accurate for smooth data. There is no graph.

## E. Modified program for a related real-world case

**New case:** daily energy produced by a solar panel and its value.

**Assumptions:** output every 2 hours from 06:00 to 18:00 [0.0, 1.2, 2.8, 3.6, 3.0, 1.4, 0.1] kW (made-up data); an assumed electricity price of KES 25 per kWh.

**Interpretation:** the panel produces about 24.1 kWh (trapezoid) to 24.33 kWh (Simpson), worth about KES 608 a day at the assumed price.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C - Original: trapezoid=15.700 kWh, Simpson=15.800 kWh
PART C - Peak = 2.5 kW: trapezoid=17.100 kWh, Simpson=17.667 kWh

PART E - daily solar energy
Trapezoid: 24.100 kWh | Simpson: 24.333 kWh | difference: 0.233 kWh
Value at KES 25/kWh (Simpson): KES 608.33
```
