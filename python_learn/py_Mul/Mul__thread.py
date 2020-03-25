#线程_thread

import _thread
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
    """生成主进程"""
    print("mainProcess start...")
    """创建线程，向函数传值，注意数据格式"""
    _thread.start_new_thread(work01,("tread_01",4))
    time.sleep(1)
    _thread.start_new_thread(work02,("tread_02",2))
    time.sleep(5)
    print("mainProcess end...")