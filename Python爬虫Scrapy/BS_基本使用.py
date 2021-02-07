from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#创建一个bs对象，若默认会选择python中内置解析器
Soup = BeautifulSoup(html_doc,'lxml')
#格式化输出
# print(Soup.prettify())

#1.标签选择法
#（1）获取p标签
# print(Soup.p)

#（2）获取a标签href属性
# print(Soup.a['href'])

#（3）获取标签内容
# print(Soup.title.string)

#2.获取节点
#（1）获取子节点
# print(Soup.body.contents) #获取文本对象中所有子节点，以列表形式返回
# for i in Soup.body.children:  #获取列表迭代器 (使用for循环遍历)
#     print(i)

#（2）获得父节点
# print(Soup.b.parent)
# for i in Soup.b.parents:
#     print(i)

#3.搜索文档树
#（1）查询指定标签
# res1 = Soup.find_all('a')
# print(res1) #返回列表

#（2）正则表达式
#查询包含d字符的标签
# import re
# res2 = Soup.find_all(re.compile('e+')) #re.compile：申明一个正则表达式对象
# print(res2)

#（3）组合查询
#查询所有title标签或者a标签
# res3 = Soup.find_all(['title','a'])
# print(res3)

#（4）关键词参数
# #查询属性id = "link2" 的标签
# res4 = Soup.find_all(id = 'link2')
# print(res4)

#（5）内容匹配
# res5 = Soup.find_all(text= "Elsie")
# res5 = Soup.find_all(text = ['Elsie','Lacie'])
# print(res5)

#4.CSS选择器
#调用select()方法 传入相应的CSS选择器，返回列表
# （1）根据ID查询标签对象
# res6 = Soup.select('#link3')
# print(res6)

#（2）根据CLASS属性查询标签对象
# res7 = Soup.select('.sister')
# print(res7)

#（3）属性选择
# res8 = Soup.select('a[href = "http://example.com/elsie"]')
# print(res8)

#（4）包含选择器
# res9 = Soup.select('body p.title')
# print(res9)

#（5）获取标签内文本
# res10 = Soup.select('p a.sister')
# print(res10[0].get_text())
# print(res10[2].string)
