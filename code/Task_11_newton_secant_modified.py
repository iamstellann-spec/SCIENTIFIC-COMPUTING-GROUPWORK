from scipy.optimize import root_scalar

def make_npv(flows):
    return lambda r: sum(cf / (1 + r)**t for t, cf in enumerate(flows))

# ---------- PART C: change the initial investment (10,000 -> 12,000) ----------
for inv in (10000, 12000):
    flows = [-inv, 3000, 3500, 4000, 2500]
    npv = make_npv(flows)
    r = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
    print(f"PART C - investment {inv}: IRR = {r.root:.4%} ({r.iterations} secant iterations)")

# ---------- PART E: new real-world case ----------
# Assumption: borrow KES 100,000 and repay KES 30,000 each year for 4 years. What is the true yearly interest rate?
flows = [100000, -30000, -30000, -30000, -30000]
npv = make_npv(flows)
r = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
print("\nPART E - effective annual interest rate of the loan")
print(f"Rate = {r.root:.4%}; NPV at that rate = {npv(r.root):.6f}")
print(f"Total repaid = {30000*4:,} for a loan of 100,000 (extra paid: {30000*4 - 100000:,})")
