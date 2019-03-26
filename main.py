import pandas as pd

FIFA = pd.read_csv('2019/data.csv')
list(FIFA)
FIFA['Interceptions'].mean()
ronaldo = FIFA[FIFA['Name'] == 'Cristiano Ronaldo']
messi = FIFA[FIFA['Name'] == 'L. Messi'

FIFA.Age.mean()
#The average age of all players is 25.12

Bayern = FIFA[FIFA.Club.str.contains('FC Bayern', regex=False)==True]

Bayern.Age.mean()
#The average age of all Bayern players is 24.31

Bayern.Age.mean()<FIFA.Age.mean()
#This statement compares average Bayern players age to all FIFA players, and Bayern players are younger than FIFA players