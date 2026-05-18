import numpy as np

arrA = np.array([
    [11, 12, 13],
    [14, 15, 16]
])

print("\narrA:")
print(arrA)


for x in arrA:
    print(x * 2)


for x in arrA:
    for y in x:
        loop_result = y * 2
        print(loop_result)

print([x * 2 for x in range(4)]) 

