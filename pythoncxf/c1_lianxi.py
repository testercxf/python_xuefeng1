print("Hello Python")

# name_cxf = 123
# print(name_cxf, type(name_cxf))
# name_cxf1 = "chenxuefeng"
# print(name_cxf1, type(name_cxf1), len(name_cxf1))
# #
# aa=123 * name_cxf - name_cxf / name_cxf + name_cxf
# print(aa)
#
# bb= "chenxuefeng"
# print("我的姓名:" +  bb)


#将一串字符串翻转打印
# name = (""" list_1"" n"1"i"" """)
# print(name)
# aa = "1234567"
# print(aa[:-1])
# print(aa[::-1])

#格式化输出
# bb=1
# cc="list_11"
# print("nishuosm:%s,list_11%d"  %(cc,bb))

# dd=cc * 10
# print("你好啊:\n%s"  %(dd))
# print("请输入你的成绩")
# print( 0 and  1  , 1  and  1  , 1  and  0  , 0  and  0)
# aa=input("请输入你的名字")
# bb=input("请输入你的名字")
# cc=input("请输入你的名字")
# print("欢迎您:{2},{0},{1}".format(aa,bb,cc))       #设置指定位置

#内置函数
# input()
# print()
# int()
# str()
# aa = [1,2,2.22,42,0]
# print(max(aa))
# print(min(aa))
# print(sorted(aa,reverse=True))
# object()
# print(round(22.65789))
# list()
# tuple()
# dict()
# str()


# list_1 = [1,2,3,1,2,11,"list_1",(1,2)]
# print(list_1[1],list_1[7], type(list_1), len(list_1))
# tuple =(1,2,"list_1a",[1,2])
# print(tuple[2],list_1, type(tuple), len(tuple))
#元组和列表的区别：列表属于可变序列，它的元素可以随时修改或者删除
#元组输入不可变序列，它的元素是不可以修改的，除非整体重新赋值

# list1 = [1,2,5,3,13,5]
# list2 = ["你哈","好啊","加油"]
# tuple1 = ("a","ss","dd","sds")
# print(sorted(list1, reverse= True), type(list1))  #sorted：对数值和字符串进行排序，reverse=True:降序排序（默认为false）
# print(sorted(list2,reverse=False))                #True和False的首字母必须大写，不能全小写，不能全大写
# print(sorted(tuple1,key=len,reverse=True))        #key=len:对长度进行降序排序



# print("如果这是真的",end="")
# print("这是真的还是假的", end="\n")
# print("如果这是假的", end="\t")           #end=""  跟什么，就是以什么结尾。print自带换行


# #修改列表值
# list = [1,23,2,32,21,2]
# list[1] = 111
# print(list)
# tuple = [1,22,"nihao",232,[1,"nihao",11]]
# print(tuple, type(tuple))
# tuple[4][0] = "nmm"
# print(tuple)

# 修改字典value值和新增一个键值对
# zidian1 = {"日期":"2021-2-1","时间":"10:11:53"}
# print(zidian1)
# zidian1["日期"]= "2021-11-21"
# zidian1["纪恋日"]="9999"
# print(zidian1)
# print(zidian1["日期"])
# key是唯一的，不能重复，value可以重复
# 对已存在的key进行新增，会覆盖之前的值

#格式化
# shuzi1 =  "nihao,111"
# shuzi2 = 111
# print("你说什么:%s" %(shuzi1))
# print(shuzi1, type(shuzi1))
# shuzi = str(1111)
# print(shuzi, type(shuzi))

# tuple1 = ([1,2],[3,6])
# print(tuple1,type(tuple1))
# print(tuple1[1])
# dict1 =dict(tuple1)
# print(dict1)
# #将元组更改为字典

# list = [20,30,40,50]
# print(list, type(list))
# tuple = (20,30,40,50)
# print(tuple, type(tuple))
# dict = {20:12,30:21,40:21,50:21}
# print(dict, type(dict))

