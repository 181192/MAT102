import random

import matplotlib.pyplot as plt
import numpy as np

n = 100  # number of steps

x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)

for i in range(n - 1):
    t = random.uniform(0, 1)
    if t < 0.5:
        x[i + 1] = x[i] + 1
    else:
        x[i + 1] = x[i] - 1
    t = random.uniform(0, 1)
    if t < 0.5:
        y[i + 1] = y[i] + 1
    else:
        y[i + 1] = y[i] - 1
    t = random.uniform(0, 1)
    if t < 0.5:
        z[i + 1] = z[i] + 1
    else:
        z[i + 1] = z[i] - 1
    plt.plot(x, y)

plt.show()
