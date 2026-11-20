# SCIENTIFIC-COMPUTING-GROUPWORK
BIT 2118 Scientific Computing group work (Tasks 2 to 20)
# SCIENTIFIC-COMPUTING-GROUPWORK
BIT 2118 Scientific Computing group work (Tasks 2 to 20)
# BIT 2118 Scientific Computing - Group Work (Tasks 2 to 20)

Individual submission. Each task has a documented original program, a changed parameter, an output interpretation, and a modified program for a related real-world case.

**Name:** (STELLA NJERI NGANGA)  
**Admission number:** (BSCCS252607368)  
**Group:** (11)

## Structure

| Folder | What is inside |
|---|---|
| `code/` | `Task_XX_*.py` = original program. `Task_XX_*_modified.py` = Part C (parameter change) plus Part E (new real-world case) |
| `docs/` | One file per task (`Task_02.md` to `Task_20.md`) answering B (inputs and operation), C (parameter change), D (meaning of output) and E (new case: assumptions, data, output, interpretation) |
| `images/` | Graphs produced by the programs |
| `outputs/` | Saved printed output of every program |

## Task index

| Task | Topic | Doc |
|---|---|---|
| 2 | NumPy Arrays and Numerical Computation | [docs/Task_02.md](docs/Task_02.md) |
| 3 | Mathematical Functions and Vectorization | [docs/Task_03.md](docs/Task_03.md) |
| 4 | Floating-Point Arithmetic and Numerical Errors | [docs/Task_04.md](docs/Task_04.md) |
| 5 | Matrix Algebra and Matrix Operations | [docs/Task_05.md](docs/Task_05.md) |
| 6 | Solution of Systems of Linear Equations | [docs/Task_06.md](docs/Task_06.md) |
| 7 | Gaussian Elimination and LU Decomposition | [docs/Task_07.md](docs/Task_07.md) |
| 8 | Iterative Methods for Linear Systems | [docs/Task_08.md](docs/Task_08.md) |
| 9 | Eigenvalues and Eigenvectors | [docs/Task_09.md](docs/Task_09.md) |
| 10 | Root Finding: Bisection and Fixed-Point | [docs/Task_10.md](docs/Task_10.md) |
| 11 | Root Finding: Newton-Raphson and Secant | [docs/Task_11.md](docs/Task_11.md) |
| 12 | Polynomial and Nonlinear Equation Solving | [docs/Task_12.md](docs/Task_12.md) |
| 13 | Interpolation | [docs/Task_13.md](docs/Task_13.md) |
| 14 | Curve Fitting and Approximation | [docs/Task_14.md](docs/Task_14.md) |
| 15 | Numerical Differentiation | [docs/Task_15.md](docs/Task_15.md) |
| 16 | Numerical Integration | [docs/Task_16.md](docs/Task_16.md) |
| 17 | ODEs: Euler Method | [docs/Task_17.md](docs/Task_17.md) |
| 18 | Numerical Solution of ODEs Using SciPy | [docs/Task_18.md](docs/Task_18.md) |
| 19 | Numerical Optimization | [docs/Task_19.md](docs/Task_19.md) |
| 20 | Random Numbers and Monte Carlo Methods | [docs/Task_20.md](docs/Task_20.md) |

## How to run

```bash
pip install numpy scipy matplotlib
cd code
python Task_02_numpy_arrays.py
```

Run the programs from inside the `code/` folder, because the graph-saving lines write to `../images/`.

## Notes

- Task 16 uses `np.trapezoid`, which needs NumPy 2.0 or newer. On older NumPy, replace it with `np.trapz`.
- In Task 13 one line was added to drop any time value that goes slightly past 14.0 because of floating-point rounding in `np.arange`.
- Each original program saves its graph with `plt.savefig(...)` before `plt.show()`.
- Timing results (Tasks 3 and 7) vary by computer.
- All data in the Part E real-world cases is made-up sample data for practice, with assumptions stated in each doc.

