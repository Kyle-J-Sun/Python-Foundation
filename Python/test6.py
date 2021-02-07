import pymysql
#连接数据库
#host:主机名 user:数据库用户名 passwd:数据库密码
#db :要操作的数据库名  charset:数据库的编码格式
conn=pymysql.connect(host='localhost',user='root',
                     passwd='123456',db='16班',charset='utf8'
                     )
#创建游标
cursor=conn.cursor()#(命令行，操作窗口，所有操作都是通过游标对象来完成的)
sql='insert into grade(gid,gradeName) values ("1001","大一")'
#写sql语句
sql='insert into grade(gid,gradeName) values (%s,%s)'#都是%s
parm=('1001','大一')
sql='insert into grade(gradeName) values (%s)'
parm=('大二')
#批量插入语句
sql='insert into grade(gradeName) values (%s)'
parm=('大三','大四')
#更新
sql='update grade set gradeName=%s where gid=%s'
parm=('研一','1001')
#多条更新
sql='update grade set gradeName=%s where gid=%s'
parm=(('研二','1002'),('研三','1003'))
#删除
sql='delete from grade where gid=%s'
parm='1001'
#执行sql语句
cursor.execute(sql,parm)
#执行多条sql语句
cursor.executemany(sql,parm)

#提交
conn.commit()
#查询
sql='select * from grade'
cursor.execute(sql)
print(cursor.fetchone())#一条
print(cursor.fetchall())#全部结果集
print(cursor.fetchmany(2))#指定条数
#关闭
cursor.close()
conn.close()
