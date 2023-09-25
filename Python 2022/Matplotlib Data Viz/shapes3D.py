import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#mpl.rcParams['legend.fontsize'] = 10


ax = plt.axes(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = (2.718) ** z
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot3D(x, y, z, label='parametric curve')
ax.legend()

plt.show()
