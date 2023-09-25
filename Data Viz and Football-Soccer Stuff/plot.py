import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

leagueWins = {'Team': ['Manchester United', 'Blackburn Rovers', 'Arsenal',
                       'Chelsea', 'Manchester City', 'Leicester City'],
              'Championships': [13, 1, 3, 4, 2, 1]}
df = pd.DataFrame(leagueWins, columns=['Team', 'Championships'])
plt.pie(df['Championships'])
teamColours = ['#f40206', '#0560b5', '#ce0000', '#1125ff', '#28cdff', '#091ebc']
plt.pie(df['Championships'], labels=df['Team'], colors=teamColours, startangle=90)
plt.title("Premier League Titles")
plt.tight_layout()
