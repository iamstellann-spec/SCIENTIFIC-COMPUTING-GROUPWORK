import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temp = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])

# ---------- PART C: change the target time and add a quadratic interpolant ----------
lin = interp1d(hours, temp, kind="linear")
quad = interp1d(hours, temp, kind="quadratic")
cub = CubicSpline(hours, temp)
for t in (10.5, 13.5):
    print(f"PART C - t={t}: linear={float(lin(t)):.3f}, quadratic={float(quad(t)):.3f}, cubic={float(cub(t)):.3f}")

# ---------- PART E: new real-world case ----------
# Assumption: daily maximum temperatures for days 1-7, but days 4 and 5 are missing (sensor outage).
days = np.array([1, 2, 3, 6, 7], dtype=float)
tmax = np.array([24.0, 25.0, 26.5, 23.0, 22.0])
l = interp1d(days, tmax); c = CubicSpline(days, tmax)
missing = np.array([4.0, 5.0])
print("\nPART E - estimating missing days")
print("Day 4,5 linear:", np.round(l(missing), 2))
print("Day 4,5 cubic :", np.round(c(missing), 2))
xs = np.linspace(1, 7, 200)
plt.scatter(days, tmax, label="Measured")
plt.plot(xs, l(xs), label="Linear"); plt.plot(xs, c(xs), label="Cubic spline")
plt.xlabel("Day"); plt.ylabel("Max temperature (C)"); plt.title("Filling missing readings")
plt.legend(); plt.grid(True); plt.savefig("../images/task_13_modified.png", dpi=120)
