f = open('1.txt',encoding='utf-8')
text = f.read(3)
te = f.readline()
print(text)
print(te)
f.close()


p = open('2','w',encoding='utf-8')
p.write('Hellllllo')
p.close()

with open('1.txt',encoding='utf-8') as f:
    print(f.read())
    print(f.closed)
    print(f.mode)
    print(f.name)
print(f.closed)

p = open('2','w+',encoding='utf-8')
for i in range (100):
    p.write(str(i)+'\n')
p.seek(1)
# Offset: 偏移字节：正值往结束方向偏移，负值往开始方向偏移。
# Whence：从文中位置移动指针 whence(0-起始位置 1-当前位置 2-末尾位置)
print(p.tell()) #返回文中指针的具体位置
print(p.read())
p.close()