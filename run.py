

import numpy as np
import matplotlib.pyplot as plt
def Sin(x):
  return np.sin(x)
def Cos(x):
  return np.cos(x)
x = np.linspace(-np.pi, np.pi)
y_sin = Sin(x)
y_cos = Cos(x)
plt.plot(x, y_sin, label="sin")
plt.plot(x, y_cos, label="cos")
plt.legend()

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()

plt.show()
