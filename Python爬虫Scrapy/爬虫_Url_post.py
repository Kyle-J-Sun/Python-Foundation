import urllib.request
import urllib.parse

#构建需要提交给表单的data，然后解析转码再发送
#encode():把字符串转换成相应数据格式的字节流数据
data =urllib.parse.urlencode({
    'name':'Kyle',
    'pass':'abc1111'
}).encode('utf-8')
#2.带data发送请求
response = urllib.request.urlopen('http://www.iqianyue.com/mypost/',data)
result = response.read() #字节流
fl = open('1.html','wb')
fl.write(result)
print(result.decode('utf-8'))
fl.close()
