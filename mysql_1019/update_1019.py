import  pymysql

conn = pymysql.connect(host="localhost",user="root",password="111400cxf",database="xuefeng",port=3306)

result = conn.cursor()                      #使用curs()方法创建一个游标对象cursor


result.execute("select * from xuefeng ")
sql_1 = result.fetchall()                    #使用fetchall()返回全部结果行
print(sql_1)
#修改id是1的年龄

result.execute("update xuefeng  set age='19'  where id=1")
conn.commit()


result.execute("select * from xuefeng")
sql_2 = result.fetchall()
print(sql_2)

conn.close()