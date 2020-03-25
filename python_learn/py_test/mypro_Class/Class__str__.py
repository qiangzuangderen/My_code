#重写__str__()方法

class Person:

    def __init__(self,name):
        self.name = name

#默认状态打印的是类的id
#重写object类的__str__()方法
#重写后将在__str__()方法中调用类的属性

    def __str__(self):
        return "名字是：{0}".format(self.name)

s1 = Person("yang")
print(s1)