import numpy as np

#single Dimension array
a=np.array([1,2,3])

print("size of each item in the array:",a.itemsize)
print("no of elements in the array:",a.size)
print("Dimension of the array is:",a.ndim)
print("shape of the array is:",a.shape)

#Two dimension array

b=np.array([[1,2],[3,4],[5,6]])
print("========================================")
print("size of each element in the array:",b.itemsize)
print("no of elements in the array is:",b.size)
print("Dimension of the array:",b.ndim)
print("shape of the array is:",b.shape)
