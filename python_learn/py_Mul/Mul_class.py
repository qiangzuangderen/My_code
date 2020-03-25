#用继承的方法创建进程

import time
from multiprocessing import Process

class clockProcess(Process):

    def __init__(self,interval):
        Process.__init__(self)
        self.interval = interval

    """重写主类下的run(),进程调用start()方法时，其实调用的是主类的run()方法"""
    def run(self):
        print("process start....:{0}".format(time.ctime()))
        time.sleep(self.interval)
        print("process end....:{0}".format(time.ctime()))

if __name__=="__main__":
    print("主进程开始执行")
    """创建子进程"""
    p = clockProcess(3)
    """调用子进程的run()方法"""
    p.start()
    p.join()
    print("主进程执行完毕")