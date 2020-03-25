#类的多态
# 1.方法有多态，属性没有多态
# 2.多态必然存在类的继承，重写方法

class Man:
    
    def eat(self):
        print("饿了要吃饭")

class Chinese(Man):

    def eat(self):                              #重写eat()方法
        print("中国人用筷子吃饭")

class English(Man):

    def eat(self):
        print("英国人用刀叉吃饭")

class Indian(Man):

    def eat(self):
        print("印度人用手抓")

def manEat(m):
    if isinstance(m,Man):        #判断m实例对象是否为Man类的继承，是返回True，不是返回false
        m.eat()                  #返回True，调用m实例对象中的方法eat()
    else:
        print("不准吃饭")

manEat(Chinese())
manEat(English())
manEat(Indian())

'''isinstance()函数的使用方法
isinstance(object,classinfo),isinstance函数中含有2个变量：
1.object:实例对象
2.classinfo:判断实例对象是否属于指定类中，即是否为该类的继承
'''


