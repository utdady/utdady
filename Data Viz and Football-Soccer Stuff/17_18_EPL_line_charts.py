import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("17_18E.csv")

Teams = data.HomeTeam.unique()
TeamLists = {Team: [0] for Team in Teams}

for row in data.itertuples():

    Home = row.HomeTeam
    Away = row.AwayTeam
    
    if row.FTHG > row.FTAG:
        TeamLists[Home].append(TeamLists[Home][-1] + 3)
        TeamLists[Away].append(TeamLists[Away][-1] + 0)

    elif row.FTHG < row.FTAG:
        TeamLists[Home].append(TeamLists[Home][-1] + 0)
        TeamLists[Away].append(TeamLists[Away][-1] + 3)

    else:
        TeamLists[Home].append(TeamLists[Home][-1] + 1)
        TeamLists[Away].append(TeamLists[Away][-1] + 1)

Matchday = list(range(0,39))

fig, ax = plt.subplots()

plt.plot(Matchday, TeamLists["Man City"], color = "#6CABDD", linewidth = 2)
plt.plot(Matchday, TeamLists["Swansea"], color = "#231F20", linewidth = 2)

plt.xlabel('GameWeek')
plt.ylabel('Points')
plt.title('Man City v Swansea Running Points')

plt.grid()
ax.xaxis.grid(color = "#F8F8F8")
ax.yaxis.grid(color = "#F9F9F9")
plt.margins(x=0,y=0)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.show()
