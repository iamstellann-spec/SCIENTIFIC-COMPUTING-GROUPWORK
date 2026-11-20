# Task 2: NumPy Arrays and Numerical Computation

Programs: [`code/Task_02_numpy_arrays.py`](../code/Task_02_numpy_arrays.py) (original) and [`code/Task_02_numpy_arrays_modified.py`](../code/Task_02_numpy_arrays_modified.py) (modified)

## Original program output

```text
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

## B. Inputs and mathematical operation

**Input values:** 24 hourly temperature readings in degrees Celsius (from 17.5 C up to 29.4 C), stored in one NumPy array.

**Mathematical operations:** mean, minimum and maximum of the array, then the conversion F = 1.8C + 32 applied to every element at once (vectorized, no loop).

## C. Changing a parameter

**Change made:** the 1 pm reading was changed from 29.4 C to 40.0 C (like a heat spike or a faulty sensor).

**Effect:** the mean rose from 23.12 C to 23.56 C, the maximum jumped from 29.40 C to 40.00 C, and the minimum stayed 17.50 C. One extreme value moves the maximum completely, but the mean only a little, because it is shared across 24 readings (the rise is 10.6 / 24 = 0.44 C).

## D. Meaning of the output

The average temperature over the day is 23.12 C. The coldest hour is 17.50 C (early morning) and the hottest is 29.40 C (early afternoon). The first six Fahrenheit values (about 63.5 F to 66.2 F) show the cool early-morning hours in Fahrenheit. There is no graph in this task.

## E. Modified program for a related real-world case

**New case:** weekly rainfall at a farm in Thika.

**Assumptions:** the 7 daily rainfall values are made-up sample data; 1 mm of rain equals 1 litre per square metre; one acre is 4046.86 m2.

**Input data:** [0.0, 2.5, 12.0, 30.5, 8.0, 0.0, 4.5] mm.

**Interpretation:** the week had 57.5 mm of rain over 5 rainy days. About 232,694 litres of water fell on one acre. The wettest day (30.5 mm) brought over half of the week's rain (53%), so the rain came in a short burst, which matters for runoff and for deciding how much water a farm can store.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C - one reading changed (29.4 -> 40.0)
Original: mean=23.12, min=17.50, max=29.40
Changed : mean=23.56, min=17.50, max=40.00

PART E - weekly rainfall at a farm (assumed data)
Total rain: 57.5 mm, mean/day: 8.21 mm, wettest day: 30.5 mm
Rainy days (>1 mm): 5
Water falling on one acre in the week: 232,694 litres
```
