import numpy as np

def centrality(A):
    vals, vecs = np.linalg.eig(A)
    i = np.argmax(np.real(vals))
    v = np.abs(np.real(vecs[:, i]))
    return np.real(vals[i]), v / v.sum()

# ---------- PART C: add one link (A-D) to the original network ----------
A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]], dtype=float)
A2 = A.copy(); A2[0, 3] = A2[3, 0] = 1
for name, M in (("Original", A), ("With A-D link", A2)):
    val, c = centrality(M)
    print(f"PART C - {name}: dominant eigenvalue={val:.4f}, importance A,B,C,D = {np.round(c, 4)}")

# ---------- PART E: new real-world case ----------
# Assumption: matatu route links between 5 towns (assumed network, for practice only).
towns = ["Nairobi", "Thika", "Ruiru", "Juja", "Kiambu"]
links = [("Nairobi","Thika"), ("Nairobi","Ruiru"), ("Nairobi","Kiambu"),
         ("Ruiru","Juja"), ("Juja","Thika"), ("Ruiru","Kiambu")]
idx = {t: i for i, t in enumerate(towns)}
N = np.zeros((5, 5))
for a, b in links:
    N[idx[a], idx[b]] = N[idx[b], idx[a]] = 1
val, c = centrality(N)
print("\nPART E - town network, dominant eigenvalue:", round(val, 4))
for t, s in sorted(zip(towns, c), key=lambda p: -p[1]):
    print(f"{t:8s}: {s:.4f}")
