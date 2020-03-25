#线程中合理的互斥锁方式：阻塞方式


from threading import Thread,Lock
import time

num = 0
"""创建互拆锁，两个线程谁先抢占CPU资源,另一个线程就自动上锁，等第一个线程释放资源后，第二个线程自动解锁"""
mutex = Lock()

def work01():
    global num

    for i in range(1000000):
        mutex.acquire()  # 上锁:合理的上锁因在线程做抢占动作之前，整个线程上锁，效率会低
        num += 1
        mutex.release()   #解锁:在用完资源后马上解锁，不能整个线程走完才解锁
    print("Test end num = ",num)

def work02():
    global num

    for i in range(1000000):
        mutex.acquire()
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
