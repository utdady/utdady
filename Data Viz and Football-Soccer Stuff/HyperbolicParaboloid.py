import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 
ax = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30) 
X, Y = np.meshgrid(x, y)           # make a mesh, a 2D array, and assign 2D arrays to X and Y
a,b = 0.5, 1
Z = X*X/a - Y*Y/b                  # make a 2D array and assign it to Z
ax.contour3D(X, Y, Z, 50)
ax.set_title('Hyperbolic Paraboloid')
plt.show()
