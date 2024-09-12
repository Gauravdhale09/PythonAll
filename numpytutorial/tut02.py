import numpy as np
#to make 1d array of all value equal to one with float datatype
ones_array1d = np.ones((4), dtype=bool)
print("1d array of 4 elements=",ones_array1d)
print("*****************************************************************")
#to make 2d array of m rows and n columns
ones_array2d = np.ones((3,4), dtype=bool)
print(ones_array2d)  #here m=3 and n=4
print("*****************************************************************")
#if we want integer datatype
ones_array2di = np.ones((3,4),dtype=int)
print(ones_array2di)
#to covert the datatype in boolean form
ones_array2db = np.ones((3,4),dtype=int)
print(ones_array2db) #output shows that ones show true while 0 sho false
zero_array2db = np.zeros((3,4),dtype=bool)
print(zero_array2db) # zero means false
print("*****************************************************************")
#to make the  matrix of random values of mxn
#emptymx = np.empty((4,5))
#print(emptymx)

