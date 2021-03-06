import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

FIFA = pd.read_csv('2019/data.csv')
list(FIFA)
FIFA['Interceptions'].mean()
ronaldo = FIFA[FIFA['Name'] == 'Cristiano Ronaldo']
messi = FIFA[FIFA['Name'] == 'L. Messi']

np.mean(FIFA['Age'])
FIFA.Age.mean()
#The average age of all players is 25.12

Bayern = FIFA[FIFA.Club.str.contains('FC Bayern', regex=False)==True]

Bayern.Age.mean()
#The average age of all Bayern players is 24.31

Bayern.Age.mean()<FIFA.Age.mean()
#This statement compares average Bayern players age to all FIFA players, and Bayern players are younger than FIFA players

plt.plot(Bayern['Age'], Bayern['Stamina'], marker='.', linestyle='none')
plt.xlabel('Age of Player')
plt.ylabel('Stamina of Player')
plt.show()