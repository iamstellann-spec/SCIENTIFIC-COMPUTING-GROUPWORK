import numpy as np, timeit
from scipy.linalg import lu_factor, lu_solve

# ---------- PART C: change one entry of A and one measurement ----------
A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 3.0]])
b = np.array([15.0, 10.0, 10.0])
A2 = A.copy(); A2[2, 2] = 6.0          # stronger "self-coupling" in the last equation
b2 = np.array([30.0, 10.0, 10.0])      # first measurement doubled
print("PART C")
print("Original solution      :", np.linalg.solve(A, b))
print("A[2,2] changed to 6    :", np.linalg.solve(A2, b))
print("b[0] changed to 30     :", np.linalg.solve(A, b2))

# ---------- PART E: new real-world case ----------
# Assumption: heat in a 200-point rod. Same matrix every time step, new right-hand side each step.
n, steps = 200, 500
main = 4.0 * np.ones(n); off = -1.0 * np.ones(n - 1)
M = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
rng = np.random.default_rng(1)
rhs_list = [rng.uniform(0, 100, n) for _ in range(steps)]

def with_lu():
    lu, piv = lu_factor(M)
    return [lu_solve((lu, piv), r) for r in rhs_list]
def without_lu():
    return [np.linalg.solve(M, r) for r in rhs_list]

t1 = timeit.timeit(with_lu, number=1)
t2 = timeit.timeit(without_lu, number=1)
diff = max(np.max(np.abs(a - c)) for a, c in zip(with_lu(), without_lu()))
print("\nPART E - 500 time steps on a 200x200 system")
print(f"Factor once + reuse: {t1:.4f}s | Solve from scratch each time: {t2:.4f}s")
print(f"Maximum difference between the two answers: {diff:.2e}")
