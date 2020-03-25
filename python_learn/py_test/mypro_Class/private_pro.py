#测试私有属性

class Emplyee:

    __company = "ZTG"            #私有类属性：__变量名

    def __init__(self,name,age):
        self.name = name
        self.__age = age      #定义age为私有实例属性：__属性名

    def __work(self):          #定义私有实例方法：def __方法名(self)
        print("疯狂工作")
        print("年龄：{0}".format(self.__age))    #类内部调用私有属性
        
        

s1 = Emplyee("yang",6)
print(s1.name)
print(s1._Emplyee__age)      #访问私有属性的格式：_类名__属性名 
print(s1._Emplyee__work())
print(s1._Emplyee__company)    #访问类私有变量格式：_类名__变量名
print(dir(s1))
