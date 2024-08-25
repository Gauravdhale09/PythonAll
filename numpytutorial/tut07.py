#Random module python
import numpy as np
import random
#print(np.random.random(1))  #it prints any random value from 0 to 1
#to create any random array of mxn
arr_1 = np.random.random((3,2))
print(arr_1)
print("*************************************************************************8")
#TO print any integer value from specific range
x = np.random.randint(100,102,100)  #it prints 2 random values from 1 to 101(excluding 101)
print(x)
print("*************************************************************************8")
#TO make an 2d array of random numbers using rows and columns
y= np.random.randint(1,1033,(6,4))
print(y)
print("*************************************************************************8")
#to create 3d array
z=np.random.randint(1,454,(2,4,4))  #two arrays of 4x4
print(z)
print("*************************************************************************8")
