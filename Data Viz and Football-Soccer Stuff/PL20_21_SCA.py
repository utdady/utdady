import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Allow for full tables to be shown
pd.options.display.max_columns = None
pd.options.display.max_rows = None

data = pd.read_csv('PL20_21_sca.csv')
data['Player'] = data['Player'].str.split('\\', expand=True)[0]

#Split the nation names by the space, and use the second one
data['Nation'] = data['Nation'].str.split(' ', expand=True)[1]

#Some positions have 2 (e.g. MFFW), let's just use the first two letters for now
data['Pos'] = data['Pos'].str[:2]

#Create list of columns to sum, then assign the sum to a new column
add_list = ['Pass SCA', 'Deadball SCA', 'Dribble SCA', 'Shot SCA', 'Fouled SCA']
data['Sum SCA'] = data[add_list].sum(axis=1)

#Create our first new column
data['Pass SCA Ratio'] = data['Pass SCA']/data['Sum SCA']

#Create new column names by adding ' ratio' to each name in our previous list
new_cols_list = [each + ' Ratio' for each in add_list]

#For each new column name, calculate the column exactly as we did a minute ago
for idx, val in enumerate(new_cols_list):
    data[val] = data[add_list[idx]]/data['Sum SCA']

#Create a sum of the percentages to check that they all add to 1
data['Sum SCA Ratio'] = data[new_cols_list].sum(axis=1)

#New dataframe where Pos == FW or MF. AND played more than 5 90s AND created more than 15 shots
data_mffw = data[((data['Pos'] == 'FW') | (data['Pos'] == 'MF')) & (data['90s'] > 5) & (data['SCA'] > 15)]

km = KMeans(n_clusters=5, init='random', random_state=0)
y_km = km.fit_predict(data_mffw[new_cols_list])
data_mffw['Cluster'] = y_km

#We'll do this a couple of times, let's make a function
def plotClusters(xAxis, yAxis):
    plt.scatter(data_mffw[data_mffw['Cluster']==0][xAxis], data_mffw[data_mffw['Cluster']==0][yAxis], s=40, c='red', label ='Cluster 1')
    plt.scatter(data_mffw[data_mffw['Cluster']==1][xAxis], data_mffw[data_mffw['Cluster']==1][yAxis], s=40, c='blue', label ='Cluster 2')
    plt.scatter(data_mffw[data_mffw['Cluster']==2][xAxis], data_mffw[data_mffw['Cluster']==2][yAxis], s=40, c='green', label ='Cluster 3')
    plt.scatter(data_mffw[data_mffw['Cluster']==3][xAxis], data_mffw[data_mffw['Cluster']==3][yAxis], s=40, c='pink', label ='Cluster 4')
    plt.scatter(data_mffw[data_mffw['Cluster']==4][xAxis], data_mffw[data_mffw['Cluster']==4][yAxis], s=40, c='gold', label ='Cluster 5')
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)    
    plt.legend()
    plt.show()
    
plotClusters('Pass SCA Ratio', 'Dribble SCA Ratio')
plotClusters('SCA90', 'Age')
