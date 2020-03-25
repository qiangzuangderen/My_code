#线程threading模块

import threading
import time

def work01(thread_name,delay):
    print("{0} start...".format(thread_name))
    time.sleep(delay)
    print("{0} end...".format(thread_name))

def work02(thread_name,delay):
    print("{0} start...".format(thread_name))
    time.sleep(delay)
    print("{0} end...".format(thread_name))

if __name__ == "__main__":
    print("main_Process start...")
    t1 = threading.Thread(target=work01,args=("thread01",4))
    t2 = threading.Thread(target=work02,args=("thread02",2))
    t1.start()
    time.sleep(1)
    t2.start()
    t1.join()
    t2.join()
    time.sleep(1)
    print("main_Process end...")