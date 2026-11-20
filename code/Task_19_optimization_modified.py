import numpy as np
from scipy.optimize import minimize

def solve(cost_a, cost_b, cap_a, cap_b, need):
    res = minimize(lambda z: cost_a*z[0] + cost_b*z[1], x0=[5, 3], method="SLSQP",
                   bounds=[(0, None), (0, None)],
                   constraints={"type": "ineq", "fun": lambda z: cap_a*z[0] + cap_b*z[1] - need})
    best = None
    for a in range(0, 40):
        for b in range(0, 40):
            if cap_a*a + cap_b*b >= need:
                c = cost_a*a + cost_b*b
                if best is None or c < best[0]: best = (c, a, b, cap_a*a + cap_b*b)
    return res, best

# ---------- PART C: change cost of A (12 -> 8) and required capacity (1000 -> 1500) ----------
print("PART C")
for label, args in (("Original", (12, 18, 100, 170, 1000)),
                    ("Cost A = 8", (8, 18, 100, 170, 1000)),
                    ("Need = 1500", (12, 18, 100, 170, 1500))):
    r, best = solve(*args)
    print(f"{label:11s}: A={r.x[0]:.3f}, B={r.x[1]:.3f}, cost={r.fun:.2f} | whole servers (cost,A,B,capacity)={best}")

# ---------- PART E: new real-world case ----------
# Assumption: mixing two animal feeds. Feed 1: KES 40/kg, 18% protein, 3.0 energy units/kg.
# Feed 2: KES 55/kg, 30% protein, 2.8 energy units/kg.
# Daily ration needs at least 40 kg, 9 kg protein and 110 energy units. Minimise cost.
cons = [{"type": "ineq", "fun": lambda z: z[0] + z[1] - 40},
        {"type": "ineq", "fun": lambda z: 0.18*z[0] + 0.30*z[1] - 9},
        {"type": "ineq", "fun": lambda z: 3.0*z[0] + 2.8*z[1] - 110}]
res = minimize(lambda z: 40*z[0] + 55*z[1], x0=[20, 20], method="SLSQP", bounds=[(0, None), (0, None)], constraints=cons)
x, y = res.x
print("\nPART E - feed mix")
print(f"Success: {res.success} | Feed 1: {x:.3f} kg | Feed 2: {y:.3f} kg | Cost: KES {res.fun:.2f}")
print(f"Total: {x + y:.2f} kg | protein: {0.18*x + 0.30*y:.2f} kg | energy: {3.0*x + 2.8*y:.2f}")
