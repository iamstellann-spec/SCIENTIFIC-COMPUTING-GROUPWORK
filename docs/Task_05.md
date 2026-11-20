# Task 5: Matrix Algebra and Matrix Operations

Programs: [`code/Task_05_matrix_algebra.py`](../code/Task_05_matrix_algebra.py) (original) and [`code/Task_05_matrix_algebra_modified.py`](../code/Task_05_matrix_algebra_modified.py) (modified)

## Original program output

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```

## B. Inputs and mathematical operation

**Input values:** the four corners of a unit square, a rotation of 45 degrees, and a scaling of 2 in x and 1.5 in y.

**Mathematical operations:** build the rotation matrix R and scaling matrix S, combine them as T = R @ S (scale first, then rotate), transform every point with matrix multiplication (points @ T.T), and compute the determinant of T.

## C. Changing a parameter

**Changes made:** the angle was changed from 45 to 90 degrees and the x scale from 2 to 3.

**Effect:** the square became a 1.5 by 3 rectangle turned a quarter turn (corners (0,0), (0,3), (-1.5,3), (-1.5,0)). The determinant changed from 3.0 to 4.5 (3 x 1.5). Rotation never changes the determinant (it is 1); only the scaling does.

## D. Meaning of the output

The transformed corners show the unit square stretched and turned: for example (1,0) goes to (1.414, 1.414). The determinant is 3.0, meaning areas are multiplied by 3 (the 1 x 1 square becomes area 3). It is positive, so the shape is not mirror-flipped. There is no graph.

## E. Modified program for a related real-world case

**New case:** rotating and shrinking a room floor plan so it fits on a screen.

**Assumptions:** the room is 4 m by 3 m with one corner at the origin; it is rotated 30 degrees and scaled to 0.5 in both directions.

**Interpretation:** the determinant is 0.25, the area scale factor (0.5 x 0.5). The 12 m2 room is drawn as 3 square units. The shape stays a rectangle because rotation and uniform scaling keep the angles.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C - angle 45->90 degrees, scale (2, 1.5) -> (3, 1.5)
Transformed points:
 [[ 0.   0. ]
 [ 0.   3. ]
 [-1.5  3. ]
 [-1.5  0. ]]
Determinant: 4.5 (original was 3.0)

PART E - rotating and scaling a room floor plan
Transformed corners:
 [[ 0.     0.   ]
 [ 1.732  1.   ]
 [ 0.982  2.299]
 [-0.75   1.299]]
Determinant (area scale factor): 0.25
Original area: 12 m^2  ->  new area: 3.0 units^2
```
