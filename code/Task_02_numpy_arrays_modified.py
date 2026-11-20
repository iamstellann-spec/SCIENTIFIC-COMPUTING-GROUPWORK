import numpy as np

# ---------- PART C: change one input ----------
temps = np.array([18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
                  29.4, 29.1, 28.5, 27.6, 26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0])
changed = temps.copy()
changed[12] = 40.0   # the 1 pm reading changes from 29.4 C to 40.0 C (faulty sensor / heat spike)
print("PART C - one reading changed (29.4 -> 40.0)")
print(f"Original: mean={temps.mean():.2f}, min={temps.min():.2f}, max={temps.max():.2f}")
print(f"Changed : mean={changed.mean():.2f}, min={changed.min():.2f}, max={changed.max():.2f}")

# ---------- PART E: new real-world case ----------
# Assumption: a rain gauge in Thika records daily rainfall (mm) for 7 days (made-up sample data).
rain_mm = np.array([0.0, 2.5, 12.0, 30.5, 8.0, 0.0, 4.5])
area_m2 = 4046.86            # one acre in square metres
litres_per_acre = rain_mm * area_m2   # 1 mm of rain = 1 litre per square metre
print("\nPART E - weekly rainfall at a farm (assumed data)")
print(f"Total rain: {rain_mm.sum():.1f} mm, mean/day: {rain_mm.mean():.2f} mm, wettest day: {rain_mm.max():.1f} mm")
print(f"Rainy days (>1 mm): {(rain_mm > 1).sum()}")
print(f"Water falling on one acre in the week: {litres_per_acre.sum():,.0f} litres")
