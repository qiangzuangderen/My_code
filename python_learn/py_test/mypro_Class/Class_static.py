#测试类方法、静态方法
#注意：在类方法和静态方法中，不能调用实例属性和实例方法，因为实例属性和实例方法还未初始化

#类方法------------------------------------------------

class Student:

    company = "ZTG"
    @classmethod
    def print_company(cls):       #必须有类对象参数cls
        print("公司名称是：{0}".format(cls.company))

Student.print_company()


#静态方法-----------------------------------------------

class Student2:

    company = "ZTG"

    @staticmethod

    def add_print(a,b):
        print("{0}+{1}={2}".format(a,b,a+b))

c = int(input("Please input a int c:"))
d = int(input("Please input a int d:"))
Student2.add_print(c,d)