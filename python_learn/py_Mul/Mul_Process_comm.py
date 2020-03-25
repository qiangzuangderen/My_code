#进程间的通信的两种方式：先写再读
"""
流程：(队列方式:Queue())
1.创建队列；
2.创建子进程，将队列传递到方法中；
3.在方法中操作队列
------------------------
流程：（进程池方式：Pool()）
1.创建进程池；
2.创建子进程，将进程池传递到方法中（同步阻塞方式）；
3.在方法中操作队列。
"""

from multiprocessing import Process,Queue,Manager,Pool
from time import sleep

def write(q):
    a = ["a","b","c","d"]
    for i in a:
        print("Process write start...{0}".format(i))
        q.put(i)
        sleep(1)

def read(q):
    for i in range(q.qsize()):
        if not q.empty():
            print("Process read start...{0}".format(q.get()))
            sleep(1)
        else:
            break

if __name__ == "__main__":
    """
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    """
    q = Manager().Queue()
    pool = Pool(3)
    pool.apply(write,(q,))
    pool.apply(read,(q,))
    pool.close()
    pool.join()

