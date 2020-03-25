#测试工厂模式和单例模式

class Carfactory:


    __obj = None                         #创建类属性，存放类的ID
    __init_flag = True                   #如果实例属性存在，不再创建新的实例属性



    def create_car(self,brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "不在库中，无法创建"

#单例模式-----------------------------------------------------

    def __new__(cls):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self):
        if Carfactory.__init_flag:
            print("Carfactory…………")
            Carfactory.__init_flag = False

#-------------------------------------------------------------


class Benz:
    pass

class BMW:
    pass


class BYD:
    pass

factory = Carfactory()                     #创建类Carfactory()的实例对象ID，存在__obj类属性中，为类Carfactory()的唯一ID，内存中不重复创建
s1 = factory.create_car("奔驰")
s2 = factory.create_car("宝马")
s3 = factory.create_car("比亚迪")
print(s1,s2,s3)

factory2 = Carfactory()             #单例模式：不同的变量名调用同一个对象，ID相同，只取__obj中的ID，内存中不创建新的ID
print(factory)
print(factory2)


print(factory._Carfactory__obj)