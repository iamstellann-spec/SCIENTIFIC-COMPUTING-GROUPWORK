import numpy as np

def transform(points, angle_deg, sx, sy):
    a = np.deg2rad(angle_deg)
    R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    S = np.array([[sx, 0], [0, sy]])
    T = R @ S
    return points @ T.T, T

square = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])

# ---------- PART C: change angle and scale ----------
print("PART C - angle 45->90 degrees, scale (2, 1.5) -> (3, 1.5)")
pts, T = transform(square, 90, 3.0, 1.5)
print("Transformed points:\n", np.round(pts, 4))
print("Determinant:", round(np.linalg.det(T), 4), "(original was 3.0)")

# ---------- PART E: new real-world case ----------
# Assumption: a 4 m x 3 m room plan is rotated 30 degrees and shrunk to half size to fit on a screen.
room = np.array([[0., 0.], [4., 0.], [4., 3.], [0., 3.]])
new_room, T = transform(room, 30, 0.5, 0.5)
print("\nPART E - rotating and scaling a room floor plan")
print("Transformed corners:\n", np.round(new_room, 3))
print("Determinant (area scale factor):", round(np.linalg.det(T), 4))
print("Original area:", 4 * 3, "m^2  ->  new area:", round(12 * np.linalg.det(T), 3), "units^2")
