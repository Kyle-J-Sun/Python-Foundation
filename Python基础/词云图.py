from wordcloud import WordCloud, ImageColorGenerator #词云模块
import matplotlib.pyplot as plt
from scipy.misc import imread
import pymysql

#处理中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置默认字体
plt.rcParams['axes.unicode_minus'] = False #解决保存图像时显示方块的问题

conn = pymysql.connect(host = 'localhost', user = 'root', passwd = 'Kyle9975', db = 'Kyle', charset = 'utf8')
cursor = conn.cursor()
sql = 'select Cast from Maoyan_Movie'
cursor.execute(sql)
cast_list = cursor.fetchall()
print(cast_list)

#数据分裂
cast_name_list = [item[0] for item in cast_list]
#切割列表，保存为字符串
cast_text = ' '.join(cast_name_list)
print(cast_text)

#设置背景图
colour = imread("Python基础/girl.png")

#定义字体
font = '/Users/kyle/PycharmProjects/py.lesson/venv/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf'

#WordCloud实例化词云
#Generate 输入词云文本
my_wordcloud = WordCloud(font_path=font, max_font_size=300, background_color='white', mask=colour).generate(cast_text)
#从背景颜色生成颜色值
image_colours = ImageColorGenerator(colour)

#显示词云图
plt.imshow(my_wordcloud.recolor(color_func=image_colours))

#不显示坐标轴
plt.axis('off')
plt.show()

