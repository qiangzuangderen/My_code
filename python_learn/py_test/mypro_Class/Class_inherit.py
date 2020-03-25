#类的继承和方法重写
#object类时所有类的父类

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_age(self):
        print("How old are you?")

class Student(Person):

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)
        self.score = score

#重写say_age方法，在调用Student类中的say_age方法时，重写的方法覆盖继承父类的方法

    def say_age(self):
        print("I know your age is {0}".format(self.age))


s1 = Student("yang",6,90)
s1.say_age()
print(s1.age)
s1.age = 12
print(s1.age)
s1.say_age()
print(dir(object()))
print(dir(s1))