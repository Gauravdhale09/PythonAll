#array slicing
import numpy as np
print("Array1=")
arr_1 = np.arange(1,101,2).reshape(5,10)
print(arr_1)
#print(arr_1.size)
one1 = arr_1[0,1]  #element of oth row and 0th column
print(one1)
print("Dimension of above element=",one1.ndim)
#For printing any row
print("2st row of arr_1=")
print(arr_1[1])
#For printing any column
print("2nd column of arr_2=")
print(arr_1[:,1:2])  #2nd column in 2d form
print("*****************************************************************")
#To partiate the matrix
print("partiate")
print(arr_1[0:4,3:4])
#to access whole matrix
print(arr_1[:,:])
#to print all rows with some column
print(arr_1[:,0:3])
#to print all columns with some row
print(arr_1[0:3,:])

print("*****************************************************************")
#array concatination and split
arr_2 = np.arange(101,201,2).reshape(5,10)
print("array2=")
print(arr_2)
print("*****************************************************************")
#for column wise concatinate
#conc_c = np.concatenate((arr_1,arr_2))
conc_c = np.vstack((arr_1,arr_2))
print(" column wise concatination of 2 arrays=")
print(conc_c)
print("*****************************************************************")
#for row wise concatinate
#conc_r = np.concatenate((arr_1,arr_2),axis=1)
conc_r = np.hstack((arr_1,arr_2))
print(" row wise concatination of 2 arrays=")
print(conc_r)
print("*****************************************************************************************")
#To split array
split1 = np.split(conc_c,2)  #2 is for two equal division
print(split1)
#TO split rowwise
split2 = np.split(conc_c,2,axis=1)  #default axis=0
print(split2)









