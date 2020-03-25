#线程treading

import threading
import time

def work01(tread_name,delay):
    print("{0} start...".format(tread_name))
    time.sleep(delay)
    print("{0} end...".format(tread_name))

def work02(tread_name,delay):
    print("{0} start...".format(tread_name))
    time.sleep(delay)
    print("{0} end...".format(tread_name))

if __name__ == "__main__":
    print("main_Process start...")
    t1 = threading.Thread(target=work01,args=("tread01",4))
    t2 = threading.Thread(target=work02,args=("tread02",2))
    t1.start()
    time.sleep(1)
    t2.start()
    t1.join()
    t2.join()
    print("main_Process end...")