import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = pd.read_csv("pos_vs_value_2008_to_2020.csv")

#sns.pairplot(data[['Season','GD','Squad_Value','Points','Position']])

#1- Get our two columns into variables, then reshape them

'''x = data['Squad_Value']
y = data['Points']

x = x.values.reshape(-1,1)
y = y.values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=101)

lm = LinearRegression()
lm.fit(x_train,y_train)

predictions = lm.predict(x_test)'''

#Blank list
relativeValue = []

#Loop through each row
for index, team in data.iterrows():
    
    #Obtain which season we are looking at
    season = team['Season']
    
    #Create a new dataframe with just this season
    teamseason = data[data['Season'] == season]
    
    #Find the max value
    maxvalue = teamseason['Squad_Value'].max()
    
    #Divide this row's value by the max value for the season
    tempRelativeValue = team['Squad_Value']/maxvalue
    
    #Append it to our list
    relativeValue.append(tempRelativeValue)
    
#Add list to new column in main dataframe
data["Relative_Value"] = relativeValue


#Assign relevant columns to variables and reshape them
x = data['Relative_Value']
y = data['Points']
x = x.values.reshape(-1,1)
y = y.values.reshape(-1,1)

#Create training and test sets for each of the two variables
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=101)

#Create an empty model, then train it against the variables
lm = LinearRegression()
lm.fit(x_train,y_train)

predictions = lm.predict(x_test)

plt.title('How many points out is each prediction?')
sns.distplot((y_test-predictions),bins=50,color='purple')
plt.show()
