import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('PL17_18fantasy_dataset.csv', encoding = 'ANSI')
sns.pairplot(data)
plt.show()
