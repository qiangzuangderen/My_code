#运算符重载

class Person:

    def __init__(self,name):
        self.name = name

#"+"运算符的重载

    def __add__(self,other):       
        if isinstance(other,Person):                            #判断other的实例对象属性是否为Person类的继承
            print("{0}--{1}".format(self.name,other.name))      #取other实例对象name属性：other.name
        else:
            return "不同类型，不能相加"

#"*"运算符的重载

    def __mul__(self,other):
        if isinstance(other,int):                               #判断other的实例对象是否为int类的继承
            return self.name*other
        else:
            return "NO"

s1 = Person("yang")
s2 = Person("lin")
s3 = s1 + s2
print(s3)
s4 = s1 * 10
print(s4)
print(dir(object))