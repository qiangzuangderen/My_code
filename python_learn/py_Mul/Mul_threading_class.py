#用继承方式创建线程

import threading
import time

def work01(delay):
    print("{0} start...".format(threading.current_thread().getName()))
    time.sleep(delay)
    print("{0} end...".format(threading.current_thread().getName()))

def work02(delay):
    print("{0} start...".format(threading.current_thread().getName()))
    time.sleep(delay)
    print("{0} end...".format(threading.current_thread().getName()))

class MyThread(threading.Thread):

    """构造函数中需传入的参数：外部函数名称，线程名称（若不指定，默认为Thread-1,Thread-2...）,外部函数的参数"""
    def __init__(self,func,name,test):
        super().__init__(target=func,name=name,args=test)

    """重写run()方法，在调用函数的过程中，_target()对应构造器中的target,_args对应构造器中的args"""
    def run(self):
        self._target(*self._args)

if __name__ == "__main__":
    print("main_Process start...")
    t1 = MyThread(work01,"tread01",(4,))
    t2 = MyThread(work02,"tread02",(2,))
    t1.start()
    time.sleep(1)
    t2.start()
    t1.join()
    t2.join()
    time.sleep(1)
    print("main_Process end...")