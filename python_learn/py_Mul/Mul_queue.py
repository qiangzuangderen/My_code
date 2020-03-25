#队列的用法

from multiprocessing import Queue

q = Queue(3)                        #设定队列的长度为3
"""put()为向队列中存元素"""
q.put("message1")
q.put("message2")
q.put("message3")
print(q.full())
if not q.full():
    q.put("message4",block=True,timeout=1)       #block=True为确定队列已满，timeout=1为等待1秒后报异常

for i in range(q.qsize()):     #qsize()为队列的长度
    print(q.get())             #get()为向队列中取元素
print(q.empty())               #判断队列是否为空
if not q.empty():
    print(q.get(block=True,timeout=1))          #队列已空，等待1秒后报异常
