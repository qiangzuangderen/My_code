#对象的浅拷贝和深拷贝
import copy

class MobilePhone:

    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

class Cpu:

    def calculate(self):
        print("Cpu处理运算")
        print("Cpu对象：",self)

class Screen:

    def show(self):
        print("screen处理图像显示")
        print("screen对象：",self)

#测试重复赋值，赋值指向同一个ID
s1 = Cpu()
s2 = Screen()
s3 = s1
print(s3)

#测试浅拷贝,浅拷贝只拷贝父类，不拷贝子类（子类的ID相同）
a1 = MobilePhone(s1,s2)                          #组合：将类Cpu(),类Screen()作为对象，封装到类MobilePhone()中，对应类MobilePhone()中的属性cpu，screen
a2 = copy.copy(a1)
print(a1,a1.cpu,a1.screen)
print(a2,a2.cpu,a2.screen)

#测试深拷贝,深拷贝完全拷贝父类，生成新的ID
b2 = copy.deepcopy(a1)
print(a1,a1.cpu,a1.screen)
print(b2,b2.cpu,b2.screen)

a1.cpu.calculate()                              #调用组合中的方法
