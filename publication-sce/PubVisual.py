import pandas as pd
from datetime import date
import numpy as np


df = pd.read_csv('publications.csv')

print(df.dtypes)

df = df.sort_values(by='cites', ascending=False)

#print(df)

df2 = df[df['cites']>49]
df2 = df2.drop(columns='id')
today = date.today() # todays date

# adding last updated to the dataframe
df2['lastUpdated'] = today

df2.to_csv("pubEval.csv",index=False)

print(df2)