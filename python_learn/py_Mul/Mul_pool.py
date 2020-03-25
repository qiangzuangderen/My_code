#进程池pool

import multiprocessing
import time

def Process_work(msg):
    print("process start:",msg)
    time.sleep(3)
    print("process end:",msg)

if __name__ == "__main__":
    """设置进程池中可容纳3个子进程"""
    p =multiprocessing.Pool(3)
    for i in range(1,7):
        msg = "Process{0}".format(i)
        """异步阻塞方法，3个一组，完成一个进一个"""
        p.apply_async(Process_work,(msg,))
        """同步阻塞方法，一个完成执行下一个"""
        #p.apply(Process_work,(msg,))
    p.close()
    p.join()

