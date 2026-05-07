import math

# Ask the user for the first coordinate
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Ask the user for the second coordinate
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Display the result
print(f"The distance between the two points is {distance:.2f}")