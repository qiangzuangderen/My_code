#测试装饰器



class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    @property                         #装饰器用途为：将方法转换为属性使用，@property表示方法salary可读
    def salary(self):
        return self.__salary

    @salary.setter                     #@*.setter表示方法salary可写,@*.delete表示方法salary可删除
    def salary(self,salary):
        if 1000<salary<5000:
            self.__salary = salary
        else:
            print("Wrong setting")

'''

#不使用装饰器---------------------------------------------------------

    def get_salary(self):          #get方法：获取私有属性的值
        return self.__salary

    def set_salary(self,salary):     #set方法：设置私有属性的值
        if 1000<salary<5000:
            self.__salary = salary
        else:
            print("Wrong input")
'''

s1 = Employee("yang",40000)
print(s1.salary)                   #此时方法salary已转换为属性，调用时按属性的规则
s1.salary = 3500                   #属性设置可写，可以直接赋值修改
print(s1.salary)

