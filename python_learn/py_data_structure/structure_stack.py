#栈的实现
"""
栈的运行规则：
LIFO（Last In First Out）原则，先进后出
"""

class Stack(object):
    """构造栈，初始化空列表"""
    def __init__(self):
        self.items = []

    #1.判断栈是否为空
    def is_empty(self):
        return self.items == []

    #2.加入元素
    def push(self,items):
        self.items.append(items)

    #3.弹出元素
    def pop(self):
        return self.items.pop()

    #4.返回栈顶元素
    def peek(self):
        return self.items[len(self.items)-1]

    #5.返回栈的大小
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push("Hello")
    stack.push("python")
    stack.push("world")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())