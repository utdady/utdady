import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("fifa_21_dataset.csv",encoding='ANSI')

sns.regplot(x="attacking_crossing",y="attacking_finishing",data=df,scatter_kws={'alpha':0.07})
plt.show()
