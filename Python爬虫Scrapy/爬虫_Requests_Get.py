import requests
re = requests.get('http://www.baidu.com')
#设置网页编码
re.encoding = 'utf-8'
#打印文本字符串数据
print(re.text)
#打印字节流数据
print(re.content.decode('utf-8').encode('utf-8'))