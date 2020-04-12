#队列的实现

"""
队列的运行规则：FIFO(First In First Out),管道原理，先进先出,尾部插入，头部出，头部插入，尾部出
"""

class Queue():
    """初始化队列"""
    def __init__(self):
        self.items = []

    """以下为队列的操作"""
    #1.判断队列是否为空
    def is_empty(self):
        return self.items == []

    #2.添加元素，进入队列
    def enqueue(self,item):
        #self.items.insert(0,item)  #在队列头部插入元素
        self.items.append(item)    #在队列末尾插入元素

    #3.出队列
    def dequeue(self):
        return self.items.pop(0)  #如果是尾部插入元素，则头部出队列
        #return self.items.pop()  #如果是头部插入元素，则尾部出队列

    #4.返回队列的大小
    def size(self):
        return len(self.items)

"""测试方式：尾部插入队列，头部出队列"""

if __name__ == "__main__":
    q = Queue()
    q.enqueue("Hello")
    q.enqueue("python")
    q.enqueue("world")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())