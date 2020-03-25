#测试ThreadLocal，设置线程局部变量
"""ThreadLocal的作用，因为全局变量在多个线程中共享，ThreadLocal的作用为保护线程中变量的安全，多个线程运行时，每个线程的变量独立"""

import threading

local = threading.local()

def process_add():
    sum = local.num
    for i in range(1000):
        sum += 1
    print("线程{0}的sum为：{1}".format(threading.current_thread().getName(),sum))


def process_thread(num):
    local.num = num
    process_add()

t1 = threading.Thread(target=process_thread,name="Thread1",args=(6,))
t2 = threading.Thread(target=process_thread,name="Thread2",args=(9,))
t1.start()
t2.start()
t1.join()
t2.join()