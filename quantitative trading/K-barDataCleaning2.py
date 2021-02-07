# ---------------------------------How to transform tick data into multiple minutes k-bars------------------------------------

from __future__ import division #Write from the start
import pandas as pd
import numpy as np
import time
import sys

df = pd.read_csv('/Users/kyle/Documents/量化投资/[20180327]量化投资_分钟k线合成及基本面案例分析/dataOneMinute.csv', encoding = 'utf-8')
df.drop(df.columns[0], axis = 1, inplace = True)
DelStrIndex = (df['time'] == '2018-03-15 14:59:00').replace(False, np.nan).dropna().index.tolist()
print(DelStrIndex)
# Find the last trading time
df.drop(df.index[DelStrIndex[0]:], inplace = True) #2018-03-15 14:07:24
# Drop the data after the last trading time
MM = 3 # Set an integer
print(df.head(5)) #print the first five rows of data from df

timeD = df['time'].str.split(' ').str[0] #2018-03-15
timeT = df['time'].str.split(' ').str[-1] #14:07:24
timeDD = timeD.str.split('-') # 3 lists
timeTT = timeT.str.split(':') # 3 lists

time_y = pd.DataFrame(timeDD.str[0], dtype='int')
time_m = pd.DataFrame(timeDD.str[1], dtype='int')
time_d = pd.DataFrame(timeDD.str[2], dtype='int')

time_h = pd.DataFrame(timeTT.str[0], dtype='int')
time_min = pd.DataFrame(timeTT.str[1], dtype='int')
timeHM = time_h * 100 + time_min
print(timeHM)


#Distingush the time needed to be combined
if MM == 60:
    timeHM1 = pd.DataFrame((930 <= np.array(timeHM)) & (np.array(timeHM) < 1030), columns=['time'])
    timeHM1.time.replace(True, 1, inplace = True) # set value of 1 if the data is at the range between 930 and 1030
    timeHM1.time.replace(False, np.nan, inplace = True) # set 0 if the data is not at the range
    timeHM1.dropna(axis = 0, how = 'any', inplace = True) # Drop 0s based on 0(vertical) direction.  any means drop the entire row if one of them is False

    timeHM2 = pd.DataFrame((1030 <= np.array(timeHM)) & (np.array(timeHM) < 1130), columns=['time'])
    timeHM2.time.replace(True, 2, inplace=True)
    timeHM2.time.replace(False, np.nan, inplace=True)
    timeHM2.dropna(axis=0, how='any', inplace=True)

    timeHM3 = pd.DataFrame((1330 <= np.array(timeHM)) & (np.array(timeHM) < 1430), columns=['time'])
    timeHM3.time.replace(True, 3, inplace=True)
    timeHM3.time.replace(False, np.nan, inplace=True)
    timeHM3.dropna(axis=0, how='any', inplace=True)

    timeHM4 = pd.DataFrame((1430 <= np.array(timeHM)) & (np.array(timeHM) < 1500), columns=['time'])
    timeHM4.time.replace(True, 4, inplace=True)
    timeHM4.time.replace(False, np.nan, inplace=True)
    timeHM4.dropna(axis=0, how='any', inplace=True)
    timeHM_end = timeHM1.append([timeHM2, timeHM3, timeHM4])
elif MM == 3 or MM == 5 or MM == 10 or MM == 15 or MM == 30:
    time_min = time_min//MM
    timeHM_end = time_h * 100 + time_min
else:
    print('Please type a correct MM value')
    sys.exit(0)

#Date and time output
datetimeN = (time_y * 10000 + time_m * 100 + time_d) + (timeHM_end/10000) #20180315.0001 20180315.0002.....
u = datetimeN.drop_duplicates()
dataMN = pd.DataFrame(columns = ['time', 'open', 'high','low', 'close', 'vol'], index = np.arange(len(u)))
start = time.time()
for i in range(len(u)):
    df_ind_all = (datetimeN == u.iloc[i]).replace(False, np.nan).dropna().index.tolist()
    ind1 = df_ind_all[0]
    ind2 = df_ind_all[-1]
    dataMN.loc[i, 'time'] = df['time'][ind1] #
    dataMN.loc[i, 'open'] = df.iloc[ind1, 1]
    dataMN.loc[i, 'high'] = max(df.iloc[ind1:ind2, 2])
    dataMN.loc[i, 'low'] = min(df.iloc[ind1:ind2, 3])
    dataMN.loc[i, 'close'] = df.iloc[ind2, 4]
    dataMN.loc[i, 'vol'] = sum(df.iloc[ind1:ind2, 5])
end = time.time()
print(dataMN.head(60))
print(end-start)
dataMN.to_csv('/Users/kyle/Documents/量化投资/[20180323]量化投资_程序化概述及1分钟k线合成/data_hour.csv')
