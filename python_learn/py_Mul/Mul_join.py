#测试join()方法

from multiprocessing import Process
from time import sleep

def worker(interval):
    print("work start....")
    sleep(interval)
    print("work end....")

if __name__=="__main__":
    print("main process start....")
    p = Process(target=worker,args=(5,))   #子进程传参，target=方法名，args=(参数1，参数2，……)
    p.start()
    """join(time)方法的用途为：主进程开始运行后，
    必须执行完join()方法中time的值再关闭主进程，
    不设置time的值表示等待的时间等于子进程执行的时间"""
    p.join(3)
    print("main process end....")