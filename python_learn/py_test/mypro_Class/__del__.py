#析构方法__del__

class person:

    def __del__(self):
        print("销毁对象{0}".format(self))

s1 = person()
s2 = person()
del s2
print("程序结束")
print(s1)