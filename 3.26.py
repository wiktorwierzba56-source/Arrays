import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for n in range(0, 361):
    x.append(n)

for n in x:
    y.append(np.sin(np.radians(n)))  # Przekształcamy stopnie na radiany

plt.plot(x, y)
plt.xlabel("x (stopnie)")
plt.ylabel("y (sin(x))")
plt.show()
