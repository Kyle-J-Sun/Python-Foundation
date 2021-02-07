#------------------------------Numpy-------------------------#
import numpy as np
n = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
]) #二维数组
print(n)
n[1:3,1:3]
print(n.shape)
print(n.size)

n2 = np.arange(4,10,2) #只能创建一维数组
print(n2)
n3 = np.ones((2,3,4))
print(n3)

n4 = np.arange(1,21).reshape(2,2,5)    #.reshape(2,2,-1)可以自动计算维度
print(n4)

#reshape: 修改数组形状后，生成新数组
#shape：可修改原数组 （shape是个属性不是函数！）

#flatten(): 数组降维

n6 = np.arange(1,21).reshape(2,2,-1)
print(n6)
n6[1:3,1:3]
# -----------------------------------------#
a = np.arange(24).reshape((2,3,4))
print(a)
a.mean()
a = a/a.mean()
print(a)
np.square(a)
np.sqrt(a)
np.ceil(a)
b = np.arange(24).reshape((2,3,4))
a>b
np.maximum(a,b)



#---------------------------------------------Pandas--------------------------------#
import pandas as pd
from pandas import DataFrame
#series:一维数组  Dataframe：二维数组
import numpy as np

d = pd.Series(range(20))
print(d)
d.cumsum()  #数值累加和


b = pd.Series([9,8,7,6],['a','b','c','d'])
print(b[b > b.median()])

a = pd.Series(['Kyle','Jack','May','Will','Jackson'], index=['Math', 'Physics', 'Econ', 'Statistics','Optimisation'], name="Result")
a.index.name = 'Subjects'
a.name = 'Names'
print(a)
#列别，标量，字典，数组，其他函数


#--------------------------Data-Frame-----------------#
dic1 = {'City': ['Beijing', "Shanghai", 'Guangzhou', 'Shenzhen', 'Shenyang'],
        'MoM': [101.5,101.2,101.3,102.0,100.1],
        'YoY': [120.7,127.3,120.0,145.5,101.6]
        }

df1 = DataFrame(dic1, index = ['c1','c2','c3','c4','c5'])
print(df1['MoM'])
#通过行索引访问
print(df1.loc['c2'])
print(df1['MoM']['c2'])

newc = df1.columns.insert(3,'New')
print(newc)
newdf1 = df1.reindex(columns = newc, fill_value=400)
print(newdf1)

df1 = df1.drop('MoM', axis=1)
print(df1)

#-----------------数据类型算数运算----------------------——#
b = pd.DataFrame(np.arange(20).reshape(4,5))
c = pd.Series(np.arange(4))
c -10
b-c



#----------------------------------------Matplotlib--------------------------------------#
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

plt.plot([3,1,4,5,2])
plt.ylabel('Grade')
#plt.savefig('test') #Save picture
plt.show()
