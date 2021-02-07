import requests
#人工转码
Req = requests.get('http://www.ibeifeng.com/')
#Decode转码
print(Req.content.decode('gbk')) #    字节流 ---> 字符串
#Encode转码
print(Req.text.encode('gbk'))#    字符串 ----> 字节流

#Encoding 编码属性，设置text编码格式
import requests
Req2 = requests.get('http://www.baidu.com')
Req2.encoding = 'utf-8'
print(Req2.text)

#自动处理乱码
import chardet     #字符串、文件编码检测模块
import requests
Req3 = requests.get('http://www.baidu.com')
#自动获取网页编码格式
print(chardet.detect(Req3.content))
#自动获取网页编码，赋值给相应内容的encoding属性
Req3.encoding = chardet.detect(Req3.content)['encoding']
print(Req3.text)

#状态码  正常：200
print(Req3.status_code)