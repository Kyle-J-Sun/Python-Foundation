# Add list elements
lst1 = ['kyle', 'sherry', 'cathy', 18, [41, 59]];
print(
    lst1,
    lst1.append('Oliva'),
    lst1,
    lst1.extend(['Wang', 'Sun', 'Li']),
    lst1,
    lst1.insert(2,'Students'),
    lst1,
    lst1.index([41,59])
)
del lst1[3],
del lst1[4];
print(lst1);
print(lst1.pop());
print(lst1)
print(lst1)
print(
    lst1.pop(1),
lst1
)
print(
    lst1.remove('Students'),
    lst1,
    lst1.reverse(),
    lst1
)
num = [5,3,4,5,7,8,9]
print(
    num.sort(),
    num,
    num + lst1,
    num * 3,
    num.clear(),
    num
)
num = [4,4,22,5,67,6,778,65]
print(
    max(num),
    min(num),
    num[2:],
    num[-1],
    num[-3:-1]
)


#python大圣课
x = range(-10,10)
print(sorted(x, key = abs))

#列表解析
#根据一个列表生成一个新的列表
#列表解析比for循环好

result = []
for i in x:
    if i < 0:
        result.append(i**2)
    else :
        result.append(i)
print(result)

#使用列表解析写以上同样功能
result2 = [i**2 for i in x if i <0]
result3 = [i**2 if i < 0 else i for i in x]
print(result2)
print(result3)