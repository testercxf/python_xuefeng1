import  pymysql

conn = pymysql.connect(host="localhost",user="root",password="111400cxf",database="xuefeng",port=3306)

result = conn.cursor()                  #使用curs()方法创建一个游标对象cursor


result.execute("select * from xuefeng")
select_sql = result.fetchall()          #使用fetchall()返回全部结果行
print(select_sql,end="\n\n")


result.execute("select * from  xuefeng  where id =1")
select_sql_1 =result.fetchall()
print(select_sql_1)

conn.close()