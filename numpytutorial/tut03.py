#numpy functions
import numpy as np
#1.arrange()
arr_1d = np.arange(1,10)
print(arr_1d)  #here values from 1 to 10 are in array where 10 is excluded
print("*****************************************************************")

arr_1ds = np.arange(1,20,2) #two is the value of steps
print(arr_1ds) #here integers values from 1 to 20  are in array with break of 2 points where 20 is excluded
print("*****************************************************************")
#2.linespace() :- for creating numeric sequences
arr_1d_2 = np.linspace(1.0,1.1,8) #here 8=number of values we want
print(arr_1d_2)  #it gives random 8 values from 1 to 5
print("*****************************************************************")
#3.reshape:-it converts the 1d array into mutidimensional array
arr_new_2d = arr_1d.reshape(3,3)
print(arr_new_2d)  #here we convert 1d array of 3x3 where mxn=3x3  #size of 1d array = mxn
print("convert in 3d array")
               #convert in 3d array
arr_new_3d = arr_1d.reshape((3,3,1))  #3d array
print(arr_new_3d)
arr_dir = np.arange(1,101).reshape(10,10)  #10d array
print(arr_dir)
print("*****************************************************************")
#4.Ravel():-converts multidimensional array in 1d array
print(arr_dir.ravel())
print("*****************************************************************")
#5.flaten:-It is same as Ravel()
#6.Transpose():-it converts row to column and column to row
print(arr_dir.transpose())

