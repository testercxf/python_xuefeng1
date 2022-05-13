
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




# 结点
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None        # = Node()


# 链表
class Link():
    def __init__(self):
        self.head = None        # = Node()

    def insert(self, a, b):
        # a 插到 b 后
        node = Node(a)
        p = self.head
        while p is not None:
            if p.data == b:
                break
            p = p.next
        if p is not None:
            q = p.next
            p.next = node
            node.next = q

    def visit(self):
        li = []
        p = self.head
        while p is not None:
            li.append(p.data)
            p = p.next
        return li

    def delete(self, data):
        p = self.head
        if p.data == data:
            self.head = p.next
            return
        else:
            q = p
            p = p.next
            while p is not None:
                if p.data == data:
                    q.next = p.next
                    return
                p = p.next
                q = q.next


s = input()
li =  s.split( )
# n = int(li[0])
f = li[1]
obj = li[-1]
# 创建，插入
link = Link()
link.head = Node(f)
for i in range(2,len(li)-1,2):
    a = li[i]
    b = li[i+1]
    link.insert(a, b)
# 删除
link.delete(obj)
# 打印
li = link.visit()
if li == []:
    print('null')
else:
    print(' '.join(li) + ' ')

