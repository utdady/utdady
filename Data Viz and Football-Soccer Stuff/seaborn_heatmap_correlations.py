import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('fifa_21_dataset.csv', encoding = 'ANSI')
data = data.drop(['sofifa_id','player_url','preferred_foot','work_rate','short_name','long_name','dob','height_cm','weight_kg'], axis=1)
data = data.head(2)

fig, ax = plt.subplots()
fig.set_size_inches(14, 10)

ax=sns.heatmap(data.corr())
plt.show()
