import re
#(1) 普通字符作为原子
# pattern='shu'
# string='http://xiaohongshu.com'
# result=re.search(pattern,string)
# print(result)
#(2) 非打印字符作为原子
#一些字符串中用于格式控制的符号，比如换行符
# pattern='\n'
# string='''http://xiaohongshu.com
# http://xiaohongshu.com'''
# result=re.search(pattern,string)
# print(result)
#(3):通用字符作为原子
# pattern='\d?python\w'
# string='abcdefghigk123python_py'
# result=re.search(pattern,string)
# print(result)
#(4):原子表（字符集）
# pattern='\d\dpython[_zxy]'
# pattern='\d\dpython[^zxy]'
# string='abcdefghigk123python_py'
# result=re.search(pattern,string)
# print(result)
#(5)元字符
# pattern='python.*'
# string='abcdefghigk123python_py'
# result=re.search(pattern,string)
# print(result)
#边界限定符
# pattern='^abc'
# pattern='py$'
# string='abcdefghigk123python_py'
# result=re.search(pattern,string)
# print(result)
#次数限定符
# pattern='py.*'#贪婪模式 ：尽可能的匹配多的次数
# pattern='abc{1,3}'
# pattern='py.*?y'#非贪婪模式：尽可能的匹配少的次数
# string='abcccdefghigk123python_pyxyzabc'
# result=re.search(pattern,string)
# print(result)
#模式选择符
# pattern='python|higk'
# string='abcccdefghigk123python_pyxyzabc'
# result=re.findall(pattern,string)
# print(result)
# pattern='(abc){2}'
# string='abcabcdefghigk123python_pyxyzabc'
# result=re.search(pattern,string)
# print(result)
#练习
#<a href='http://www.baidu.com'> 百度首页 </a>
#匹配到http://www.baidu.com
# pattern='ht.*m'
# pattern='[a-zA-Z]+://[^s]*[.com|.cn]'
# string="<a href='http://www.baidu.com'> 百度首页 </a>'"
# result=re.search(pattern,string)
# print(result)
#匹配电话号码
#021-6789456710000 匹配八位
#0423-12345678923  匹配七位
# pattern='\d{3}-\d{8}|\d{4}-\d{7}'
# string="0423-12345678923"
# result=re.search(pattern,string)
# print(result)
#匹配电子邮箱
#shih998_SH@163.com
#SSS_II@qq.vip.com
pattern='\w+@\w+(\.\w{2,5}){1,2}'
string="SSS_II@qq.vip.com"
result=re.search(pattern,string)
print(result)
