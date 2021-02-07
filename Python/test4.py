#将文本去掉空行和注释行放入新的文件中
f=open('1.txt','r',encoding='utf-8')
result=[]
for line in f.readlines():
    line=line.strip()#前后的空格删除
    if not len(line) or line[0]=='#':
        continue
    else:
        result.append(line)
w_word='\n'.join(result)
# print(w_word)
k=open('2.txt','w',encoding='utf-8')
k.write(w_word)
k.close()
f.close()
s=['我','爱','中国']
res=''.join(s)
print(res)
