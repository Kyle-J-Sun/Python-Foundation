import  csv
import csv
with open(r"C:\Users\ibf\Desktop\aaa.csv") as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        print(row)
    for row in readCSV:
        print(row[0],row[1])
# 使用reader函数，接收一个可迭代的对象（比如csv文件），能返回一个生成器，就可以从其中解析出csv的内容：
# 比如下面的代码可以读取csv的全部内容，以行为单位：
with open(r"C:\Users\ibf\Desktop\aaa.csv", "r", encoding = "gbk") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
print(rows)
#读取第二列的内容
with open(r"C:\Users\ibf\Desktop\aaa.csv", "r", encoding = "gbk") as f:
    reader = csv.reader(f)
    column = [row[1] for row in reader]

print(column)
with open(r'C:\Users\ibf\Desktop\aaa.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    Salesorder = []
    clienttype = []
    manufacturer = []
    for row in readCSV:
        order = row[0]
        type = row[1]
        producer = row[2]

        Salesorder.append(order)
        clienttype.append(type)
        manufacturer.append(producer)

    print(Salesorder)
    print(clienttype)
    print(manufacturer)

with open(r"C:\Users\ibf\Desktop\aaa.csv", "a", newline="") as datacsv:
    # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
    csvwriter.writerow(["A", "B", "C", "D"])
# DictReader，和reader函数类似，接收一个可迭代的对象，能返回一个生成器，
# 但是返回的每一个单元格都放在一个字典的值内，而这个字典的键则是这个单元格的标题（即列头）。
with open(r"C:\Users\ibf\Desktop\aaa.csv", "r",encoding = "gbk") as f:
    reader = csv.DictReader(f)
    column = [row for row in reader]
    # column = [row['A'] for row in reader]
    print(column)
with open(r"C:\Users\ibf\Desktop\aaa.csv", "r", encoding = "gbk") as f:
    reader = csv.reader(f)
    rows = [row[0] for row in reader]#列表生成式：用来生成列表的特定语法形式
print(rows)
l=[]
for row in reader:
    l.append(row)
# 生成一个从3到10的数字列表
list1=list(range(3,11))
list2=[x for x in range(3,11)]
print(list1)
print(list2)
# 生成一个2n+1的数字列表，n--3--11
l2=[]
for n in range(3,12):
    l2.append(2*n+1)
l3=[2*n+1 for n in range(3,12)]
print(l2)
print(l3)
#[exp for iter_var in iterable]
#迭代iterable每一个元素 ，每次迭代都会把结果先赋值给iter_var，然后通过
#exp得到一个新的计算值
#[exp for iter_var in iterable if_exp]
l=[12,14,15,16,17,23,24,25]
l4=[x for x in l if x>20]
print(l4)
l=['15','16','17']
l1=['18','19']
list=[(x,y) for x in l for y in l1]
print(list)
