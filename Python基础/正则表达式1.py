import re
# (1) 普通字符作为原子
pattern = 'shu'
string = 'http://xiaohongshu.com'
result = re.search(pattern,string)
print(result)
# (2) 非打印字符作为原子
# 一些字符串中用于格式控制的符号，比如换行符
pattern = '\n'
string = '''http://xiaohongshu.com
http://xiaohongshu.com'''
result = re.search(pattern,string)
print(result)
# (3) 通用字符作为原子(匹配 32python_ )
pattern = '\w\dpython\w'
pattern = '\d\dpython\w'
pattern = '\d{2}python\w'
pattern = '\d?python\w'
string = 'abcdfsdalfjksld12432python_PWDJN'
result = re.search(pattern,string)
print(result)
# (4) 原子表（字符集）
import re
# pattern = '\d\dpython[_zxy]'
pattern = '\d\dpython[^zxy]'
string = 'abcdfsdalfjksld12432python_PWDJN'
result = re.search(pattern,string)
print(result)
# (5) 元字符
pattern = '..python.*'
string = 'abcdfsdalfjksld12432python_PWDJN'
result = re.search(pattern,string)
print(result)
# (6) 边界限定符
pattern = 'py$'
string = 'abcdfsdalfjksld12432python_PWDJNpy'
result = re.search(pattern,string)
print(result)
# (7) 次数限定符
# pattern = 'py.*' #贪婪模式：尽可能匹配多的次数
# pattern = 'abc{2}' #= pattern = 'abcc'
# pattern = 'abc{1,3}'
pattern = 'py.?y'
string = 'abcdfsdalfjksld12432python_pynyPWDJNpy'
result = re.search(pattern,string)
print(result)
# (8) 模式选择符
# pattern = 'python|fjks'
pattern = '(abc){2}'
string = 'abcabcdfsdalfjksld12432python_pynyPWDJNpy'
result = re.findall(pattern,string) #findall: 以列表形式返回
result = re.search(pattern,string)
print(result)