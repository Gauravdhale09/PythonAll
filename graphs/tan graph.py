import numpy as np
import matplotlib.pyplot as plt

x_sin = np.arange(0 , 3 * np.pi ,0.1)
y_tan = np.tan(x_sin)
print(x_sin)
print(y_tan)

plt.plot(x_sin , y_tan)
plt.show()