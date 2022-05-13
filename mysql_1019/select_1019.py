import  pymysql
from mysql_1019.info  import *
import  os

conn = pymysql.connect(host="localhost",user=user,password=password,database=database,port=port)
result = conn.cursor()


result.execute("select * from xuefeng")
select_sql = result.fetchall()
print(select_sql)


result.execute("select * from  xuefeng  where id =1")
select_sql_1 =result.fetchall()
print(select_sql_1)

#导出数据到excel表
conn.close()