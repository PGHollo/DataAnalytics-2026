# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

# Original variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

print("Original Variables")
print("------------------")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print()
print("Conversion Tests")
print("----------------")

# Variable a tests
# int_a = int(a)  # ValueError: invalid literal for int() with base 10
float_a = float(a)
int_float_a = int(float(a))
slice_a = int(float(a[1:6]))
strip_a = a.strip()

print(f"a as float: {float_a}, type: {type(float_a)}")
print(f"a as float then integer: {int_float_a}, type: {type(int_float_a)}")
print(f"a sliced numeric portion: {slice_a}, type: {type(slice_a)}")
print(f"a stripped: {strip_a}, type: {type(strip_a)}")

print()

# Variable b tests
int_b = int(b)
float_b = float(b)
slice_b = int(b[0:2])

print(f"b as integer: {int_b}, type: {type(int_b)}")
print(f"b as float: {float_b}, type: {type(float_b)}")
print(f"b sliced numeric portion: {slice_b}, type: {type(slice_b)}")

print()

# Variable c tests
# int_c = int(c)  # ValueError: invalid literal for int() with base 10
# float_c = float(c)  # ValueError: could not convert string to float
slice_c = int(c[0:3])

print(f"c sliced numeric portion: {slice_c}, type: {type(slice_c)}")

print()

# Variable d tests
# int_d = int(d)  # ValueError: invalid literal for int() with base 10
# float_d = float(d)  # ValueError: could not convert string to float
slice_d = int(d[7:8])
strip_d = d.strip()

print(f"d sliced numeric portion: {slice_d}, type: {type(slice_d)}")
print(f"d stripped: {strip_d}, type: {type(strip_d)}")