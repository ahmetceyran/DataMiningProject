import pandas as pd
import numpy as np
import csv
from datetime import datetime, date

#df = pd.read_csv('AllDatasV19.csv')
#df1 = pd.read_csv('AllDatasV17.csv')
#df['yearsPlayedOnLastTeam'] = df['yearSinceLastTransfer'] - df['yearSinceRetirement']
#df['retirementAge'] = df['AgeNow'] - df['yearSinceRetirement']
#df = df.drop(['AgeNow', 'yearSinceRetirement'], axis=1)
#df = df[df['retiredOrNot'].str.contains('Retired', na=False)]
#df['lastTransferFee'] = df['lastTransferFee'].str.replace("?","free transfer")
#df['lastTransferFee'] = df['lastTransferFee'].str.replace("-","free transfer")
#df.drop(df.columns[df.columns.str.contains('Unnamed',case = False)],axis = 1, inplace = True)
#df = df.drop(['teams','birthdate','retirementDate','lastTransferDate','yearSinceRetirement','AgeNow', 'yearSinceLastTransfer'], axis=1)
#def age(born):
    #born = datetime.strptime(born, "%d/%m/%Y").date()
    #today = date.today()
    #return today.year - born.year - ((today.month, 
                                      #today.day) < (born.month, 
                                                    #born.day))
  
#df['yearSinceLastTransfer'] = df['lastTransferDate'].apply(age)
#df['retirementDate'] = pd.to_datetime(df['retirementDate'], errors='coerce')

#df = df.dropna(subset=['retirementDate'])
#df = df.dropna(subset=['lastTransferDate'])
#df = df.dropna(subset=['lastTransferFee'])
#df = df.dropna(subset = ['birthdate'])
#df = pd.read_csv('AllDatasV5.csv', parse_dates=['birthdate'], dayfirst=False)
#df = pd.read_csv('AllDatasV6.csv', parse_dates=['lastTransferDate'], dayfirst=False)
#df = pd.read_csv('AllDatasV9.csv', parse_dates=['retirementDate'], dayfirst=False)

#df['birthdate'] = pd.to_datetime(df['birthdate']).dt.strftime('%d/%m/%Y')
#df['lastTransferDate'] = pd.to_datetime(df['lastTransferDate']).dt.strftime('%d/%m/%Y')
#df['retirementDate'] = pd.to_datetime(df['retirementDate']).dt.strftime('%d/%m/%Y')


#df['birthdate'] = df['birthdate'].str.replace("                                                                    ","")
#df['birthdate'] = df['birthdate'].str.replace("Jan","01/")
#df['birthdate'] = df['birthdate'].str.replace("Feb","02/")
#df['birthdate'] = df['birthdate'].str.replace("Mar","03/")
#df['birthdate'] = df['birthdate'].str.replace("Apr","04/")
#df['birthdate'] = df['birthdate'].str.replace("May","05/")
#df['birthdate'] = df['birthdate'].str.replace("Jun","06/")
#df['birthdate'] = df['birthdate'].str.replace("Jul","07/")
#df['birthdate'] = df['birthdate'].str.replace("Aug","08/")
#df['birthdate'] = df['birthdate'].str.replace("Sep","09/")
#df['birthdate'] = df['birthdate'].str.replace("Oct","10/")
#df['birthdate'] = df['birthdate'].str.replace("Nov","11/")
#df['birthdate'] = df['birthdate'].str.replace("Dec","12/")
#df['retirementDate'] = df['retirementDate'].str.replace("Jan","01/")
#df['retirementDate'] = df['retirementDate'].str.replace("Feb","02/")
#df['retirementDate'] = df['retirementDate'].str.replace("Mar","03/")
#df['retirementDate'] = df['retirementDate'].str.replace("Apr","04/")
#df['retirementDate'] = df['retirementDate'].str.replace("May","05/")
#df['retirementDate'] = df['retirementDate'].str.replace("Jun","06/")
#df['retirementDate'] = df['retirementDate'].str.replace("Jul","07/")
#df['retirementDate'] = df['retirementDate'].str.replace("Aug","08/")
#df['retirementDate'] = df['retirementDate'].str.replace("Sep","09/")
#df['retirementDate'] = df['retirementDate'].str.replace("Oct","10/")
#df['retirementDate'] = df['retirementDate'].str.replace("Nov","11/")
#df['retirementDate'] = df['retirementDate'].str.replace("Dec","12/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Jan","01/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Feb","02/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Mar","03/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Apr","04/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("May","05/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Jun","06/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Jul","07/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Aug","08/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Sep","09/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Oct","10/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Nov","11/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace("Dec","12/")
#df['birthdate'] = df['birthdate'].str.replace(" 1,","01/")
#df['birthdate'] = df['birthdate'].str.replace(" 2,","02/")
#df['birthdate'] = df['birthdate'].str.replace(" 3,","03/")
#df['birthdate'] = df['birthdate'].str.replace(" 4,","04/")
#df['birthdate'] = df['birthdate'].str.replace(" 5,","05/")
#df['birthdate'] = df['birthdate'].str.replace(" 6,","06/")
#df['birthdate'] = df['birthdate'].str.replace(" 7,","07/")
#df['birthdate'] = df['birthdate'].str.replace(" 8,","08/")
#df['birthdate'] = df['birthdate'].str.replace(" 9,","09/")
#df['retirementDate'] = df['retirementDate'].str.replace(" 1,","01/")
#df['retirementDate'] = df['retirementDate'].str.replace(" 2,","02/")
#df['retirementDate'] = df['retirementDate'].str.replace(" 3,","03/")
#df['retirementDate'] = df['retirementDate'].str.replace(" 4,","04/")
#df['retirementDate'] = df['retirementDate'].str.replace(" 5,","05/")
#df['retirementDate'] = df['retirementDate'].str.replace(" 6,","06/")
#df['retirementDate'] = df['retirementDate'].str.replace(" 7,","07/")
#df['retirementDate'] = df['retirementDate'].str.replace(" 8,","08/")
#df['retirementDate'] = df['retirementDate'].str.replace(" 9,","09/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(" 1,","01/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(" 2,","02/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(" 3,","03/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(" 4,","04/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(" 5,","05/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(" 6,","06/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(" 7,","07/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(" 8,","08/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(" 9,","09/")
#df['birthdate'] = df['birthdate'].str.replace(" \(.*\)","")
#df['birthdate'] = df['birthdate'].str.replace(" ","")
#df['birthdate'] = df['birthdate'].str.replace(",","/")
#df['retirementDate'] = df['retirementDate'].str.replace(" ","")
#df['retirementDate'] = df['retirementDate'].str.replace(",","/")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(" ","")
#df['lastTransferDate'] = df['lastTransferDate'].str.replace(",","/")

#df.head()

#df.shape

#df.info()

#df.to_csv("C:\\Users\\ahmet\\GitHub\\DataMiningProject\\AllDatasV20.csv", index=False)


