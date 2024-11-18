import numpy as np

a = np.logspace(1,4,5)

print(a)

n = len(a)

for i in range(n):
    print('%.1f' % a[i], end=' ')

    