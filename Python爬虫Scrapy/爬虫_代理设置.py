import requests
proxies = {
    'HTTP':'125.115.181.4:3128'
}
Req = requests.get('http://www.taobao.com', proxies = proxies)
print(Req.status_code)