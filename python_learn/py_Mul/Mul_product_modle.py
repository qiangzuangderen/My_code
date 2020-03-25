#生产消费模式

from threading import Thread
from queue import Queue
import time

class producter(Thread):

    def run(self):
        while True:
            global queue
            count = 0
            if queue.qsize()<1000:
                for i in range(100):
                    count += 1
                    msg = self.name + "生产第" + str(count) + "个产品"
                    queue.put(msg)
                    print(msg)
                time.sleep(0.5)


class costumer(Thread):

    def run(self):
        while True:
            global queue
            if queue.qsize()>100:
                for i in range(10):
                    msg = self.name + "消费" + queue.get()
                    print(msg)
                time.sleep(1)


if __name__ == "__main__":

    queue = Queue()
    p = producter()
    c = costumer()
    p.start()
    time.sleep(1)
    c.start()