# Task 12: Polynomial and Nonlinear Equation Solving

Programs: [`code/Task_12_nonlinear_equations.py`](../code/Task_12_nonlinear_equations.py) (original) and [`code/Task_12_nonlinear_equations_modified.py`](../code/Task_12_nonlinear_equations_modified.py) (modified)

## Original program output

```text
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True
```

## B. Inputs and mathematical operation

**Input values:** two equations, the circle x^2 + y^2 = 4 and the parabola y = x^2 - 1, and two starting guesses [1, 1] and [-1, 1].

**Mathematical operations:** write each equation as a residual (left side minus right side) and use `scipy.optimize.root` to find x and y where both residuals are zero. Check that the residuals are tiny.

## C. Changing a parameter

**Change made:** the circle radius was changed from 2 to 3 (x^2 + y^2 = 9).

**Effect:** the right-hand intersection moved from (1.5175, 1.3028) to (1.8364, 2.3723). A bigger circle meets the parabola further out and higher up.

## D. Meaning of the output

The two intersections are (1.5175, 1.3028) and (-1.5175, 1.3028). They are mirror images because both curves are symmetric about the y axis. The residuals are around 1e-13 (essentially zero) and `Converged: True`, so both points lie on both curves. A different starting guess finds a different intersection, which is why we try more than one. There is no graph.

## E. Modified program for a related real-world case

**New case:** where the coverage boundaries of two cell towers cross.

**Assumptions:** tower 1 at (0, 0) with range 5 km; tower 2 at (6, 0) with range 4 km.

**Interpretation:** the boundaries cross at (3.75, 3.3072) and (3.75, -3.3072), 3.31 km north and south of the line between the towers. Both guesses converged with zero residuals.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C - radius 2: intersection = [1.5175 1.3028], residuals = [-0. -0.]
PART C - radius 3: intersection = [1.8364 2.3723], residuals = [-0.  0.]

PART E - coverage boundary crossings
Guess [3.0, 3.0] -> [3.75   3.3072] converged: True residuals: [0. 0.]
Guess [3.0, -3.0] -> [ 3.75   -3.3072] converged: True residuals: [0. 0.]
```
