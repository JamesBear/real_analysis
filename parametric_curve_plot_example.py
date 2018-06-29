
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import math
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

# Prepare arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
r2 = z+1
x = r * np.sin(theta)
y = r * np.cos(theta)
x2 = r2 * np.sin(theta)
y2 = r2 * np.cos(theta)

ax.plot(x, y, z, label='parametric curve, r = z^2+1')
ax.plot(x2, y2, z, label='parametric curve, r = z')
ax.legend()

plt.show()
