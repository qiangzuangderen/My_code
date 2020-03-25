#线程中变量共享，互斥锁：非阻塞方式
"""
通过运行结果显示，同一个进程中，线程中可共享全局变量,如果一个线程动态，一个线程静态，不会引起错误，
如果两个线程都是动态，会对CPU资源进行抢夺，当计算量大时，会出错。
"""

from threading import Thread,Lock
import time

num = 0
"""创建互拆锁，两个线程谁先抢占CPU资源,另一个线程就自动上锁，等第一个线程释放资源后，第二个线程自动解锁"""
mutex = Lock()

def work01():
    global num
    mutex.acquire()  #上锁
    for i in range(1000000):
        num += 1
    mutex.release()   #解锁
    print("Test end num = ",num)

def work02():
    global num
    mutex.acquire()
    for i in range(1000000):
        num += 1
    mutex.release()
    print("Test end num = ",num)

if __name__ == "__main__":
    print("main_Process start:")
    t1 = Thread(target=work01)
    t2 = Thread(target=work02)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main_Process end")
