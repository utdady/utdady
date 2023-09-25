import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = pd.read_csv("manUtd_20_21.csv")

dataAssists = data[data["A"]>0]

norm = matplotlib.colors.Normalize(vmin=min(dataAssists.A), vmax=max(dataAssists.A))
colors = [matplotlib.cm.Reds(norm(value)) for value in dataAssists.A]

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(16, 4.5)

fig = plt.gcf()
fig.set_size_inches(16, 4.5)

squarify.plot(label=dataAssists.PLAYER,sizes=dataAssists.A, color = colors, alpha=.6)
plt.title("Man Utd Assists",fontsize=23,fontweight="bold")

plt.axis('off')
plt.show()
