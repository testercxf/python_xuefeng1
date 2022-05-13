import  pymysql
from mysql_1019.info  import *


conn = pymysql.connect(host="localhost",user=user,password=password,database=database,port=port)

result = conn.cursor()                   #使用curs()方法创建一个游标对象cursor

result.execute("select * from xuefeng")
del_1 = result.fetchall()                #使用fetchall()返回全部结果行
print(del_1)


result.execute("delete from xuefeng")
conn.commit()

result.execute("select * from xuefeng")
del_2 = result.fetchall()
print(del_2)

conn.close()