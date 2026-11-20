# Task 7: Gaussian Elimination and LU Decomposition

Programs: [`code/Task_07_gaussian_lu.py`](../code/Task_07_gaussian_lu.py) (original) and [`code/Task_07_gaussian_lu_modified.py`](../code/Task_07_gaussian_lu_modified.py) (modified)

## Original program output

```text
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

## B. Inputs and mathematical operation

**Input values:** a 3 x 3 coefficient matrix A and three measurement vectors b.

**Mathematical operations:** LU decomposition (`lu_factor`) of A once, then forward and back substitution (`lu_solve`) for each b. A direct `np.linalg.solve` is used for comparison.

## C. Changing a parameter

**Changes made:** (1) A[2,2] was changed from 3 to 6; (2) the first measurement was doubled from 15 to 30.

**Effect:** with A[2,2] = 6 the solution changed from [5, 5, 5] to about [4.83, 4.30, 2.38], with the biggest change in the third unknown. Doubling b[0] changed it to about [9.02, 6.10, 5.37], with the first unknown nearly doubling.

## D. Meaning of the output

For the first measurement the solution is [5, 5, 5], matching the direct solver. The other two sets give slightly different solutions. The residual norms are around 1e-15 or zero, so the solutions satisfy the equations up to computer rounding. There is no graph.

## E. Modified program for a related real-world case

**New case:** repeated heat calculations along a rod with 200 points, 500 time steps.

**Assumptions:** the matrix stays the same every step (4 on the diagonal, -1 beside it); each step has a new random right-hand side (made-up data).

**Interpretation:** factoring once and reusing took 0.0113 s, while solving from scratch each time took 0.1606 s, about 14x slower, with identical answers (difference 0). This is why simulations that reuse the same matrix use LU decomposition.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C
Original solution      : [5. 5. 5.]
A[2,2] changed to 6    : [4.8255814  4.30232558 2.38372093]
b[0] changed to 30     : [9.02439024 6.09756098 5.36585366]

PART E - 500 time steps on a 200x200 system
Factor once + reuse: 0.0113s | Solve from scratch each time: 0.1606s
Maximum difference between the two answers: 0.00e+00
```
