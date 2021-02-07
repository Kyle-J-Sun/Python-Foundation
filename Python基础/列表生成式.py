import csv
with open(r'/Users/kyle/Downloads/aaa.csv','r',encoding='GBK') as filescv:
    readCSV = csv.reader(filescv, delimiter =',')
    for row in readCSV:
        print(row)

#列表生成式
#[exp for iter_var in interable [if condition]]

import csv
with open(r'/Users/kyle/Downloads/aaa.csv','r',encoding='GBK') as filescv2:
    reader = csv.reader(filescv2)
    rows = [row for row in reader]
    print(rows)
    # column = [row[1] for row in reader]
    # print(column)

# 迭代Iterable中的每个元素
# 每次迭代都先把结果赋值给iter_var，然后通过exp得到一个新的计算值。
# 最后把所有通过exp得到的计算值以一个新列别的形式返回
# L=[]
# for iter_var in iterable:
#         L.append(exp)
#生成一个3到10的数字列表

list1 = list(range(3,11))
print(list1)
list2 = [x for x in range(3,11)]
print(list2)

#带过滤功能的语法格式
#[exp for iter_var in interable if_exp]
# L=[]
# for iter_var in iterable:
#   if_exp:
#         L.append(exp)
#生成一个2n+1的数字列表，n为3到11

list3 = []
for i in range(3,12):
    list3.append(2*i+1)
print(list3)

list4 = [2*n+1 for n in range(3,12)]
print(list4)

#过滤出指定列表中数值大于50的元素

exm = [23,45,50,51,56,53,45,58,33,21,89]
list5 = []
for i in exm:
    if i > 50:
        list5.append(i)
print(list5)

list6 = [i for i in exm if i > 50]
print(list6)

#计算两个集合的全排列

exm1 = ["红","蓝"]
exm2 = ['1','2','3']
list7 = [(x,y) for x in exm1 for y in exm2]
print(list7)

#列表生成式写出来的功能都可以通过for循环实现

list8 = []
for x in exm1:
    for y in exm2:
        list8.append((x,y))
print(list8)





