# from  pythoncxf.c1_lianxi import  test_1
'''
python作业
'''

#根据用户输入的英文名字，对其正常输出和翻转输出
# yingwen_name = input("请输入你的英文名字:")
# dict_yw={}                                         #定义一个空字典
# dict_yw["name"] = yingwen_name
# fanzhuan = yingwen_name[::-1]                     #对用户输入的数据进行翻转
# dict_yw["new_name"] = fanzhuan
# real_name = dict_yw["name"]                        #通过key（键）查找对应的value（值）
# print("你的英文名字是:", real_name )
# print("你的英文名字翻转后是:", fanzhuan)





# 对用户输入的成绩进行升序排序并且输出最高的一门成绩
# sx_cj = float(input("请输入你的数学成绩:"))
# yw_cj  = float(input("请输入你的语文成绩:"))
# yyu_cj = float(input("请输入你的英语成绩:"))
# zh_cj = float(input("请输入你的综合成绩:"))
# paixu  = sorted([sx_cj, yw_cj, yyu_cj, zh_cj],reverse=True)           #对列表中的元素进行降序排序
# print("你的最高一门成绩是:", paixu[0])                                  #用索引方式输出列表中第一个元素
#print("你的最高一门成绩是:", max(paixu))



#求两个数的和
# a = float(input("请随机输入第一个数字:"))
# b = float(input("请随机输入第二个数字:"))
# c = a+b
# print("两数之和:%d"  %c)                         #当数据过大时不会以科学记数法展示输出结果



#99乘法表
# for x in range(1,10):
#     for y in range(1,x+1):
#         print("%d*%d=%d" %(y,x,(x*y)),end="\t")
#     print()                                      #换行作用




# 猜数字游戏
import  random
#
# sj_1 =random.randint(0,20)                              #限制随机数0到20
# while True:
#     number_1 = int(input("请输入你的答案"))
#     if  number_1 > sj_1:
#         print("你猜的太大了，往小了猜")
#     elif  number_1 < sj_1:
#         print("你猜的太小了，往大了猜")
#     else:
#         print("猜对啦，宝贝")
#        break


# with open("test.txt",encoding="utf-8") as f:
#      a = f.readlines()
#     for a in f.read():
#         print(a,)
#

#冒泡排序
# a=[100,97,4,89,34,2,100,200,42,12,32,231,21]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#            a[j+1],a[j] = a[j],a[j+1]
# print(a)





#创建一个文件并写入内容
# with  open("test_cxf","a",encoding="utf-8") as cxf:
#     cxf.write("何人半夜推山去？四面浮云猜是汝。\n常时相对两三峰，走遍溪头无觅处。\n")



#处理异常
# try:
#     with  open("test","r",encoding="utf-8") as cxf:
#         print(cxf.read())
# except:
#         print("81行到83行代码错误")                      #出现异常后输出该提示
# with open("test_cxf","r",encoding="utf-8") as cxf:       #以只读方式读取内容，encoding是防止无法识别10进制以外的
#         print(cxf.read())



# test_1(90,96)