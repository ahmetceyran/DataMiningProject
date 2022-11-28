import pandas as pd
import numpy as np
import csv

df = pd.read_csv('AllDatasV1.csv')

df = df.drop(['web-scraper-order', 'web-scraper-start-url', 'teams-href', 'playerprofile-href', 'playername'], axis = 1)

df['birthdate'] = df['birthdate'].str.replace("                                                                    "," ")

df.head()

df.shape

df.info()

df.to_csv("C:\\Users\\ahmet\\GitHub\\DataMiningProject\\AllDatasV3.csv")


