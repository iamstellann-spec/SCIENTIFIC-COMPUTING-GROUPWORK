import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# ---------- PART C: change capacity, spread of demand, and number of simulations ----------
def overload(capacity, mean, std, N):
    d = rng.normal(mean, std, N)
    return (d > capacity).mean()
print("PART C")
for cap, std, N in ((1000, 120, 100_000), (1100, 120, 100_000), (1000, 200, 100_000), (1000, 120, 1_000)):
    print(f"capacity={cap}, std={std}, N={N:>7,}: overload probability = {overload(cap, 850, std, N):.4%}")

# ---------- PART E: new real-world case ----------
# Assumption: a project has 3 tasks with uncertain durations in days (triangular: min, most likely, max).
# A: (3, 5, 9)  B: (2, 4, 8)  C: (4, 6, 12). The deadline is 17 days.
N = 100_000
total = (rng.triangular(3, 5, 9, N) + rng.triangular(2, 4, 8, N) + rng.triangular(4, 6, 12, N))
late = total > 17
print("\nPART E - project deadline risk")
print(f"Average total duration: {total.mean():.2f} days")
print(f"Probability of finishing after 17 days: {late.mean():.2%}")
print(f"90th percentile duration: {np.percentile(total, 90):.2f} days")
plt.hist(total, bins=60); plt.axvline(17, linestyle="--", color="red")
plt.xlabel("Total project duration (days)"); plt.ylabel("Number of simulations")
plt.title("Monte Carlo project duration (red = deadline)")
plt.grid(True); plt.savefig("../images/task_20_modified.png", dpi=120)
