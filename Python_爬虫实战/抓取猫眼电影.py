#(1)明确需求
#网站：https://maoyan.com/board/4
#字段：排名，图片，名称，主演，上映时间，评分
#数据库：存储到Mysql
#模块：requests,pymysql,re

#(2)分析HTML结构

#(3)编写代码

import requests
import pymysql
import re

#1. 请求单页内容
def get_one_page(url):
    #构建headers
    headers = {
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text

'''----------------------------------------------------Title------------------------------------------------------------
<dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/2049" title="十二怒汉" class="image-link" data-act="boarditem-click" data-val="{movieId:2049}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default">
      <img alt="十二怒汉" class="board-img" src="https://p0.meituan.net/movie/df15efd261060d3094a73ef679888d4f238149.jpg@160w_220h_1e_1c">
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/2049" title="十二怒汉" data-act="boarditem-click" data-val="{movieId:2049}">十二怒汉</a></p>
        <p class="star">
                主演：亨利·方达,李·科布,马丁·鲍尔萨姆
        </p>
<p class="releasetime">上映时间：1957-04-13(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
---------------------------------------------------------------------------------------------------------------------'''


#2. 解析单页HTML
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>'+
                         '.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?'+
                         'integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S) #re.S：让.匹配到换行符
    items = re.findall(pattern,html)
    print(items)

# #3. 处理单页数据
#     for item in items:
#         yield {
#             'Index':item[0],
#             'Image':item[1],
#             'Title':item[2],
#             'Cast':item[3].strip()[3:],  #strip(): 去掉空格和换行符
#             'Release_time':item[4].strip()[5:15],
#             'Score':item[5]+item[6]
#         }
#
# #4. 保存
# def save_into_mySQL(content):
#     # 连接数据库
#     conn = pymysql.connect(host = 'localhost',user = 'root', passwd = 'Kyle9975', db = 'Kyle', charset = 'utf8')
#     # 创建游标
#     cursor = conn.cursor()
#     Index = content['Index']
#     Image = content['Image']
#     Title = content['Title']
#     Cast = content['Cast']
#     Release_time = content['Release_time']
#     Score = content['Score']
#     # 写SQL语句
#     sql = 'insert into Maoyan_Movie values (%s,%s,%s,%s,%s,%s)'
#     parm = (Index,Image,Title,Cast,Release_time,Score)
#     # 执行
#     cursor.execute(sql,parm)
#     # 提交
#     conn.commit()
#     # 关闭
#     cursor.close()
#     conn.close()

#5. 函数回调
#定义一个主函数，从而提高运行效率。
def main(num):
    #重构URL
    url = 'https://maoyan.com/board/4?offset='+str(num)
    html = get_one_page(url)
    for i in parse_one_page(html):
        print(i)
        # save_into_mySQL(i)

#6. 进行分页处理
#调用主函数
if __name__ == '__main__':
    for i in range(10):
        main(i*10)

