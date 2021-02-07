import pandas as pd
import numpy as np
import time
import datetime

# ---------------------------------How to transform tick data into one-minute k-bar-------------------------------------

df = pd.read_csv('/Users/kyle/Documents/量化投资/[20180323]量化投资_程序化概述及1分钟k线合成/data.csv', encoding='utf-8')
# Importing the data
df.drop(df.columns[0], axis=1, inplace=True)
# Dropping the original tick data

MM = int(60) #

timeD = df['time'].str.split(' ').str[0]
# Converting into string format
timeT = df['time'].str.split(' ').str[-1]
# Converting into string format
print(timeD)

timeDD = timeD.str.split('-')
timeTT = timeT.str.split(':')
print(timeDD)
print(timeTT)
time_y = pd.DataFrame(timeDD.str[0], dtype='int') * 10000
time_m = pd.DataFrame(timeDD.str[1], dtype='int') * 100
time_d = pd.DataFrame(timeDD.str[2], dtype='int')
dateN = time_y + time_m + time_d
print(dateN)

time_h = pd.DataFrame(timeTT.str[0], dtype='int') * 100
time_min = pd.DataFrame(timeTT.str[1],dtype='int')
dateM = time_h+time_min
print(dateM)

# Based on the future, replace time
dateM.replace(859, 900, inplace = True) #move data at 8:59 to 9:00
dateM.replace(1130, 1129, inplace = True)
dateM.replace(1329, 1330, inplace = True)
dateM.replace(1500, 1459, inplace = True)
dateM.replace(2059, 2100, inplace = True)
dateM.replace(100, 59, inplace = True)

# Based on the Stock, replace time
#dateM.replace(925, 930, inplace = True) #move data at 8:59 to 9:00
#dateM.replace(926, 930, inplace = True)
#dateM.replace(929, 930, inplace = True)
#dateM.replace(1130, 1129, inplace = True)
#dateM.replace(1259, 1300, inplace = True)
#dateM.replace(1500, 1459, inplace = True)

# De-duplication
u1 = dateM.drop_duplicates()
datetimeN = dateN + dateM/10000
u2 = datetimeN.drop_duplicates()
df2 = pd.DataFrame(columns=['time','open','high','low','close','vol'], index=np.arange(len(u2)))

start = time.time()
# Recording the proccessing time
for i in range(len(u2)):
    df_ind_all = (datetimeN == u2.iloc[i]).replace(False, np.nan).dropna().index.tolist()
    # Judge whether equal, if not, replace false data into nan data ,and drop the nan data, then add the index into the list
    ind1 = df_ind_all[0] # get the first row within the first hour
    ind2 = df_ind_all[-1] # get the last row within the first hour
    if dateM.loc[ind1, 'time'] == int(930) or (dateM.loc[ind1, 'time'] == 1300):
        df2.loc[i,'time'] = df['time'][ind2]
        #If the time = 9:30 or 13:00, then we can let the last data as opening time
    else:
        df2.loc[i, 'time'] = df['time'][ind1]
        df2.loc[i, 'open'] = df.iloc[ind1, 1]
        df2.loc[i, 'high'] = max(df.iloc[ind1:ind2, 1])
        df2.loc[i, 'low'] = min(df.iloc[ind1:ind2, 1])
        df2.loc[i, 'close'] = df.iloc[ind2, 1]
    if dateM.loc[ind1, 'time'] == int(930):
        df2.loc[i,'vol'] = df.iloc[ind2, 2]
    else:
        df2.loc[i,'vol'] = df.iloc[ind2, 2] - df.iloc[ind1, 2]
end = time.time()
print(df2.head(5))
print(end-start)
df2.to_csv('/Users/kyle/Documents/量化投资/[20180323]量化投资_程序化概述及1分钟k线合成/data2.csv')
