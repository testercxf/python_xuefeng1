import  pymysql
from mysql_1019.info  import *

#打开数据库连接
#localhost本地连接
conn = pymysql.connect(host="localhost",user=user,password=password,port=port)
#使用cursor()方法创建一个游标对象cursor
result = conn.cursor()                    #创建一个窗体命令行

#使用execute()方法执行SQL查询
result.execute("show databases")
#使用fetchone()返回一条结果行
#使用fetchall()返回全部结果行
data = result.fetchall()
print(data)

result.execute("create database xuefeng")       #执行SQL语句，创建一个名为xuefeng3的数据库

result.execute("show databases")
data = result.fetchall()
print(data)
conn.close()