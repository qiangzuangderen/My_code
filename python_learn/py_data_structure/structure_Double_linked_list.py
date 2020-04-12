#双向列表
"""
双向列表与单项列表的区别：
1.一个节点分三个部分，反向指针prev，节点item，正向指针next；
2.反向指针指向前一个节点，正向指针指向后一个节点。
"""

class Node(object):
    """双向列表节点块"""
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class DlinkList:
    """双向链表"""
    #初始化链表
    def __init__(self,node=None):
        if node != None:
            Headnode = Node(node)
            self.__head = Haadnode
        else:
            self.__head = None

    """以下为双向列表的操作方法"""
    #1.判断链表是否为空
    def is_empty(self):
        return self.__head == None

    #2.计算链表的长度
    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    #3.遍历链表
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print()

    #4.头部插入元素
    def add(self,item):
        node = Node(item)
        if self.is_empty():
            #如果是空链表，将__head指向node
            self.__head = node
        else:
            #将__head的next指向__head
            node.next = self.__head
            #将__head的头结点的前驱prev指向node
            node.prev = node
            #将头结点指向node
            self.__head = node

    #5.链表尾部插入
    def append(self,item):
        """尾部插入"""
        node = Node(item)
        if self.is_empty():
            #如果是空链表，将头结点指向node
            self.__head = node
        else:
            #移动到链表尾部
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            #将尾节点cur的next指向node
            cur.next = node
            #将node的prev指向cur
            node.prev = cur

    #6.查找元素
    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    #7.指定位置插入
    def insert(self,pos,item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            #移动到指定位置的前一个位置
            while count < (pos - 1):
                count += 1
                cur = cur.next
            #将node的prev指向cur
            node.prev = cur
            #将node的next指向cur的下一个节点
            node.next = cur.next
            #将cur的下一个节点的prev指向node
            cur.next.prev = node
            #将cur的next指向node
            cur.next = node

    #8.删除节点
    def remove(self,item):
        curNode = self.__head
        while curNode != None:
            if curNode.item == item:
                #判断是否是头节点
                if curNode == self.__head:
                    self.__head = curNode.next
                    #判断链表是否只有一个节点
                    if curNode.next:
                        curNode.next.prev = None
                else:
                    #删除
                    curNode.prev.next = curNode.next
                    if curNode.next:
                        curNode.next.prev = curNode.prev
                break
            else:
                curNode = curNode.next

if __name__ == "__main__":
    doubleLinkList = DlinkList()
    doubleLinkList.add(11)
    doubleLinkList.add(22)
    doubleLinkList.add(33)
    doubleLinkList.travel()
    print("------------追加-----------")
    doubleLinkList.append(100)
    doubleLinkList.append(200)
    doubleLinkList.append(300)
    doubleLinkList.travel()
    print("------------指定位置插入----------")
    doubleLinkList.insert(1,44)
    doubleLinkList.travel()
    doubleLinkList.insert(100,400)
    doubleLinkList.travel()
    doubleLinkList.insert(2,1000)
    doubleLinkList.travel()
    print("-----------删除节点-----------")
    doubleLinkList.remove(44)
    doubleLinkList.travel()
    doubleLinkList.remove(400)
    doubleLinkList.travel()
    doubleLinkList.remove(1000)
    doubleLinkList.travel()
    print("链表的长度：",doubleLinkList.length())
    print("查找节点22",doubleLinkList.search(22))
    print("查找节点111",doubleLinkList.search(111))
