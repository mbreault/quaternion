import numpy as np
import quaternion  # This imports the numpy-quaternion extension

# Create a quaternion representing a 90-degree rotation around the Z-axis
angle = np.radians(90)  # Convert 90 degrees to radians
axis = np.array([0, 0, 1])  # Z-axis
rotation_quaternion = quaternion.from_rotation_vector(angle * axis)

# Define a 3D vector to rotate (e.g., a point in 3D space)
vector = np.array([1, 0, 0])  # X-axis unit vector

# Rotate the vector using the quaternion
rotated_vector = quaternion.rotate_vectors(rotation_quaternion, vector)

# Output the rotated vector
print(rotated_vector)
