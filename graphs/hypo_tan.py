import numpy as np
import matplotlib.pyplot as plt

x_sin = np.arange(0 , 3 * np.pi ,0.1)
y_tanh = np.sin(x_sin)
print(x_sin)
print(y_tanh)

plt.plot(x_sin , y_tanh)
plt.show()