#多任务的属性

import multiprocessing
import time

def clock1(interval):
    print("当前时间：",time.ctime())
    time.sleep(interval)
    print("end clock1")

def clock2(interval):
    print("当前时间：",time.ctime())
    time.sleep(interval)
    print("end clock2")

def clock3(interval):
    print("当前时间：",time.ctime())
    time.sleep(interval)
    print("end clock3")

if __name__=="__main__":
    p1 = multiprocessing.Process(target=clock1,args=(5,))
    p2 = multiprocessing.Process(target=clock2,args=(2,))
    p3 = multiprocessing.Process(target=clock3,args=(3,))
    p1.start()
    p2.start()
    p3.start()
    """jion()方法确定子进程完成后，再结束主进程"""
    p1.join()
    p2.join()
    p3.join()
    print("pid:",p1.pid,p2.pid,p3.pid)
    print("pname",p1.name,p2.name,p3.name)
    """p.is_alive()方法为判断子进程是否还存在，布尔类型，返回True或者False"""
    print("alive:",p1.is_alive(),p2.is_alive(),p3.is_alive())
    print("main process end...")