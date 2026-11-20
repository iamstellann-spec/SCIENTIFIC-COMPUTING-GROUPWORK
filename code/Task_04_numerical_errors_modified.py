import numpy as np, math

# ---------- PART C: change the input values ----------
print("PART C - smaller x values in the unstable formula")
for x in [1e-8, 1e-12, 1e-14, 1e-16]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")

# Different approximation of sqrt(2): 1.41421 instead of 1.414
true_value = np.sqrt(2)
for approx in (1.414, 1.41421):
    ae = abs(true_value - approx)
    print(f"approx={approx}: absolute error={ae:.8f}, relative error={ae/true_value:.8%}")

# ---------- PART E: new real-world case ----------
# Assumption: a bank adds a 0.10 KES fee one million times. The true total is exactly 100,000.00.
total = 0.0
for _ in range(1_000_000):
    total += 0.10
print("\nPART E - accumulating 1,000,000 fees of KES 0.10 (true total = 100000)")
print(f"Plain float sum : {total:.10f}")
print(f"Error           : {abs(total - 100000):.10f}")
print(f"math.fsum       : {math.fsum([0.10]*1_000_000):.10f}")
print("Safe equality check:", np.isclose(total, 100000.0), "| Exact equality:", total == 100000.0)
