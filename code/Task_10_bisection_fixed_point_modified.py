import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# ---------- PART C: change the constant 10 to 20 in the heat-balance model ----------
def f_orig(T): return T - 25 - 10*np.exp(-T/20)
def f_new(T):  return T - 25 - 20*np.exp(-T/20)
for name, f in (("original (10)", f_orig), ("changed (20)", f_new)):
    r = root_scalar(f, bracket=[20, 50], method="bisect", xtol=1e-10)
    print(f"PART C - {name}: equilibrium = {r.root:.6f} C after {r.iterations} bisection steps")

# ---------- PART E: new real-world case ----------
# Assumption: a bakery sells at KES 60 per unit. Costs = 5000 fixed + 20 per unit + 0.04*q^2 (crowding cost).
def profit(q): return 60*q - (5000 + 20*q + 0.04*q**2)
low  = root_scalar(profit, bracket=[0, 500],  method="bisect", xtol=1e-10).root
high = root_scalar(profit, bracket=[500, 1000], method="bisect", xtol=1e-10).root
print(f"\nPART E - break-even quantities: {low:.2f} units and {high:.2f} units")
print(f"Profit at 500 units: KES {profit(500):,.2f}")
q = np.linspace(0, 1000, 400)
plt.plot(q, profit(q)); plt.axhline(0, linewidth=0.8)
plt.axvline(low, linestyle="--"); plt.axvline(high, linestyle="--")
plt.xlabel("Units produced"); plt.ylabel("Profit (KES)"); plt.title("Break-even points")
plt.grid(True); plt.savefig("../images/task_10_modified.png", dpi=120)
