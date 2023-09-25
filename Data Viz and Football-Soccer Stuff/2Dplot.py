from matplotlib import pyplot as plt
import numpy as np
import math 
x = np.arange(0, math.pi*2, 0.05) # make an array of values from 0.0 to 2π with a step 0.05
y = np.sin(x)                     # make an array of values using the function sin(x) 
plt.plot(x,y)                     # create a line plot
plt.xlabel("angle")               # add a label for the x axis
plt.ylabel("sine")                # add a label for the y axis
plt.title('sine wave')            # add a title for the plot
plt.show()                        # create a GUI window and visualize the plot
