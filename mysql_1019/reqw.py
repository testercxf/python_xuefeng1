
# 如何使用python records 库优雅的操作数据库
# https://www.cnblogs.com/wagyuze/p/11398484.html


# def fun (s):
#     n = 0
#     for x in s:
#         if x.isdigit():
#             n = n*16 + int(x)
#         else:
#             n=n*16 + 10 + ord (x)-ord ("A")
#     return n
#
# while True:
#     try:
#         s = input()
#         s = s.replace ( 'cxf', '')
#         n = fun(s)
#         print(n)
#     except:
#         break
#
#
#
#
# # 结点
# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None        # = Node()
#
#
# # 链表
# class Link():
#     def __init__(self):
#         self.head = None        # = Node()
#
#     def insert(self, a, b):
#         # a 插到 b 后
#         node = Node(a)
#         p = self.head
#         while p is not None:
#             if p.data == b:
#                 break
#             p = p.next
#         if p is not None:
#             q = p.next
#             p.next = node
#             node.next = q
#
#     def visit(self):
#         li = []
#         p = self.head
#         while p is not None:
#             li.append(p.data)
#             p = p.next
#         return li
#
#     def delete(self, data):
#         p = self.head
#         if p.data == data:
#             self.head = p.next
#             return
#         else:
#             q = p
#             p = p.next
#             while p is not None:
#                 if p.data == data:
#                     q.next = p.next
#                     return
#                 p = p.next
#                 q = q.next
#
#
# s = input()
# li =  s.split( )
# # n = int(li[0])1
# f = li[1]
# obj = li[-1]
# # 创建，插入
# link = Link()
# link.head = Node(f)
# for i in range(2,len(li)-1,2):
#     a = li[i]
#     b = li[i+1]
#     link.insert(a, b)
# # 删除
# link.delete(obj)
# # 打印
# li = link.visit()
# if li == []:
#     print('null')
# else:
#     print(' '.join(li) + ' ')

#
# def f(n,k):
#     num=0
#     if k==0:
#         num=num+1
#     for n in range(k,n+1):
#         while n>0:
#             j=n%10
#             n=n//10
#             if j==k:
#                 num=num+1
#         print(num)
# f(2000,0)

#
# def fun(a,b,c):
#     print(a,b,c)
# list = [1,2,3]
# fun(*list)
#
# def fun1(a,b,c):
#     print(a,b,c)
# dict = {"a":111,"b":222,"c":333}
#
# fun(**dict)


# def fun4(a,b,*,c,d):   #从*之后的参数，在函数调用时，只能采用关键字参数传递
#     print(a,b,c,d)
#
# #调用fun4函数
# # fun4(10,20,30,40)  #位置实参传递
# fun4(a=10,b=20,c=30,d=40) #关键字实参传递
# fun4(10,20,c=30,d=40)  #前两个参数，采用的是位置实参传递，而c,d采用的是关键字实参传

# def fac(n):
#     if n==1:
#         return 1
#     else:
#         res=n*fac(n-1)
#         print(res)
#         return  res
#
# print(fac(6))

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)  #fib(5)+fib(4)
#斐波那契数列第6位上的数字
print(fib(6))
print('------------------------------')
#输出这个数列的前6位上的数字
for i in range(1,7):
    print(fib(i))

# names = ['张三','张晓霞','李旺明','陈晓旭','阿莫西林']
#
# result = [name for  name in names if len(name)>=3]
# print(result)

# num1 = 1
# num2 = 2
# res = 1
# ress =[]
# ress.append(res+num1) if  num1>num2  else  ress.append(res-num2)
# print(ress)
#
# def  maxnum(x,y):
#     return x if  x>y else y
#
# print(maxnum(3,2))
#
#
# print([0 if i % 2 == 0 else 1 for i in range(20)])

cond = False
name = ["Cat", "Tom"][bool(cond)]
print(name)


