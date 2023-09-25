import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('fifa_21_dataset.csv',encoding='ANSI')
clubs = data[data['league_name'] != 'English Premier League'].index
data.drop(clubs, inplace = True)

teamColours = ['#5CBFEB','#D00027','#001C58','#034694','#DA020E','#EF0107','#0053A0','#274488','#ffb700','#1B458F','#000000','#000000','#53162f','#ffff00','#60223B','#811331','#0073ff','#091453','#ED1A3B','#ad0000']

fig, ax = plt.subplots()
fig.set_size_inches(14, 5)

sns.boxplot(x='club_name', y='age', data=data, palette = teamColours)
plt.xticks(rotation=65)
plt.show()
