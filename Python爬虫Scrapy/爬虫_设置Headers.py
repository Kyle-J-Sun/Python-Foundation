#设置Headers：应对反爬虫
#http://www.dianping.com/
import requests
#构建Headers
Headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
#User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
#带Headers请求网页
Req = requests.get('http://www.dianping.com/', headers = Headers)
print(Req.text)
