import numpy as np
arr1  = np.array([1,2,3,4,5])
print("one dimension array=",arr1)
print("type=",type(arr1))
print("shape of array=",arr1.shape)  
print("dimensions of array=",arr1.ndim)

#two dimension array
arr_2d = np.array([[1,2,3,4],[5,6,7,8]])
print("two dimension array=\n",arr_2d)
print("size of 2d array=",arr_2d.size)
print("shape of 2d array=",arr_2d.shape)  # 2 is row and 4 is column
print("dimensions of 2d array=",arr_2d.ndim)

# 4D array
l1 = [1,2,4,5]
l2 = [6,7,8,9]
l3 = [10,11,12,24]
l4 = [25,26,26,21]
arr4 = np.array([l1, l2, l3, l4])

print(arr4)
