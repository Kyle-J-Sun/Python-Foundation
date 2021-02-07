import urllib.request
import ssl
context = ssl._create_unverified_context()
response = urllib.request.urlopen('http://www.taobao.com', context = context, timeout = 5)
print(response.read().decode('utf-8'))