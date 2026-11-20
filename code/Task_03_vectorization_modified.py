import numpy as np, timeit

rng = np.random.default_rng(42)

def compare(n):
    data = rng.uniform(5, 250, n)
    def loop():
        out = []
        for v in data:
            out.append((v / 1000.0) ** 2)
        return out
    def vec():
        return (data / 1000.0) ** 2
    lt = timeit.timeit(loop, number=1)
    vt = timeit.timeit(vec, number=3) / 3
    return lt, vt

# ---------- PART C: change the size of the data ----------
print("PART C - change N (number of readings)")
for n in (10_000, 1_000_000):
    lt, vt = compare(n)
    print(f"N={n:>9,}: loop={lt:.4f}s  vectorized={vt:.5f}s  speed-up={lt/vt:.1f}x")

# ---------- PART E: new real-world case ----------
# Assumption: 1,000,000 product prices in KES; Kenyan VAT of 16% is added to each, then totalled.
prices = rng.uniform(50, 5000, 1_000_000)
def loop_vat():
    total = 0.0
    for p in prices:
        total += p * 1.16
    return total
def vec_vat():
    return (prices * 1.16).sum()
lt = timeit.timeit(loop_vat, number=1)
vt = timeit.timeit(vec_vat, number=3) / 3
print("\nPART E - adding 16% VAT to one million prices (assumed data)")
print(f"Total with VAT (loop)      : KES {loop_vat():,.2f}")
print(f"Total with VAT (vectorized): KES {vec_vat():,.2f}")
print(f"Loop {lt:.4f}s vs vectorized {vt:.5f}s -> {lt/vt:.1f}x faster")
