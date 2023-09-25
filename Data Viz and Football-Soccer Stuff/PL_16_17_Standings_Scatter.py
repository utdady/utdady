import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

table = pd.read_csv("16_17table.csv")

fig, ax = plt.subplots()
fig.set_size_inches(7,5)

plt.plot(table['GF'],table['GA'],"o")
plt.plot([table['GF'].mean(),table['GF'].mean()],[90,20],'k-',linestyle=":",lw=1)
plt.plot([20,90],[table['GA'].mean(),table['GA'].mean()],'k-',linestyle=":",lw=1)

ax.set_title("Goals for & Against")
ax.set_xlabel("Goals For")
ax.set_ylabel("Goals Against")

ax.text(18,90,"Poor attack, poor defence",color="red",size="8")
ax.text(67,20,"Strong attack, strong defence",color="red",size="8")

plt.show()
