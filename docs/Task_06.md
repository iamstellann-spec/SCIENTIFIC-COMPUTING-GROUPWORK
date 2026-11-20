# Task 6: Solution of Systems of Linear Equations

Programs: [`code/Task_06_linear_systems.py`](../code/Task_06_linear_systems.py) (original) and [`code/Task_06_linear_systems_modified.py`](../code/Task_06_linear_systems_modified.py) (modified)

## Original program output

```text
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

## B. Inputs and mathematical operation

**Input values:** coefficient matrix A = [[4, 2], [8, 12]] (CPU and memory per server type) and the totals b = [20, 72].

**Mathematical operation:** solve Ax = b with `np.linalg.solve`, then check the answer using the residual b - A x.

## C. Changing a parameter

**Change made:** the observed totals were changed from [20, 72] to [24, 80].

**Effect:** the answer changed from 3 Type A and 4 Type B servers to 4 Type A and 4 Type B servers. More total CPU and memory is explained by one extra Type A server.

## D. Meaning of the output

The program finds 3 Type A servers and 4 Type B servers. The check works: 4(3) + 2(4) = 20 CPU units and 8(3) + 12(4) = 72 GB. The residual is 0, meaning the solution reproduces the totals exactly. There is no graph.

## E. Modified program for a related real-world case

**New case:** mixing two fertilisers.

**Assumptions:** Mix 1 is 20% nitrogen and 10% phosphorus; Mix 2 is 10% nitrogen and 30% phosphorus. The farm needs 14 kg of nitrogen and 18 kg of phosphorus.

**Interpretation:** the farm should use 48 kg of Mix 1 and 44 kg of Mix 2. Check: 0.2(48) + 0.1(44) = 14 and 0.1(48) + 0.3(44) = 18. The residual is zero.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C - totals [20. 72.]: Type A=3.00, Type B=4.00, residual norm=0.0e+00
PART C - totals [24. 80.]: Type A=4.00, Type B=4.00, residual norm=0.0e+00

PART E - fertiliser mixing
Mix 1: 48.00 kg, Mix 2: 44.00 kg
Check (nitrogen, phosphorus): [14. 18.]
Residual norm: 0.0
```
