#将文本去掉空行和注释行放入新的文件中
File = open('1.txt','r',encoding='UTF-8')
Result = []
for line in File.readlines():
    line = line.strip() #删除前后空格
    if not len(line) or line[0] == '#':
        continue
    else:
        Result.append(line)
Cut_List = '\n'.join(Result) #切割列表
print(Cut_List)
Result_File = open('3.txt','w',encoding='UTF-8')
Result_File.write(Cut_List)
Result_File.close()
File.close()

#Join函数的使用
exm = ['For','Exam','ple','Yeah']
Cut_List1 = '-'.join(exm)
print(Cut_List1)

#模块倒入
import random,csv,os
ran = random.randint()
#模块方法的倒入
from random import randint
ran2 = randint()

p = ['Hello', 'Kyle', 'Here']
print("-".join(p))

#字符串
#str 和 unicode (python3以后只有unicode)




