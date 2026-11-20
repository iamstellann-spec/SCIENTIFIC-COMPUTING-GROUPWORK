# Task 19: Numerical Optimization

Programs: [`code/Task_19_optimization.py`](../code/Task_19_optimization.py) (original) and [`code/Task_19_optimization_modified.py`](../code/Task_19_optimization_modified.py) (modified)

## Original program output

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution: (108, 0, 6, 1020)
```

## B. Inputs and mathematical operation

**Input values:** cost per unit A = 12 and B = 18, capacity per unit A = 100 and B = 170, required capacity at least 1000, starting guess (5, 3), and non-negative bounds.

**Mathematical operations:** minimize the cost 12x + 18y subject to 100x + 170y >= 1000 using `minimize` (SLSQP). A loop then searches whole-server combinations to find the cheapest integer answer.

## C. Changing a parameter

**Changes made:** (1) the cost of A was changed from 12 to 8; (2) the required capacity was changed from 1000 to 1500.

**Effect:** with A at 8 the best plan switched completely to 10 units of A (cost 80). With a requirement of 1500 the plan used 8.824 units of B (cost 158.82), or 9 whole B servers (cost 162). The reason: A costs 0.12 per unit of capacity and B costs 0.106, so B is cheaper at first; with A at 8 it costs 0.08 per unit, so A wins.

## D. Meaning of the output

The optimizer chooses 0 of A and 5.882 of B, giving exactly 1000 capacity at a cost of 105.88. The capacity limit is exactly met, because paying for extra capacity would only add cost. For whole servers, the best is 6 of B (capacity 1020, cost 108), KES 2.12 more than the fractional answer. There is no graph.

## E. Modified program for a related real-world case

**New case:** the cheapest animal-feed mix.

**Assumptions:** Feed 1 costs KES 40/kg, with 18% protein and 3.0 energy units per kg; Feed 2 costs KES 55/kg, with 30% protein and 2.8 energy units per kg. The daily ration needs at least 40 kg, 9 kg of protein and 110 energy units.

**Interpretation:** use 25 kg of Feed 1 and 15 kg of Feed 2 at a cost of KES 1,825. It uses exactly 40 kg and 9 kg of protein, which are the binding limits; the energy (117) is above the minimum.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C
Original   : A=0.000, B=5.882, cost=105.88 | whole servers (cost,A,B,capacity)=(108, 0, 6, 1020)
Cost A = 8 : A=10.000, B=0.000, cost=80.00 | whole servers (cost,A,B,capacity)=(80, 10, 0, 1000)
Need = 1500: A=0.000, B=8.824, cost=158.82 | whole servers (cost,A,B,capacity)=(162, 0, 9, 1530)

PART E - feed mix
Success: True | Feed 1: 25.000 kg | Feed 2: 15.000 kg | Cost: KES 1825.00
Total: 40.00 kg | protein: 9.00 kg | energy: 117.00
```
