import numpy as np
import numpy as numpi

list1 = [1, 2, 3]
list2 = [3, 4, 6]
array1 = numpi.array(list1)
array2 = numpi.array(list2)

print(array1+array2)
print(array1*array2)
print(array1-array2)
print(array1/array2)
print(array1.shape)
print(array1[2])


array3 = numpi.arange(1, 4)
print(array3)

print(np.linspace(1, 5, 3))
print(np)

print(np.sqrt(25))
print(np.sum(array1))
print(np.min(array1))
print(np.max(array1))

# STANDARD DEVIATION
print("STANDARD DEVIATION", np.std(array1))

