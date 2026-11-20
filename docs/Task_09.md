# Task 9: Eigenvalues and Eigenvectors

Programs: [`code/Task_09_eigenvalues.py`](../code/Task_09_eigenvalues.py) (original) and [`code/Task_09_eigenvalues_modified.py`](../code/Task_09_eigenvalues_modified.py) (modified)

## Original program output

```text
Dominant eigenvalue: 2.561552812808829
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.5059797815742444e-15
```

## B. Inputs and mathematical operation

**Input values:** the 4 x 4 adjacency matrix of a small network with nodes A, B, C, D (1 means two nodes are connected).

**Mathematical operations:** compute all eigenvalues and eigenvectors with `np.linalg.eig`, choose the largest eigenvalue, take the matching eigenvector, make its entries positive and scale them to add to 1 (the importance score), and verify that A v = lambda v.

## C. Changing a parameter

**Change made:** a new link between A and D was added.

**Effect:** the network became fully connected. The dominant eigenvalue rose from 2.5616 to 3.0, and all four nodes now have equal importance (0.25 each). When every node connects to every other node, none is more important.

## D. Meaning of the output

The dominant eigenvalue is 2.5616. B and C are most important (0.2808 each) because they connect to three nodes, while A and D score 0.2192 because they connect to only two. The verification error (about 1.5e-15) is essentially zero, so the eigenvector is correct. There is no graph.

## E. Modified program for a related real-world case

**New case:** importance of towns in a matatu route network.

**Assumptions:** this is an assumed example network for practice, not real route data. Links: Nairobi-Thika, Nairobi-Ruiru, Nairobi-Kiambu, Ruiru-Juja, Juja-Thika, Ruiru-Kiambu.

**Interpretation:** Nairobi and Ruiru score highest (0.2406 each), then Kiambu (0.1939), then Thika and Juja (0.1624). Towns with more connections, and connections to other well-connected towns, score higher.

**Output of the modified program** (Part C comparison, then Part E case):

```text
PART C - Original: dominant eigenvalue=2.5616, importance A,B,C,D = [0.2192 0.2808 0.2808 0.2192]
PART C - With A-D link: dominant eigenvalue=3.0000, importance A,B,C,D = [0.25 0.25 0.25 0.25]

PART E - town network, dominant eigenvalue: 2.4812
Nairobi : 0.2406
Ruiru   : 0.2406
Kiambu  : 0.1939
Thika   : 0.1624
Juja    : 0.1624
```
