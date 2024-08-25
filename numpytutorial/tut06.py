import numpy as np
import matplotlib.pyplot as plt
print("value of pi=",np.pi)
print("Degree value of sin angles=",np.sin(90))  #it gives accurate value
#if we want to find value in randian
print("Radian value of sin angles=",np.sin(120 * np.pi/180))
print("*****************************************************************")
p = np.arange(5,51,5)
print(p)
q = np.arange(6,61,6)
print(q)
#To plot the graph of sin function
# make arrays for X and Y axis
x_sin = np.arange(0, 3*np.pi, 0.1)
print(x_sin)
y_sin = np.sin(x_sin)
#print(y_sin)
y_cos = np.cos(x_sin)
y_tan = np.tan(x_sin)
y_sinh = np.sinh(x_sin)
print(y_sinh)
y_cosh = np.cosh(x_sin)
y_tanh = np.tanh(x_sin)


#forming sinusoidal wave

plt.plot(x_sin , y_cos)
plt.show()

