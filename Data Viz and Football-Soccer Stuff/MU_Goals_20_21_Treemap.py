import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = pd.read_csv("manUtd_20_21.csv")

dataGoals = data[data["G"]>0]

norm = matplotlib.colors.Normalize(vmin=min(dataGoals.G), vmax=max(dataGoals.G))
colors = [matplotlib.cm.Blues(norm(value)) for value in dataGoals.G]

fig = plt.gcf()
ax = fig.add_subplot()
fig.set_size_inches(16, 4.5)

squarify.plot(label=dataGoals.PLAYER,sizes=dataGoals.G, color = colors, alpha=.6)
plt.title("Man Utd Goals",fontsize=23,fontweight="bold")

plt.axis('off')
plt.show()
