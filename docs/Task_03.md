# Task 3: Mathematical Functions and Vectorization

Programs: [`code/Task_03_vectorization.py`](../code/Task_03_vectorization.py) (original) and [`code/Task_03_vectorization_modified.py`](../code/Task_03_vectorization_modified.py) (modified)

## Original program output

```text
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.1355 s
Vectorized time: 0.0031 s
Approximate speed-up: 43.4x
```

## B. Inputs and mathematical operation

**Input values:** 1,000,000 random network latencies between 5 and 250 milliseconds (random seed 42, so the data is repeatable).

**Mathematical operations:** divide each value by 1000 (milliseconds to seconds), then square it. This is done two ways: a Python loop and one vectorized NumPy expression. `timeit` measures how long each takes.

## C. Changing a parameter

**Change made:** the number of readings N was reduced from 1,000,000 to 10,000.

**Effect:** the loop took 0.0013 s at 10,000 values and 0.1302 s at 1,000,000 values, while the vectorized version took 0.00003 s and 0.00324 s. The speed-up stayed around 40x to 48x at both sizes. So vectorization is much faster whatever the size, and the actual time saved grows as the data grows. (Exact timings differ from computer to computer.)

## D. Meaning of the output

The first five squared latencies are small numbers like 0.0379 (seconds squared). The important output is the timing: in the original run the loop needed about 0.136 s, the vectorized version about 0.003 s, roughly 43x faster, for exactly the same answers. Vectorization lets NumPy do the repeated work in fast compiled code instead of Python executing one step at a time. There is no graph.

## E. Modified program for a related real-world case

**New case:** adding 16% VAT to one million product prices.

**Assumptions:** prices are random values between KES 50 and KES 5,000 (made-up data); VAT is 16%; the goal is the total with VAT.

**Interpretation:** both methods give the same total, KES 2,927,813,678.51, but the vectorized one was about 41x faster. For a business with millions of transactions, vectorized calculations keep reports quick.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C - change N (number of readings)
N=   10,000: loop=0.0013s  vectorized=0.00003s  speed-up=48.3x
N=1,000,000: loop=0.1302s  vectorized=0.00324s  speed-up=40.1x

PART E - adding 16% VAT to one million prices (assumed data)
Total with VAT (loop)      : KES 2,927,813,678.51
Total with VAT (vectorized): KES 2,927,813,678.51
Loop 0.0866s vs vectorized 0.00209s -> 41.5x faster
```
