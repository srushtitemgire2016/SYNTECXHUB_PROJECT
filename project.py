import numpy as np
import time

print("===== NUMPY DATA EXPLORER =====\n")

# 1. Array Creation, Indexing & Slicing
arr = np.arange(1, 13)   # 1 to 12
print("Original Array:", arr)

print("Indexing Example (3rd element):", arr[2])
print("Slicing Example (5th to 9th elements):", arr[4:9])

# 2. Reshaping Array
reshaped = arr.reshape(3, 4)
print("\nReshaped Array (3x4):\n", reshaped)

# 3. Axis-wise Operations
print("\nRow-wise Sum:", reshaped.sum(axis=1))
print("Column-wise Sum:", reshaped.sum(axis=0))

# 4. Mathematical & Statistical Operations
print("\nSquare of each element:\n", reshaped ** 2)
print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())
print("Max Value:", arr.max())

# 5. Broadcasting Example
b = np.array([10, 20, 30, 40])
broadcast_result = reshaped + b
print("\nBroadcasting Result (reshaped + [10,20,30,40]):\n", broadcast_result)

# 6. Saving & Loading NumPy Arrays
np.save("data.npy", arr)
loaded_arr = np.load("data.npy")
print("\nSaved and Loaded Array:", loaded_arr)

# 7. Performance Comparison with Python List
big_size = 10_00_000
numpy_arr = np.arange(big_size)
python_list = list(range(big_size))

start = time.time()
numpy_arr * 2
numpy_time = time.time() - start

start = time.time()
[x * 2 for x in python_list]
python_time = time.time() - start

print("\n===== PERFORMANCE TEST =====")
print("NumPy Execution Time:", numpy_time)
print("Python List Execution Time:", python_time)
print("\nNumPy is faster by:", python_time - numpy_time, "seconds")
