import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics

leagueWins = {'Team':['Manchester United','Blackburn Rovers','Arsenal','Chelsea','Manchester City','Leicester City','Liverpool'],
             'Championships':[13,1,3,5,5,1,1]}

teamColours=['#f40206','#0560b5','#ce0000','#1125ff','#28cdff','#091ebc','#D00027']

df = pd.DataFrame(leagueWins, columns=['Team', 'Championships'])
plt.pie(df['Championships'],labels = df['Team'],colors = teamColours, startangle = 90)
plt.title("Premier League Titles")
plt.tight_layout()
plt.show()
