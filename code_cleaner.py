import pandas as pd

df = pd.read_csv('AllDatas.csv')

print(df.shape)

print(df.isnull().sum())