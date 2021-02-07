import urllib.request
#Urlopen(): 向目标服务器发送一个请求
file = urllib.request.urlopen('http://www.ibeifeng.com') #Response
#获取到的是字节流型数据
# print(file.read())
#转码 decode() 字节流 ---> 普通字符串
result = file.read().decode('gbk')
print(result)