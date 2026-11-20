import numpy as np
import matplotlib.pyplot as plt

# ---------- PART C: change the step size h and the rate k ----------
def cooling(h, k, T0=90.0, Ta=25.0, end=30.0):
    t = np.arange(0, end + h, h)
    T = np.zeros_like(t); T[0] = T0
    for i in range(len(t) - 1):
        T[i + 1] = T[i] + h * (-k * (T[i] - Ta))
    exact = Ta + (T0 - Ta) * np.exp(-k * t)
    return t, T, exact
print("PART C - final temperature error at 30 min")
for h, k in ((1.0, 0.12), (5.0, 0.12), (0.1, 0.12), (1.0, 0.30)):
    t, T, ex = cooling(h, k)
    print(f"h={h:<4} k={k:<4}: Euler={T[-1]:.3f} C, exact={ex[-1]:.3f} C, error={abs(T[-1] - ex[-1]):.4f} C")

# ---------- PART E: new real-world case ----------
# Assumption: fish population in a pond follows logistic growth dP/dt = r P (1 - P/K).
r, K, P0, h, end = 0.4, 1000.0, 100.0, 0.5, 30.0
t = np.arange(0, end + h, h)
P = np.zeros_like(t); P[0] = P0
for i in range(len(t) - 1):
    P[i + 1] = P[i] + h * r * P[i] * (1 - P[i] / K)
exact = K / (1 + ((K - P0) / P0) * np.exp(-r * t))
print("\nPART E - pond population (r=0.4, K=1000, P0=100, h=0.5 days)")
print(f"Euler after 30 days: {P[-1]:.1f} | exact: {exact[-1]:.1f} | max error: {np.max(np.abs(P - exact)):.1f}")
print(f"Day when population first exceeds 500 (Euler): {t[np.argmax(P > 500)]:.1f}")
plt.plot(t, P, marker="o", markersize=3, label="Euler"); plt.plot(t, exact, label="Exact")
plt.xlabel("Days"); plt.ylabel("Population"); plt.title("Logistic growth of fish in a pond")
plt.legend(); plt.grid(True); plt.savefig("../images/task_17_modified.png", dpi=120)
