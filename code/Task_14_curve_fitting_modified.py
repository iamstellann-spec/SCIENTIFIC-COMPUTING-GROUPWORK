import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
resp = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

# ---------- PART C: change the model from quadratic to straight line ----------
def quad(x, a, b, c): return a*x**2 + b*x + c
def line(x, m, c): return m*x + c
pq, _ = curve_fit(quad, users, resp)
pl, _ = curve_fit(line, users, resp)
rmse = lambda m, p: np.sqrt(np.mean((resp - m(users, *p))**2))
print("PART C - model comparison")
print(f"Quadratic: RMSE={rmse(quad, pq):.2f} ms, prediction at 400 users = {quad(400, *pq):.1f} ms")
print(f"Linear   : RMSE={rmse(line, pl):.2f} ms, prediction at 400 users = {line(400, *pl):.1f} ms")

# ---------- PART E: new real-world case ----------
# Assumption: monthly active users of a new app (made-up data) grow exponentially.
months = np.arange(1, 9, dtype=float)
active = np.array([120, 150, 190, 240, 300, 380, 480, 600], dtype=float)
def expo(t, a, b): return a * np.exp(b * t)
p, _ = curve_fit(expo, months, active, p0=(100, 0.2))
fit = expo(months, *p)
print("\nPART E - app growth")
print(f"Model: users = {p[0]:.2f} * exp({p[1]:.4f} * month)")
print(f"RMSE: {np.sqrt(np.mean((active - fit)**2)):.2f} users")
print(f"Monthly growth rate: {np.exp(p[1]) - 1:.2%}")
print(f"Predicted users in month 10: {expo(10, *p):.0f}")
xs = np.linspace(1, 10, 200)
plt.scatter(months, active, label="Data"); plt.plot(xs, expo(xs, *p), label="Exponential fit")
plt.xlabel("Month"); plt.ylabel("Active users"); plt.title("App user growth")
plt.legend(); plt.grid(True); plt.savefig("../images/task_14_modified.png", dpi=120)
