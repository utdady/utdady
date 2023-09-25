'''
Prompt: Write a program surfaces3D.py that creates 3D plots (either contour3D,
        plot_wireframe, or plot_surface) of the following surfaces: hyperbolic
        and elliptic paraboloids, hyperbolic and elliptic hyperboloids, a sphere
        (or ellipsoid), a cone, a square pyramid, and a parallelepiped.  You are
        allowed to search for solutions on the Internet (but only for this
        question!!!).
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z)
plt.show()
