import numpy as np

# ---------- PART C: change the observed totals ----------
A = np.array([[4.0, 2.0], [8.0, 12.0]])
for b in (np.array([20.0, 72.0]), np.array([24.0, 80.0])):
    s = np.linalg.solve(A, b)
    print(f"PART C - totals {b}: Type A={s[0]:.2f}, Type B={s[1]:.2f}, residual norm={np.linalg.norm(b - A @ s):.1e}")

# ---------- PART E: new real-world case ----------
# Assumption: two fertiliser mixes. Mix 1 = 20% nitrogen, 10% phosphorus. Mix 2 = 10% nitrogen, 30% phosphorus.
# A farm needs 14 kg nitrogen and 18 kg phosphorus. How many kg of each mix?
A2 = np.array([[0.20, 0.10],
               [0.10, 0.30]])
b2 = np.array([14.0, 18.0])
x = np.linalg.solve(A2, b2)
print("\nPART E - fertiliser mixing")
print(f"Mix 1: {x[0]:.2f} kg, Mix 2: {x[1]:.2f} kg")
print("Check (nitrogen, phosphorus):", A2 @ x)
print("Residual norm:", np.linalg.norm(b2 - A2 @ x))
