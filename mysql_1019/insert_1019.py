import  pymysql

#连接数据库
#localhost本地连接
conn = pymysql.connect(host="localhost",user="root",password="111400cxf",database="xuefeng",port=3306)

result = conn.cursor()                      #使用curs()方法创建一个游标对象cursor

result.execute("select * from xuefeng")
result_1 = result.fetchall()                #使用fetchall()返回全部结果行
print(result_1)
# 使用预处理语句插入数据
insert_sql = """insert into xuefeng  value(
1,"实习生","女","21"),
(2,"志刚","男","18"),
(3,"江辉","男","19")
# """
result.execute(insert_sql)
conn.commit()             #提交,如果不commit将不会提交到数据库的表中
#
# result.execute("select * from xuefeng")
# result_2 = result.fetchall()
# print(result_2)

conn.close()