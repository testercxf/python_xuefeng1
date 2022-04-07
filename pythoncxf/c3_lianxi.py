# user_1 = input("请输入卡号")
# psw_1  = input("请输入密码")
# user = ""
#
#
# a = 5
# b = 3
# print(a**b)

# a = "'"
# b = "1"
# print(b<a)
#


# a = ("a")
# print(type(a))

# a = ["aaa","bb","cccc","d",12,4.3,True]
#
# b =a.extend(["1","2","3"])
# print(sorted(a, reverse=True))

# print(sorted(a, key=len,reverse=True))
# print(().)
# print(a)
# b = a
# print(b)
# print(a)

# a.clear()
# print(a)
# a.append(100)
# print(a)
# a.remove(100)
# print(a)

# a = ["90.9",90]
#
# a.insert(1,"python")
# print(a)
# 插入

# a.sort(reverse=True)
# print(a.)
# 排序并修改变量本身

# a = [22,"hello",22,6.66,True]
# print(a.index(22, 1,5))
# 查找

# a = (["hello",20,30],{"name":"张三","sexx":"男"})
#
# a[0][0]="python"
# b = a[1]["name"]="李思"
# print(a, type(a))
# 元组中包含列表和字典的对象时，怎么修改


# a = {1:20,2:30}
# print(a.keys())
# print(a)


# a = int(input("请输入你的年龄"))
# if a>=18:
#     print("你已成年！")
# else:
#     print("你还是未成年！")
# 代码块缩进

#替换
# a = "hello world"
# print(a. replace("hello","你好"))


# a = 3
# b = 1
# c = 0
# if a<b:
#     c = a
# else:
#     c = b

# c = a if a<b else b
# print(c)


# a = 1
# while  a<6:
#     print("第一次")
#     a = a+2
# 循环练习

# for循环练习(用for循环遍历变量a并存放变量b中)
# a = {"1":22,"sexx":"男"}
# b = []
# for i in a.items():
#     b.append(i)
# print(b)


# for练习()
# import  math
# for a in range(0,8):
#     print("a={}".format(a))
#     print(round(math.pi, a))


# 查找[1,100)3的倍数,并将最后一次结果存放在列表中
# n = 0
# m = []
# for a in range(1,100):
#     if  a%3 ==0:
#         # n = n + 1
#         # if n ==99:
#         m.append(a)
#         print("%a是3的倍数"%a)
# print(m)
#         break


# 获取0到8之间的基数并追加到列表中
# js_1 = []
# for a in  range(0,10):
#      if  a%2 == 1:
#          js_1.append(a)
#          print(js_1)





#while循环打印99乘法表
# a = 0
# while a<=9 :
#     b = 1
#     while  b<=a:
#         print("%d*%d=%d\t" %(b,a,a*b),end="")
#         b+=1
#     print("")
#     a+=1



#输出99乘法表
# for x in range(1,10):
#     for y in range(1,x+1):
#         print("{}*{}={}\t".format(y,x,(x*y)),end="")
#     print("")


# 1-100的累加和，基数和，偶数和
sum_all = 0
sum_odd = 0
sum_even = 0
for  x in  range(1,101):
    sum_all += x
    if  x%2 == 1:
        sum_odd += x
    elif  x%2 ==0:
        sum_even += x
    else:
        pass
print("1-100的累加和为:%d    100以内的奇数和是:%d   100以内的偶数和是:%d" %(sum_all, sum_odd, sum_even))


# for x in range(5):
#     for y in range(5):
#         print(x,end="\t")
#     print()




# dict_1 = dict(name="高小1",age=18,xz=30000,cs="北京")
# dict_2 = dict(name="高小2",age=19,xz=40000,cs="上海")
# dict_3 = dict(name="高小3",age=12,xz=20000,cs="北京")
# list_1 = [dict_1, dict_2, dict_3]
# for  a in  list_1:
#     if  a.get("xz")>20000:
#      print(a)


#要求输入员工的工资，若工资小于0则重新输入，最后打印出录入员工的数量和工资明细，以及平均工作
# num_yuangong = 0
# num_pjgongzi = 0
# list_1 = []
# while  True:
#     a = input("请输入员工工资，输入exit录入完毕")
#     if  a == "exit":
#         print("录入完毕")
#         break
#     if  float(a)<0:
#           continue
#
#     num_yuangong += 1
#     list_1.append(float(a))
#     num_pjgongzi += float(a)
#
# print("员工数:%d" %num_yuangong)
# print("工资:",list_1)
# print("平均工资:%.1f"%(num_pjgongzi/num_yuangong))



