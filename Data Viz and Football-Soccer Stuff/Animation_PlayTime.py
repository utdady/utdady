import os
import pandas as pd
import numpy as np
import calendar
import matplotlib.pyplot as plt
import imageio
import random

def return_random_hex():
    r = lambda: random.randint(0,255)
    return('#%02X%02X%02X' % (r(),r(),r()))

df = pd.read_csv('20_21_PlayTime.csv')
leagues = {'English Premier League': 'd1', 'Ligue 1': 'd2', 'Bundesliga': 'd3', 'Serie A': 'd4', 'La Liga': 'd5'}

for index,league in enumerate(leagues):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    col = return_random_hex()
    for league2 in leagues:
        (df[df['League']==league2]['Age'].value_counts(normalize=True)*100).sort_index().plot(color = 'gray')
        (df[df['League']==league]['Age'].value_counts(normalize=True)*100).sort_index().plot(color = col)
    plt.text(1,15,'Players by Age', fontsize=22, fontweight=300)
    plt.text(1,14,league, fontsize=16, color=col, fontweight=600)
    plt.xlabel('Age')
    plt.ylabel('No.of Players')
    plt.tight_layout()
    plt.savefig(str(index) + '.png')

with imageio.get_writer('mybettergif.gif', mode='I') as writer:
  for index in range(0,4):
     for i in range(0,6):
        image = imageio.imread(str(index) + '.png')
        writer.append_data(image)
