#类的组成

class Students:

    def __init__(self,name,score):   #构造函数__init__()，定义类的实例属性，self必须列第一位
        self.name = name
        self.score = score

    def say_score(self):             #定义类的方法
        print("{0}的分数是{1}".format(self.name,self.score))

s1 = Students("yang",90)    #通过类名（）调用构造函数，self为对象本身，指定ID，调用时将ID赋给s1
s1.say_score()
Students.say_score(s1)     #解释器在执行时先找到类，再去找类中的方法，再去找方法的对象，再为对象传值
Students.say_score(Students("ling",77))