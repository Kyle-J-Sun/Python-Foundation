'''----------------------------------------------------Title------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------'''
import requests
import pymysql
import re
content = '''
 <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/4883" title="钢琴家" class="image-link" data-act="boarditem-click" data-val="{movieId:4883}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/bcbe59fc51580317adf94537a61a1a26142090.jpg@160w_220h_1e_1c" alt="钢琴家" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/4883" title="钢琴家" data-act="boarditem-click" data-val="{movieId:4883}">钢琴家</a></p>
        <p class="star">
                主演：艾德里安·布洛迪,艾米莉娅·福克斯,米哈乌·热布罗夫斯基
        </p>
<p class="releasetime">上映时间：2002-05-24(法国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-3">3</i>
    <a href="/films/3294" title="勇敢的心" class="image-link" data-act="boarditem-click" data-val="{movieId:3294}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/5e2aaddb1c0c9ea4c36dc465245cc5ab290967.jpg@160w_220h_1e_1c" alt="勇敢的心" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/3294" title="勇敢的心" data-act="boarditem-click" data-val="{movieId:3294}">勇敢的心</a></p>
        <p class="star">
                主演：梅尔·吉布森,苏菲·玛索,帕特里克·麦高汉
        </p>
<p class="releasetime">上映时间：1995-05-18(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-4">4</i>
    <a href="/films/11237" title="阿飞正传" class="image-link" data-act="boarditem-click" data-val="{movieId:11237}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/85215b28d568ea8e2c97766edd95f890210522.jpg@160w_220h_1e_1c" alt="阿飞正传" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/11237" title="阿飞正传" data-act="boarditem-click" data-val="{movieId:11237}">阿飞正传</a></p>
        <p class="star">
                主演：张国荣,张曼玉,刘德华
        </p>
<p class="releasetime">上映时间：2018-06-25</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-5">5</i>
    <a href="/films/13824" title="射雕英雄传之东成西就" class="image-link" data-act="boarditem-click" data-val="{movieId:13824}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/86c5190ba1d1236093c13f2fe9ed8dd4150050.jpg@160w_220h_1e_1c" alt="射雕英雄传之东成西就" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/13824" title="射雕英雄传之东成西就" data-act="boarditem-click" data-val="{movieId:13824}">射雕英雄传之东成西就</a></p>
        <p class="star">
                主演：张国荣,梁朝伟,张学友
        </p>
<p class="releasetime">上映时间：1993-02-05(中国香港)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-6">6</i>
    <a href="/films/6796" title="爱·回家" class="image-link" data-act="boarditem-click" data-val="{movieId:6796}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/de1142a5dceb901eb939eb0bcfc2f88470909.jpg@160w_220h_1e_1c" alt="爱·回家" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/6796" title="爱·回家" data-act="boarditem-click" data-val="{movieId:6796}">爱·回家</a></p>
        <p class="star">
                主演：俞承豪,金艺芬,童孝熙
        </p>
<p class="releasetime">上映时间：2002-04-05(韩国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-7">7</i>
    <a href="/films/263" title="初恋这件小事" class="image-link" data-act="boarditem-click" data-val="{movieId:263}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/4be3dda6873054115658bddd133708ce89845.jpg@160w_220h_1e_1c" alt="初恋这件小事" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/263" title="初恋这件小事" data-act="boarditem-click" data-val="{movieId:263}">初恋这件小事</a></p>
        <p class="star">
                主演：马里奥·毛瑞尔,平采娜·乐维瑟派布恩,阿查拉那·阿瑞亚卫考
        </p>
<p class="releasetime">上映时间：2012-06-05</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-8">8</i>
    <a href="/films/267" title="泰坦尼克号" class="image-link" data-act="boarditem-click" data-val="{movieId:267}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/b607fba7513e7f15eab170aac1e1400d878112.jpg@160w_220h_1e_1c" alt="泰坦尼克号" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/267" title="泰坦尼克号" data-act="boarditem-click" data-val="{movieId:267}">泰坦尼克号</a></p>
        <p class="star">
                主演：莱昂纳多·迪卡普里奥,凯特·温丝莱特,比利·赞恩
        </p>
<p class="releasetime">上映时间：1998-04-03</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-9">9</i>
    <a href="/films/1346" title="迁徙的鸟" class="image-link" data-act="boarditem-click" data-val="{movieId:1346}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/a1634f4e49c8517ae0a3e4adcac6b0dc43994.jpg@160w_220h_1e_1c" alt="迁徙的鸟" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1346" title="迁徙的鸟" data-act="boarditem-click" data-val="{movieId:1346}">迁徙的鸟</a></p>
        <p class="star">
                主演：雅克·贝汉,Philippe Labro
        </p>
<p class="releasetime">上映时间：2001-12-12(法国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/790" title="蝙蝠侠：黑暗骑士" class="image-link" data-act="boarditem-click" data-val="{movieId:790}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/09658109acfea0e248a63932337d8e6a4268980.jpg@160w_220h_1e_1c" alt="蝙蝠侠：黑暗骑士" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/790" title="蝙蝠侠：黑暗骑士" data-act="boarditem-click" data-val="{movieId:790}">蝙蝠侠：黑暗骑士</a></p>
        <p class="star">
                主演：克里斯蒂安·贝尔,希斯·莱杰,阿伦·伊克哈特
        </p>
<p class="releasetime">上映时间：2008-07-14(阿根廷)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-11">11</i>
    <a href="/films/247791" title="恐怖直播" class="image-link" data-act="boarditem-click" data-val="{movieId:247791}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/1da0af2570fe697d38c4a37fdfded19b254936.jpg@160w_220h_1e_1c" alt="恐怖直播" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/247791" title="恐怖直播" data-act="boarditem-click" data-val="{movieId:247791}">恐怖直播</a></p>
        <p class="star">
                主演：河正宇,李璟荣,李大卫
        </p>
<p class="releasetime">上映时间：2013-07-31(韩国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
'''



# headers = {
#     'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# }
# url = 'https://maoyan.com/board/4?offset=1'
# response = requests.get(url, headers=headers)
# print(response.text)

pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>' +
                     '.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?' +
                     'integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)  # re.S：让.匹配到换行符
items = re.findall(pattern, content)
print(items)