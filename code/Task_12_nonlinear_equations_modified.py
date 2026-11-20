import numpy as np
from scipy.optimize import root

# ---------- PART C: change the circle radius from 2 to 3 ----------
def eq_r(r):
    return lambda z: [z[0]**2 + z[1]**2 - r**2, z[1] - (z[0]**2 - 1)]
for r in (2, 3):
    s = root(eq_r(r), [1.0, 1.0])
    print(f"PART C - radius {r}: intersection = {np.round(s.x, 4)}, residuals = {np.round(eq_r(r)(s.x), 10)}")

# ---------- PART E: new real-world case ----------
# Assumption: two cell towers. Tower 1 at (0,0) with range 5 km; tower 2 at (6,0) with range 4 km.
# Find where the two coverage boundaries cross.
def towers(z):
    x, y = z
    return [x**2 + y**2 - 25, (x - 6)**2 + y**2 - 16]
print("\nPART E - coverage boundary crossings")
for guess in ([3.0, 3.0], [3.0, -3.0]):
    s = root(towers, guess)
    print("Guess", guess, "->", np.round(s.x, 4), "converged:", s.success, "residuals:", np.round(towers(s.x), 10))
