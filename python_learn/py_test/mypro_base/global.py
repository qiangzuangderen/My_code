import math
import time

a = 3   #全局变量

def test_func():
    b = 4 #局部变量
    print(b*10)

    global a   #声明使用全局变量
    a = 300    #改变全局变量的对象赋值
    print(a)

test_func()
print(a)       #全局变量的赋值以改变


#------------------变量效率测试-------------------

def test01():
    start = time.time()
    for i in range(100000000):
        math.sqrt(99)       #使用全局变量对象math.sqrt
    end = time.time()
    print("耗时：{0}".format((end - start)))

def test02():
    b = math.sqrt       #将math.sqrt对象赋值给b，形成局部变量
    start = time.time()
    for t in range(100000000):
        b(99)           #调用局部变量b
    end = time.time()
    print("耗时：{0}".format((end - start)))

test01()
test02()


