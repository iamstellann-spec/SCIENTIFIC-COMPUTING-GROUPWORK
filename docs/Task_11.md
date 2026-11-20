# Task 11: Root Finding: Newton-Raphson and Secant Methods

Programs: [`code/Task_11_newton_secant.py`](../code/Task_11_newton_secant.py) (original) and [`code/Task_11_newton_secant_modified.py`](../code/Task_11_newton_secant_modified.py) (modified)

## Original program output

```text
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution: 0.000000
```

## B. Inputs and mathematical operation

**Input values:** cash flows [-10000, 3000, 3500, 4000, 2500] (an initial investment followed by four yearly inflows), Newton starting guess 0.10, secant starting guesses 0.05 and 0.20.

**Mathematical operations:** find the rate r at which the net present value NPV(r) = sum of cash flow / (1+r)^t equals zero. That rate is the internal rate of return (IRR). Newton-Raphson uses the derivative; the secant method uses only function values.

## C. Changing a parameter

**Change made:** the initial investment was changed from 10,000 to 12,000.

**Effect:** the IRR fell from 11.54% to 3.33%, because the same inflows now repay a bigger investment. Both took 7 secant iterations.

## D. Meaning of the output

Both methods give an IRR of 11.542461%, meaning the project earns about 11.5% per year on the money invested. The NPV at that rate is 0, which confirms the root. If the required return is below 11.5%, the project is worthwhile. There is no graph.

## E. Modified program for a related real-world case

**New case:** the true yearly interest rate of a loan.

**Assumptions:** a borrower receives KES 100,000 and repays KES 30,000 at the end of each of 4 years. (Cash flows are [100000, -30000, -30000, -30000, -30000].)

**Interpretation:** the effective annual interest rate is 7.7138%. The borrower repays KES 120,000 in total, KES 20,000 more than borrowed.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C - investment 10000: IRR = 11.5425% (7 secant iterations)
PART C - investment 12000: IRR = 3.3298% (7 secant iterations)

PART E - effective annual interest rate of the loan
Rate = 7.7138%; NPV at that rate = 0.000000
Total repaid = 120,000 for a loan of 100,000 (extra paid: 20,000)
```
