import numpy as np
import matplotlib.pyplot as plt

# ---------- PART C: change the step size h ----------
# Test function f(x) = sin(x). The true derivative at x = 1 is cos(1).
f, true = np.sin, np.cos(1.0)
print("PART C - effect of step size h on derivative of sin(x) at x=1")
for h in (0.1, 0.01, 0.001):
    fwd = (f(1 + h) - f(1)) / h
    cen = (f(1 + h) - f(1 - h)) / (2 * h)
    print(f"h={h:<6}: forward error={abs(fwd - true):.2e}, central error={abs(cen - true):.2e}")

# ---------- PART E: new real-world case ----------
# Assumption: a car's speed (m/s) is logged every second; estimate acceleration (m/s^2).
t = np.arange(0, 6, dtype=float)
v = np.array([0.0, 2.1, 4.3, 6.2, 8.4, 10.1])
a = np.gradient(v, t)   # central differences inside, one-sided at the ends
print("\nPART E - acceleration from speed readings")
for ti, vi, ai in zip(t, v, a):
    print(f"t={ti:.0f}s speed={vi:4.1f} m/s acceleration={ai:.2f} m/s^2")
print(f"Average acceleration: {a.mean():.2f} m/s^2")
plt.plot(t, a, marker="o"); plt.xlabel("Time (s)"); plt.ylabel("Acceleration (m/s^2)")
plt.title("Acceleration estimated from speed"); plt.grid(True)
plt.savefig("../images/task_15_modified.png", dpi=120)
