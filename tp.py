import numpy as np

# Create an array
a = np.linspace(1, 10, 5)
print("Array a:", a)

# Accessing elements
print("First element:", a[0])
print("Last element:", a[-1])

# Slicing
print("First three elements:", a[:3])

# Modifying elements
a[0] = 99
print("Modified array a:", a)

# Multidimensional array
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array b:\n", b)

# Accessing elements in 2D array
print("Element at (0, 0):", b[0, 0])
print("Element at (1, 2):", b[1, 2])

# Slicing 2D array
print("First two rows:\n", b[:2, :])