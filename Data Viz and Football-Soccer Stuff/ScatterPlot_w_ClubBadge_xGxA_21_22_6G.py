import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

df = pd.read_csv('xGxA_21_22_6G.csv')
df['path'] = df['Squad'] + '.png'

plt.rcParams.update({'font.family':'DejaVu Sans'})
bgcol = '#fafafa'

fig, ax = plt.subplots(figsize=(6, 4), dpi=120)
fig.set_facecolor(bgcol)
ax.set_facecolor(bgcol)
ax.scatter(df['xG'], df['xGA'], c=bgcol)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('#ccc8c8')
ax.spines['bottom'].set_color('#ccc8c8')

plt.tick_params(axis='x', labelsize=12, color='#ccc8c8')
plt.tick_params(axis='y', labelsize=12, color='#ccc8c8')

def getImage(path):
    return OffsetImage(plt.imread(path), zoom=0.1, alpha = 1)

for index, row in df.iterrows():
    ab = AnnotationBbox(getImage(row['path']), (row['xG'], row['xGA']), frameon=False)
    ax.add_artist(ab)

plt.hlines(df['xGA'].mean(), df['xG'].min(), df['xG'].max(), color='#c2c1c0')
plt.vlines(df['xG'].mean(), df['xGA'].min(), df['xGA'].max(), color='#c2c1c0')

fig.text(.15,.95,'xG Performance, Weeks 1-6',size=18)
fig.text(.15,.90,'Top Left is bad, Botttom Right is ideal', size=10)

fig.text(.06,.14,'xG Against', size=9, color='#575654',rotation=90)
fig.text(.12,0.05,'xG For', size=9, color='#575654')

fig.text(.76,.535,'Avg. xG Against', size=6, color='#c2c1c0')
fig.text(.325,.17,'Avg. xG For', size=6, color='#c2c1c0',rotation=90)

plt.savefig('xGChart.png', dpi=1200, bbox_inches = "tight")
plt.show()
