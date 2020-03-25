#全局变量在不同子进程中不共享

from multiprocessing import Process

num = 10
def work01():
    global num
    num += 5
    print("work01 num:",num)

def work02():
    global num
    num += 10
    print("work02 num:",num)

if __name__ == "__main__":
    print("main process start...")
    p1 = Process(target=work01)
    p2 = Process(target=work02)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    p1.close()
    p2.close()
    print("main process end...,num:",num)