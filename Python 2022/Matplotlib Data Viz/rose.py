'''
Prompt: Write a program that creates a rose curve in polar coordinates Rose
        (mathematics) - Wikipedia (Links to an external site.). Add widgets
        (two sliding bars) that can control the curve parameters n and d that
        define the angular frequency k, (k = n /d).
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button

def isEven(n):
    s = str(n)
    l = len(s)
    dotSeen = False
    for i in range(l - 1, -1, -1 ):
        if s[i] == '0' and dotSeen == False:
            continue
        if s[i] == '.':
            dotSeen = True
            continue
        if int(s[i]) % 2 == 0:
            return True
              
        return False

theta = np.linspace(16 * -np.pi, 16 * np.pi, 1000000)

# The parametrized function to be plotted
def f(theta, n, d):
    if isEven(float(n / d)):
        return np.cos(((n * 2) / d) * theta)
    else:
        return np.cos((n / d) * theta)

# Define initial parameters
init_n = 0
init_d = 1

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = plt.polar(theta , f(theta, init_n, init_d))
plt.axis('off')

# adjust the main plot to make room for the sliders
plt.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(ax=axfreq, label='d', valmin=1, valmax=10, valinit=init_n, valstep=1)

# Make a vertically oriented slider to control the amplitude
axamp = plt.axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(ax=axamp, label='n', valmin=1, valmax=10, valinit=init_d, orientation="vertical", valstep=1)

# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(f(theta, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()


# register the update function with each slider
freq_slider.on_changed(update)
amp_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    freq_slider.reset()
    amp_slider.reset()
button.on_clicked(reset)

plt.show()
