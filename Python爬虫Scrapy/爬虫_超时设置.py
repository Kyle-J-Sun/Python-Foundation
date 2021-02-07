import requests
try:
    Req = requests.get('http://book.dangdang.com/', timeout = 1)
    print(Req.status_code)
except Exception as Error:
    print(Error)

