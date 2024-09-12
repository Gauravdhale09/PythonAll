#Mathmatical operation using numpy
#1.Addition of two arrays
import numpy as np
arr_1 = np.arange(1,10).reshape(3,3)
arr_2 = np.arange(11,20).reshape(3,3)
print("this are two arrays⬇")
print("arr1=")
print(arr_1)
print("arr2=")
print(arr_2)
print("*****************************************************************")
#print(arr_1+arr_2)
print("1)addition of two arrays")
add = np.add(arr_1,arr_2)
print(add)
#2.subtraction
print("2)subtraction of two arrays")
sub  = np.subtract(arr_2,arr_1)
print(sub)
#3.multiplication
print("3)element wise multiplication of two arrays")
multi_e = np.multiply(arr_1,arr_2)     #This is for element wise multiplication
print(multi_e)
#multiplication of two matrices
print("4)multiplication of 2 matrices")
multi_m = arr_1 @ arr_2
print(multi_m)
#5.To find max and min value of an array
max = arr_2.max()
min = arr_2.min()
print("max value of arr_2=",max)
print("max value of arr_2-",min)
#6.To find index of max and min value
imax = arr_2.argmax()
imin = arr_2.argmin()
print(f"index of max value of arr_2 i.e. {max}=",imax)
print(f"index of max value of arr_2 i.e. {min}=",imin)
print("max row  of arr_2=",arr_2.max(axis=0))
print("max column  of arr_2=",arr_2.max(axis=1))
print("sum of every element of arr_2=",np.sum(arr_2))
print("sum of every row of arr_2=",np.sum(arr_2,axis=0))
print("sum of every column of arr_2=",np.sum(arr_2,axis=1))
print("Average value of matrix arr_2=",np.mean(arr_2))
print("square root of every element of arr_2=")
print(np.sqrt(arr_2))
print("standard division of arr_2=",np.std(arr_2))
print("exponent of every element of arr_2=")
print(np.exp(arr_2))
print("Natural log of every element of arr_2=")
print(np.log(arr_2))
print("log to the base 10=")
print(np.log10(arr_2))

