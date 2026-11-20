import numpy as np
from scipy.integrate import simpson

# ---------- PART C: change one reading (peak 1.8 kW -> 2.5 kW) ----------
t = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
p = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
p2 = p.copy(); p2[3] = 2.5
for name, arr in (("Original", p), ("Peak = 2.5 kW", p2)):
    print(f"PART C - {name}: trapezoid={np.trapezoid(arr, t):.3f} kWh, Simpson={simpson(arr, x=t):.3f} kWh")

# ---------- PART E: new real-world case ----------
# Assumption: solar panel output (kW) every 2 hours from 06:00 to 18:00, and an assumed price of KES 25 per kWh.
th = np.array([6, 8, 10, 12, 14, 16, 18], dtype=float)
kw = np.array([0.0, 1.2, 2.8, 3.6, 3.0, 1.4, 0.1])
e_t, e_s = np.trapezoid(kw, th), simpson(kw, x=th)
print("\nPART E - daily solar energy")
print(f"Trapezoid: {e_t:.3f} kWh | Simpson: {e_s:.3f} kWh | difference: {abs(e_t - e_s):.3f} kWh")
print(f"Value at KES 25/kWh (Simpson): KES {e_s * 25:,.2f}")
