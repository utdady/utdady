'''
Prompt: Write a program dice.py that calculates sums of two dice that are thrown
        hundred times (you can use randint). Record sums and trials as two
        integer arrays. Then create a scatter, line, histogram, and pie plots of
        the obtained data. Your plots should be arranges as 2x2 matrix.
'''

import random
import matplotlib.pyplot as plt
import numpy as np

sums = []
for i in range(100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    s = dice1 + dice2
    sums.append(s)

fig = plt.figure(tight_layout=True)

# scatter plot
ax = fig.add_subplot(2, 2, 1)
data = np.array(sums)
trials = np.arange(1,101)
ax.scatter(trials, data, s=1.5, color='green')
ax.set_title("Scatter")
ax.set_xlabel('trials')
ax.set_ylabel('sums')

# pie plot
ax = fig.add_subplot(2, 2, 4)
ax.set_title("Pie Plot")
nums = [i for i in range(2,13)]
n = np.array([sums.count(j) for j in nums])
ax.pie(n, labels=nums, autopct='%1.0f%%')

# histogram
ax = fig.add_subplot(2, 2, 3)
ax.set_title("Histogram")
ax.hist(data)

# line plot
ax = fig.add_subplot(2, 2, 2)
ax.set_title("Line Plot")
ax.plot(data, linestyle='dotted')

plt.show()
