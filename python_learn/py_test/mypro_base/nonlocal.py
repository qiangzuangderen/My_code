#测试nonlocal/global声明

a = 0

def outer():
    b = 1
    def inner():
        nonlocal b
        b = 100
        print("b:",b)
    inner()
    global a
    a = 200
    print("a:",a)

outer()