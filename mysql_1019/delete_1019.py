import  pymysql

conn = pymysql.connect(host="localhost",user="root",password="111400cxf",database="xuefeng",port=3306)

result = conn.cursor()                   #使用curs()方法创建一个游标对象cursor

result.execute("select * from xuefeng")
del_1 = result.fetchall()                #使用fetchall()返回全部结果行
print(del_1)


result.execute("delete from xuefeng where id =4")
conn.commit()

result.execute("select * from xuefeng")
del_2 = result.fetchall()
print(del_2)

conn.close()