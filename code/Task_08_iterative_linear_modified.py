import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, tol=1e-8, max_iter=5000):
    D = np.diag(A); R = A - np.diagflat(D)
    x = np.zeros_like(b); errs = []
    for _ in range(max_iter):
        xn = (b - R @ x) / D
        e = np.linalg.norm(xn - x, ord=np.inf); errs.append(e)
        if e < tol: return xn, errs
        x = xn
    return x, errs

def gauss_seidel(A, b, tol=1e-8, max_iter=5000):
    x = np.zeros_like(b); errs = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        e = np.linalg.norm(x - old, ord=np.inf); errs.append(e)
        if e < tol: return x, errs
    return x, errs

def rod(n, left, right):
    A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    b = np.zeros(n); b[0] = left; b[-1] = right
    return A, b

# ---------- PART C: change boundaries (100,20 -> 80,40) and the tolerance ----------
A, b = rod(5, 80., 40.)
xj, ej = jacobi(A, b); xg, eg = gauss_seidel(A, b)
print("PART C - boundaries 80 C and 40 C, tol=1e-8")
print("Direct   :", np.round(np.linalg.solve(A, b), 4))
print("Jacobi   :", np.round(xj, 4), "iterations:", len(ej))
print("GaussSeid:", np.round(xg, 4), "iterations:", len(eg))
_, ej4 = jacobi(A, b, tol=1e-4)
print("Jacobi iterations with looser tol=1e-4:", len(ej4))

# ---------- PART E: new real-world case ----------
# Assumption: a metal rod with 20 interior points, one end heated to 60 C, other end at 30 C.
A, b = rod(20, 60., 30.)
xj, ej = jacobi(A, b); xg, eg = gauss_seidel(A, b)
exact = np.linalg.solve(A, b)
print("\nPART E - 20-point rod (60 C to 30 C)")
print("Jacobi iterations:", len(ej), "| Gauss-Seidel iterations:", len(eg))
print("Max difference from direct solution (Jacobi, GS):", np.max(np.abs(xj-exact)), np.max(np.abs(xg-exact)))
print("Temperatures at points 1, 10, 20:", np.round(exact[[0, 9, 19]], 3))
plt.semilogy(ej, label="Jacobi"); plt.semilogy(eg, label="Gauss-Seidel")
plt.xlabel("Iteration"); plt.ylabel("Maximum change"); plt.title("Rod model: 20 points")
plt.legend(); plt.grid(True); plt.savefig("../images/task_08_modified.png", dpi=120)
