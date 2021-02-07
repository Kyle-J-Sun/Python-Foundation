import requests

#构建data
Login_Account = {
    'name':'Kyle',
    'pass':'Kyle9975'
}

#带data发送request
Sign_in = requests.post('http://www.iqianyue.com/mypost',data = Login_Account)
Result = Sign_in.content
Web = open('Reg.html','wb')
Web.write(Result)
print(Result.decode('utf-8'))
Web.close()