#转换为字典类型
# tuple1 = ([10,20],[20,30],[40,50])
# print(tuple1)
# dict1 =dict(tuple1)
# print(dict1)

#查找字符串,如有多个重复字符，只会返回第一个出现的下标
# a= "hello world"
# print(a.find("o w5rf.5u654"))
# print(a.find("he"))

#字符串合并
# a = "*"
# b = ("nihao","nihaoa","nihaoaa")
# print(a.join(b))

#字符串拆分
# a1 = "nihao1 1a sa f"
# print(a1.split(" "))

#判断字符串的开头结尾，返回布尔值
# aa =  "ni  nih"
# print(aa.startswith("i"))       #判断开头
# print(aa.endswith("h"))         #判断结尾

#替换字符串，临时替换
# aaa = "tihuan"
# print(aaa. replace("ti","tihuan"))
# print(aaa)


# b = "34"
# c = "123panduan你好"
# print(b.isalpha())
# print(b. isalnum())
# print(c. isalpha())
# print(c. isalnum())
#isalpha()如果字符串至少有一个字符并且所有字符都是字母，则返回True
#isalnum()如果字符串中只包含数字则返回数字则返回True，反之返回False



#zip转换
# key = ["name","age","sex"]
# value = ["张三",19,"男"]
# zip = dict(zip(key,value))
# print(zip)
# for zip in zip(key,value):
# print(zip, type(zip))/


#列表推导式
# a = [x for x in range(1,10) if  x<7 ]
# print(a)
# a = [x*3 for x in range(1,20)]
# print(a,len(a))
# a = [(aa,bb) for aa in range(1,10) for bb in range(2,10)]  #使用两个循环
# print(a)

#字典推导式
# text_count ="hello python hello world !!!"
# c = {a:text_count.count(a) for a in text_count }
# print(c)


#生成器推导式（元组推导式）
# a = (x for x in range(1,10))
# print(a)
# print(tuple(a))
# print(tuple(a))   #只能遍历一次

# for x in a:
#     print(x, end= "**")     #a是生成器对象，生成器是可迭代的对象
# print(tuple(a))


#函数练习
# def  test_1(a,b):
#     """根据两个值大小进行判断"""
#     if a>b:
#         print("a最大:%d"%a)
#     elif b>a:
#         print("b最大:%d"%b)
#     else:
#         print("错啦")
#
# test_1(20,30)
# help(test_1.__doc__)    #获取某一个函数的描述



# def  add(a,b):
#     """求两数相乘
#     :param a: a的值
#     :param b: b的值
#     """
#     print(a*b)
# add(10,20)

# print("#################################################")

#局部变量和全局变量
# a = 20
# def fi(a,b,c):
#     print(a,b,c,)
#     print(locals())
#     print("#"*20)
#     print(globals())
# fi(10,20,30)




#文件的读写操作
# with open("test_cxf","r", encoding="utf-8") as f:       #读取文件内容
#     print(f.read())
#
# with open("test_cxf","a") as f1:                 #写入文件内容
#     print(f1.write("hell python\n"))
#
# with open("test_cxf",encoding="utf-8") as f11:
#     print(f11.read())


# print("###########################################")
# a = [21,13,43,23,53,63,31]
# for x in range(len(a)):
#     for y in range(len(a)-1):
#         if a[x]<a[y]:
#             a[y],a[x] = a[x],a[y]
# print(a)



#冒泡排序
def  maopao(b):
    for x in range(len(a)):
        for y in range(len(a)-1):
            if a[x] < a[y]:
             a[y], a[x] = a[x], a[y]
    return b

a = [21,13,43,23,53,63,31]
print(maopao(a))


#用while循环输出99乘法表
 # row =1
 # while  row<=9:
 #     col =1
 #     while col<=row:
 #         print("%d*%d=%d" %(col,row,row*col),end="\t")
 #         col +=1
 #     print()
 #     row +=1
