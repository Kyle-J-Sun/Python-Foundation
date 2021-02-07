from lxml import etree
html_doc='''
 <html>
        <head>
            <title>春晚</title>
        </head>
        <body>
            <h1 name="title">个人简介</h1>
            <div name="desc">
                <p name="name">姓名：<span>小岳岳</span></p>
                <p name="addr">住址：中国 河南</p>
                <p name="info">代表作：五环之歌</p>
            </div>
'''

#初始化
html = etree.HTML(html_doc)
print(type(html))

#查询所有div标签下的所有P标签
print(html.xpath('//div/p'))

#查询第二个p标签的name属性值
print(html.xpath('//p[3]/@name'))

#查询div标签下p标签下span标签内容
print(html.xpath('//div/p/span')[0].text) #text: 仅能获取当前标签文本数据

#查询body标签下h1标签的name属性值
print(html.xpath('//body/h1/@name'))

#查询所有包含name的属性值，并且name属性值为desc的标签
print(html.xpath('//*[@name = "desc"]'))

#查询第一个p标签内的所有文本数据
print(html.xpath('string(//p[1])')) #string:获取包括子标签在内的所有文本数据

