from __future__ import unicode_literals
import joypy
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm

df = pd.read_csv("top250.csv")

fig, axes = joypy.joyplot(df[df.Name != 'Neymar'], by="Season", column="Transfer_fee",figsize=(5,8),linewidth=0.05,overlap=3,colormap=cm.summer_r,x_range=[0,110000000])

plt.text(70, 0.9, "Top 250 transfers \n 2000-2018",fontsize=12)

plt.show()
