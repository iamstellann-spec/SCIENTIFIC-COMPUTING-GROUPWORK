import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ---------- PART C: change the resistance from 1000 to 2000 ohms ----------
def rc(R, C=0.001, Vs=5.0):
    sol = solve_ivp(lambda t, V: [(Vs - V[0]) / (R * C)], (0, 5), [0.0],
                    t_eval=np.linspace(0, 5, 200), rtol=1e-9, atol=1e-11)
    return sol
print("PART C - effect of resistance (time constant tau = R*C)")
for R in (1000.0, 2000.0):
    s = rc(R)
    tau = R * 0.001
    v_tau = np.interp(tau, s.t, s.y[0])
    print(f"R={R:.0f}: tau={tau:.1f}s, V at 1 s={np.interp(1, s.t, s.y[0]):.3f} V, V at tau={v_tau:.3f} V (63.2% of 5 V = 3.161 V), V at 5 s={s.y[0, -1]:.3f} V")

# ---------- PART E: new real-world case ----------
# Assumption: SIR epidemic in a school of 1000 students. beta=0.3/day, gamma=0.1/day (R0 = 3), 1 student infected.
beta, gamma, N = 0.3, 0.1, 1000.0
def sir(t, y):
    S, I, Rr = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]
sol = solve_ivp(sir, (0, 160), [999.0, 1.0, 0.0], t_eval=np.linspace(0, 160, 321), rtol=1e-8, atol=1e-10)
S, I, Rr = sol.y
print("\nPART E - SIR model")
print(f"Peak infected: {I.max():.0f} students on day {sol.t[np.argmax(I)]:.1f}")
print(f"Never infected at end: {S[-1]:.0f} | recovered at end: {Rr[-1]:.0f}")
plt.plot(sol.t, S, label="Susceptible"); plt.plot(sol.t, I, label="Infected"); plt.plot(sol.t, Rr, label="Recovered")
plt.xlabel("Days"); plt.ylabel("Students"); plt.title("SIR model for a school")
plt.legend(); plt.grid(True); plt.savefig("../images/task_18_modified.png", dpi=120)
