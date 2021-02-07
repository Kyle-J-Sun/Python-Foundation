#需求：1.对51job数据分析是招聘数据最大薪资和最小薪资两列进行缺失值补全
#     2.对51job数据分析招聘数据最大薪资和最小薪资两列进行异常值处理

import matplotlib.pyplot as plt
import pandas as pd
import pymysql
#set connection
conn = pymysql.connect(host = 'localhost', user = 'root', passwd = 'Kyle9975', db = '51Job', charset = 'utf8')
sql = 'select salary_lowest, salary_highest from Data_Analyst inner join city on city.id_city = Data_Analyst.id_city'
#read_sql(Sql commends, DB Connection)
data = pd.read_sql(sql, conn)
print(data)
#print statistical description
print(data.describe())
x = 0
#将为0的数值替换成None
data.loc[(data['salary_lowest'] == 0), 'salary_lowest'] = None
data.loc[(data['salary_highest'] == 0), 'salary_highest'] = None
#最低和最高薪资缺失值插补
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            #将缺失值插补成中位数
            data.loc[j, i] = data.describe()['salary_lowest']['50%']
            data.loc[j, i] = data.describe()['salary_highest']['50%']
            x += 1 #计数
print(x)
print('After')
print(data.describe())

#异常值处理
#1.散点图（x:lowest, y:highest）
data2 = data.T #数组转置
print(data2)
salary_lowest = data2.values[0]
salary_highest = data2.values[1]
plt.plot(salary_lowest, salary_highest, 'o')
plt.xlabel('Lowest salary')
plt.ylabel('Highest salary')
plt.show()

line = len(data.values)
col = len(data.values[0])
#最低薪资异常 > 25000  最高薪资异常 > 50000
for i in range(0, line):
    for j in range(0, col):
        if(data.values[i][0] > 25000):
            data.values[i][j] = data.describe()['salary_lowest']['50%']
        if(data.values[i][1] > 50000):
            data.values[i][j] = data.describe()['salary_highest']['50%']

print("After")
print(data.describe())

da2 = data.values.T
salary_lowest2 = da2[0]
salary_highest2 = da2[1]
plt.plot(salary_lowest2, salary_highest2, 'o')
plt.xlabel('Lowest salary')
plt.ylabel('Highest salary')
#定义x轴和y轴的范围
plt.xlim(0,26000)
plt.ylim(0,51000)
plt.show()

