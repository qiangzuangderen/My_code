#super()获取父类方法的定义，而不是父类的对象

class A:

    def say(self):
        print("A:",self)

class B(A):

    def say(self):
        super().say()        #仅调用A中say()方法的定义，执行的事B类的对象
        print("B:",self)

B().say()

'''执行结果：打印的为B类的ID
A: <__main__.B object at 0x000001F9F36D10D0>
B: <__main__.B object at 0x000001F9F36D10D0>
'''