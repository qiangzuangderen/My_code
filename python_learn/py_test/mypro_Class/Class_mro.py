#测试mro()的类解析顺序


class A:
    
    def aa(self):
        print("aa")

    def say(self):
        print("say AAA")

class B:

    def bb(self):
        print("bb")

    def say(self):
        print("say BBB")

class C(A,B):           #父类谁写在前面，同名方法调用谁

    def cc(self):
        print("cc")

s1 = C()
s1.say()
print(C.mro())