# Task 4: Floating-Point Arithmetic and Numerical Errors

Programs: [`code/Task_04_numerical_errors.py`](../code/Task_04_numerical_errors.py) (original) and [`code/Task_04_numerical_errors_modified.py`](../code/Task_04_numerical_errors_modified.py) (modified)

## Original program output

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

## B. Inputs and mathematical operation

**Input values:** 0.1 + 0.2 compared with 0.3; the true value of the square root of 2 compared with the approximation 1.414; and x = 1e-4, 1e-8, 1e-12 in the expression (sqrt(1+x) - 1) / x.

**Mathematical operations:** exact equality versus `np.isclose` tolerance comparison; absolute error |true - approx|; relative error (absolute error / true value); and two algebraically equal formulas for the same expression, a direct one and a rearranged "stable" one (1 / (sqrt(1+x) + 1)).

## C. Changing a parameter

**Changes made:** (1) smaller x values (1e-14 and 1e-16) were tried in the unstable formula; (2) the approximation of the square root of 2 was changed from 1.414 to 1.41421.

**Effect:** the direct formula gets worse as x shrinks: 0.5000444 at x=1e-12, 0.4885 at x=1e-14, and 0.0 at x=1e-16, because 1 + 1e-16 is stored as exactly 1. The stable formula stays at 0.5 (the correct limit). The better square-root approximation cut the relative error from 0.0151% to 0.000252%.

## D. Meaning of the output

0.1 + 0.2 gives 0.30000000000000004, so exact equality with 0.3 is False, while `np.isclose` says True. The absolute error of 1.414 is 0.00021356 and the relative error is 0.0151%. In the last loop the correct value is 0.5, and the direct formula loses accuracy for small x. This is catastrophic cancellation: subtracting two almost equal numbers wipes out the correct digits. Rearranging the formula avoids it. There is no graph.

## E. Modified program for a related real-world case

**New case:** a bank adds a fee of KES 0.10 one million times.

**Assumptions:** the true total is exactly KES 100,000.00; the sum is accumulated in ordinary floating-point numbers.

**Interpretation:** the plain float sum came out as 100000.0000013329, an error of about 0.0000013. Tiny, but exact equality with 100000 is False while `np.isclose` is True; `math.fsum` gives the exact total. Real financial systems avoid this problem by storing money as whole cents or using decimal types, and by comparing with tolerances.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C - smaller x values in the unstable formula
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
x=1e-14: direct=0.488498130835, stable=0.500000000000
x=1e-16: direct=0.000000000000, stable=0.500000000000
approx=1.414: absolute error=0.00021356, relative error=0.01510114%
approx=1.41421: absolute error=0.00000356, relative error=0.00025190%

PART E - accumulating 1,000,000 fees of KES 0.10 (true total = 100000)
Plain float sum : 100000.0000013329
Error           : 0.0000013329
math.fsum       : 100000.0000000000
Safe equality check: True | Exact equality: False
```
