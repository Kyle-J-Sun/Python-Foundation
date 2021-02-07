#打开文件
f=open('1.txt',encoding='utf-8')

# cous=f.read()#默认读取全部内容
# # cous=f.read(3)#读取前三个字符
# ss=f.readline()#每次读取一行内容，包括行尾的换行符
cous=f.readlines()#以列表的形式读取
# print(ss)
print(cous)
f.close()
f=open('2','w',encoding='utf-8')
f.write('Hello World')
f.write('\nHello World2')
f.close()
with open('2',encoding='utf-8') as f:
    print(f.read())
    print(f.closed)#判断文件是否关闭
print(f.closed)
f=open(r"C:\Users\ibf\Desktop\aaa.txt",'a+',encoding='utf-8')
for i in range(100):
    f.write(str(i)+'\n')
f.seek(1)#seek(offset,whence) offset--偏移offset个字节，
# 正值是往结束方向偏移，负值往起始方向偏移
#whence 从文中位置移动指针 whence（0-起始，1-当前，2-末尾）
print(f.tell())#返回文中指针的具体位置
print(f.read())
f.close()