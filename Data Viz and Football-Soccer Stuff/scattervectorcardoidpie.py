import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(tight_layout=True)

ax = fig.add_subplot(2, 2, 1) # using a different approach to arrange plots
filename = 'data.txt'       # you need to download the file from the canvas
data = np.loadtxt(filename) # load data from a file
col1 = data[:,0]            # make array of data in the 1st column
col2 = data[:,1]            # make array of data in the 2nd column
ax.scatter(col1, col2, s=1.5, color='green')
ax.set_title("Scatter")
ax.set_xlabel('x')
ax.set_ylabel('y')

ax = fig.add_subplot(2, 2, 2)
ax.set_title("Vector Field")
x,y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2))
z = x*np.exp(-x**2 - y**2)
v, u = np.gradient(z, 0.2, .2)
ax.quiver(x,y,u,v)

ax = fig.add_subplot(2, 2, 3)
ax.set_title("Pie Plot")
major = ['Bio', 'Chem', 'Physics', 'Arts', 'Math']
students = [25,18,45,23,11]
ax.pie(students, labels = major,autopct='%1.0f%%')

ax = fig.add_subplot(2, 2, 4, polar=True)
ax.set_title("Cardioid")
theta = np.linspace(0, 2*np.pi, 100)
r =2*(1 - np.cos(theta))
ax.plot(theta, r, color='red')
plt.show()
