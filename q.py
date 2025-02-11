import numpy as np

# Create a 1D NumPy array
original_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Split the array into 3 equal parts
split_arrays = np.array_split(original_array, 3)

# Print the original array and the split arrays
print("Original Array:")
print(original_array)

print("\nSplit Arrays:")
for i, array in enumerate(split_arrays):
    print(f"Array {i + 1}: {array}")