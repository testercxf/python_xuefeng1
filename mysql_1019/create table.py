import  pymysql
from mysql_1019.info  import *

#连接数据库   localhost本地数据库
conn =pymysql.connect(host="localhost",user=user,password=password,port=port)
result = conn.cursor()                            #创建一个游标对象

result.execute("use xuefeng")                   #进入该数据库
result.execute("show tables")
table_sql = result.fetchall()                   #使用fetchall()返回全部结果行
print(table_sql)
#使用预处理语句创建一个表
table =  """create table  xuefeng(
id int(11)  not null,
name varchar(255),
sex  char(5),
age  varchar(20),
primary key (id)
)
"""
#使用execute执行SQL语句
result.execute(table)

result.execute("show tables")
table_sql = result.fetchall()
print(table_sql)
conn.close()

