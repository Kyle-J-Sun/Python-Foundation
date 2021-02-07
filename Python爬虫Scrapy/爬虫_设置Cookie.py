#设置Cookies：跳过登录
import requests
File = open('Python爬虫Scrapy/Cookie.txt','r')
Cookie = {}
#处理cookie
# Split函数：切割读取，返回列表，遍历
for line in File.read().split(';'):
    #split将参数设置为1，把字符串切割成两部分
    name,value = line.split('=',1)
    #为空字典添加内容
    Cookie[name] = value
#带cookies发送请求
Req = requests.get('http://www.baidu.com',cookies = Cookie)
Data = Req.content
Web = open('baidu.html','wb')
Web.write(Data)
print(Data.decode('utf-8'))
Web.close()
File.close()
