class  Rectangle:
    def  __init__(self,x,y):                 #初始化方法，定义一个类的时候指定这个类中包含有哪些属性
        """定义形参并给属性赋初始值
        :param x: 长方形的长
        :param y: 长方形的宽
        """
        self.length = x                       #self.属性 = 形参
        self.width = y
    def perimeter(self):
        """求长方形的周长"""
        num_perimeter = (self.length +self.width)*2
        print("该长方形的周长为：%.2f" %num_perimeter)

    def proportion(self):
        """求长方形的面积"""
        num_proportion = self.length*self.width
        print("该长方形的面积为：%.2f" %num_proportion)

if  __name__ == "__main__":                 #其中的代码就不会在被 import 时被执行
    num_zc = Rectangle(7,8)                #自动调用初始化方法
    num_zc.perimeter()
    num_zc.proportion()


