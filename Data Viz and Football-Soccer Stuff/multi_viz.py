import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from mplsoccer.pitch import Pitch

colors = ['red', 'skyblue', 'navy', 'pink', 'green', 'black']

teams = ['United', 'City', 'Albion', 'Athletic', 'FC', 'County']
xGFor = np.random.rand(200)*3
xGAgainst = np.random.rand(200)*3
teamsArray = np.random.choice(teams, 200)
df = pd.DataFrame({'Team':teamsArray,'xGFor':xGFor, 'xGAgainst':xGAgainst})

fig, ax = plt.subplots(2, 3, sharex='col', sharey='row', figsize = (6,3), dpi = 140)

for count, item in enumerate(ax.reshape(-1)):

     item.hist(df[df['Team']==teams[count]]['xGFor'],10, color = colors[count],range=[0, 3])

     item.text(0.1,0.8,teams[count],transform=item.transAxes)

     item.set_ylim([0,10])
     item.set_xlim([0,3])

     fig.text(0.5, -0.02, 'xGFor', ha='center', va='center')
     fig.text(0.06, 0.5, 'Frequency', ha='center', va='center', rotation='vertical')

df = pd.DataFrame(np.random.randint(0,100,size=(200, 2)), columns=['X', 'Y'])
fig = plt.figure(figsize=(5,5), dpi = 140)
grid = plt.GridSpec(6, 6)

a1 = fig.add_subplot(grid[0:5, 0:5])
a2 = fig.add_subplot(grid[5, 1:4],sharex=a1)
a3 = fig.add_subplot(grid[0:5, 5],sharey=a1)

pitch = Pitch(pitch_type='opta', orientation='vertical', stripe=False)
pitch.draw(ax=a1)
pitch.scatter(df['X'], df['Y'],
                    s=10, c='black', label='scatter', ax=a1)

a2.hist(df['Y'], 3, color = 'black', histtype='stepfilled')
a3.hist(df['X'], 9, orientation='horizontal', color='black', histtype='stepfilled')


df = pd.DataFrame(np.random.randint(0,100,size=(200, 2)), columns=['X', 'Y'])
fig = plt.figure(figsize=(5,5), dpi = 140)
grid = plt.GridSpec(6, 6, wspace=-0.45, hspace=0.2)

a1 = fig.add_subplot(grid[0:5, 0:5])
a2 = fig.add_subplot(grid[5, 1:4],sharex=a1)
a3 = fig.add_subplot(grid[0:5, 5],sharey=a1)

pitch = Pitch(pitch_type='opta', orientation='vertical', pitch_color='#f7fafa', line_color='pink', stripe=False)
pitch.draw(ax=a1)
pitch.scatter(df['X'], df['Y'],
                    s=10, c='#06c7c4', label='scatter', ax=a1)

a2.hist(df['Y'], 3, color = 'pink', edgecolor="#fc8197", histtype='stepfilled')
a2.axis('off')

a3.hist(df['X'], 9, orientation='horizontal', color='pink', edgecolor="#fc8197", histtype='stepfilled')
a3.axis('off')

plt.text(-64.8,110,'Player X - Touches', size=14)
fig.set_facecolor('#ffffff')

plt.show()
