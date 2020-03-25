#方法没有重载，以最后定义的方法为准，方法是动态的，方法也是对象

class Person:

    def work(self):
        print("努力工作")

def play_Game(a):
    print("{0}好好玩".format(a))

def work2():
    print("疯狂工作")

s1 = Person()
s1.work()
s1.play = play_Game   #将play_Game()作为对象赋给类Person中的新方法play
s1.play("yang")
s1.work = work2       #将work2()作为对象赋给类Person中的方法work，因为方法没有重载，以第二次定义的work2为准
s1.work()