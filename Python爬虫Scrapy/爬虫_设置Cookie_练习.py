import requests
import chardet
File = open('Python爬虫Scrapy/Cookie_Beifeng.txt','r')
Cookie = {}
for line in File.read().split(';'):
    name,value = line.split('=')
    Cookie[name] = value
Req = requests.get('http://tpcss.ibeifeng.com/course/course', cookies = Cookie)
Result = Req.content
Web = open('Python爬虫Scrapy/Beifeng.html','wb')
Web.write(Result)
Web.close()
File.close()