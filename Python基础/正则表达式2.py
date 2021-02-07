#练习

#(1) <a href = 'http://www.baidu.com'> 百度首页 </a>
#匹配 http://www.baidu.com
import re
pattern1 = '\w*://\w*.\w*.\w*'
string1 = "<a href = 'http://www.baidu.com'> 百度首页 </a>"
result1 = re.search(pattern1,string1)
print(result1)
#-----------------------------------------------------------
pattern1 = 'ht.*m'
string1 = "<a href = 'http://www.baidu.com'> 百度首页 </a>"
result1 = re.search(pattern1,string1)
print(result1)
#----------------------------------------------------------
pattern1 = '[a-zA-Z]+://[^s]*[.com|.cn]'
string1 = "<a href = 'http://www.baidu.com'> 百度首页 </a>"
result1 = re.search(pattern1,string1)
print(result1)

#(2) 匹配电话号码
#021-2221344583872381 匹配前8位
#0423-134324234134123 匹配前7位
pattern2 = '\d{3}-\d{8}|\d{4}-\d{7}|\d{4}-\d{7}'
string2 = '021-2221344583872381'
result2 = re.search(pattern2,string2)
print(result2)

#(3) 匹配电子邮箱
#shih998_SH@163.com
#SSS_II@qq.vip.com
pattern2 = '\S+@\w+(\.\w+){1,3}'
string2 = 'SSS_II@qq.vip.com'
result2 = re.search(pattern2,string2)
print(result2)
