#1D array
import numpy as np


arr_1d = np.array([10, 20, 30, 40, 50])

print(" === 1D Array === ")
print(arr_1d)


print("First element:", arr_1d[0])
print("Third element:", arr_1d[2])
print("Last element:", arr_1d[-1])

print("\n")


#2d array

arr_2d = np.array([
[1, 2,3],
[4,5,6],
[7,8,9]
])

print(" === 2D Array === ")
print(arr_2d)

# Accessing elements in 2D array
# Syntax: array[row] [column]

print("Element at row 0, col 0:", arr_2d[0][0])
print("Element at row 1, col 2:", arr_2d [1][2])
print("Element at row 2, col 1:", arr_2d [2] [1])

print("\n")




arr_3d = np.array([
	[[1, 2],
	 [3, 4]],
	[[5, 6],
	 [7, 8]]
])

print(" === 3D Array === ")
print(arr_3d)

# Accessing elements in 3D array
# Syntax: array[layer][row][column]

print("Element at layer 0, row 1, col 1:", arr_3d[0][1][1])
print("Element at layer 1, row 0, col 0:", arr_3d[1][0][0])

print("\n === End of Program === ")
