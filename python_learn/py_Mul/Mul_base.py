#测试多任务
from multiprocessing import Process
from time import sleep

def song():
    for i in range(3):
        print("for song,{0}".format(i))
        sleep(1)

def dance():
    for i in range(3):
        print("for dance,{0}".format(i))
        sleep(1)

if __name__=="__main__":
    song()
    p = Process(target=dance)
    p.start()