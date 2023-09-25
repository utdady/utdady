import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

standings = {'POS': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
             'TEAM': ['Chelsea','Tottenham Hotspur','Manchester City','Liverpool','Arsenal','Manchester United','Everton','Southampton','Bournemouth','West Brom','West Ham','Leicester','Stoke','Crystal Palace','Swansea','Burnley','Watford','Hull','Middlesbrough','Sunderland'],
             'W': [30,26,23,22,23,18,17,12,12,12,12,12,11,12,12,11,11,9,5,6],
             'D': [3,8,9,10,6,15,10,10,10,9,9,8,11,5,5,7,7,7,13,6],
             'L': [5,4,6,6,9,5,11,16,16,17,17,18,16,21,21,20,20,22,20,26],
             'GF': [85,86,80,78,77,54,62,41,55,43,47,48,41,50,45,39,40,37,27,29],
             'GA': [33,26,39,42,44,29,44,48,67,51,64,63,56,63,70,55,68,80,53,69],
             'GD': [52,60,41,36,33,25,18,-7,-12,-8,-17,-15,-15,-13,-25,-16,-28,-43,-26,-40],
             'PTS': [93,86,78,76,75,69,61,46,46,45,45,44,44,41,41,40,40,34,28,24]}

teamColours = ['#034694','#001C58','#5CBFEB','#D00027','#EF0107','#DA020E','#274488','#ED1A3B','#000000','#091453','#60223B','#0053A0','#E03A3E','#1B458F','#000000','#53162f','#FBEE23','#EF6610','#C92520','#BA1F1A']

plt.bar(x=np.arange(1,21),height=standings['PTS'],color=teamColours)
plt.title("Premier League 16/17")
plt.xticks(np.arange(1,21),standings['TEAM'],rotation=90)
plt.xlabel("Team")
plt.ylabel("Points")
plt.show()
