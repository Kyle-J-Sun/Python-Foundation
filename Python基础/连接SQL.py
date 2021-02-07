import pymysql

# 连接数据库
conn = pymysql.connect(host = 'localhost',user = 'root', passwd = 'Kyle9975', db = 'Kyle', charset = 'utf8')
# 创建游标
cursor = conn.cursor()
# sql = 'insert into Student(gid,GradeName) values ("1001","First Year")'
# 写SQL语句
sql = 'insert into Student(GradeName) values (%s)'
parm = ('Third year','Forth Year','Master','PHD')
# 执行
# cursor.execute(sql,parm)
cursor.executemany(sql,parm)
# 提交
conn.commit()
# 关闭
cursor.close()
conn.close()

# 更新
import pymysql
conn = pymysql.connect(host = 'localhost',user = 'root', passwd = 'Kyle9975', db = 'Kyle', charset = 'utf8')
cursor = conn.cursor()
sql = 'update Student set GradeName = %s where gid = %s'
# parm = ('Doctor','1001')
parm = (('Master','1002'),('First year','1003'))
# cursor.execute(sql,parm)
cursor.executemany(sql,parm)
conn.commit()
cursor.close()
conn.close()

# 删除
import pymysql
conn = pymysql.connect(host = 'localhost',user = 'root', passwd = 'Kyle9975', db = 'Kyle', charset = 'utf8')
cursor = conn.cursor()
sql = 'delete from Student where gid = %s'
parm = '1001'
cursor.execute(sql,parm)
conn.commit()
cursor.close()
conn.close()

#查询
import pymysql
conn = pymysql.connect(host = 'localhost',user = 'root', passwd = 'Kyle9975', db = 'Kyle', charset = 'utf8')
cursor = conn.cursor()
sql = 'select * from Student'
cursor.execute(sql)
print(cursor.fetchmany(2))
conn.commit()
cursor.close()
conn.close()

