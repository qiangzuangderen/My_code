#单链表的实现
"""
链表的组成结构
1.链表块：数据item，指向下一个链表块的标识next
2.游标cur
3.长度计数器count
"""
class SingleNode(object):
    """单链表的节点"""
    def __init__(self,item):
        #item存放数据
        self.item = item
        #next是下一个节点的标识
        self.next = None

class SingleLinkList:
    #初始化链表
    def __init__(self,node=None):
        if node != None:
            HeadNode = SingleNode(node)
            #__head在单个链表中为私有属性
            self.__head = HeadNode
        else:
            self.__head = node

    """以下为链表操作的方法"""
    #1.判断列表是否为空
    def is_empty(self):
        #if self.__head == None:
        #     return True
        #else:
        #    return False
        return self.__head == None

    #2.计算链表的长度
    def length(self):
        #cur为游标，初始时指向头结点
        cur = self.__head
        #设置长度计数器
        count = 0
        while cur != None:
            count += 1
            #将cur后移一个节点
            cur = cur.next
        return count

    #3.遍历链表
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")

    #4.头部添加元素
    def add(self,item):
        #先创建一个保存item值的节点
        node = SingleNode(item)
        #将新节点的链接域next指向头结点，即__head指向的位置
        node.next = self.__head
        #将链表的头__head指向新节点
        self.__head = node

    #5.尾部添加元素
    def append(self,item):
        #将传入的值构造成节点
        node = SingleNode(item)
        if self.is_empty():  #单链表为空时，头结点为当前构造节点
            self.__head = node
        else:
            curNode = self.__head
            while curNode.next != None:
                curNode = curNode.next
            #修改节点指向，最后一个节点的next指向node
            curNode.next = node

    #6.指定位置插入元素
    def insert(self,pos,item):
        #若插入位置在第一个元素之前，执行头部插入
        if pos <= 0:
            self.add(item)
        #若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        #找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # 设置pre，用来指向pos的前一个位置pos-1,初始从头节点开始移动到指定位置
            pre = self.__head
            while count < (pos-1):
                count += 1
                pre = pre.next
            #先将新节点node的next指向插入位置的节点
            node.next = pre.next
            #将插入位置的前一个节点的next指向新节点
            pre.next = node

    #7.删除节点
    def remove(self,item):
        cur = self.__head
        pre = None
        while cur != None:
            #找到了制定元素
            if cur.item == item:
                #如果第一个就是要删除的节点
                if not pre:
                    #将头指针指向头结点的后一个节点
                    self.__head = cur.next
                else:
                    #将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                #继续按链表后移节点
                pre = cur
                cur = cur.next

    #8.查找节点是否存在,返回True或者False
    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == "__main__":
    #初始化元素值为20的单向链表
    #singleLinkList = SingleLinkList(20)
    #初始化一个空的单向链表
    singleLinkList = SingleLinkList()
    print("是否为空链表：",singleLinkList.is_empty())
    print("链表的长度为：",singleLinkList.length())
    print("---------遍历单链表----------")
    singleLinkList.travel()
    print("------------查找-------------")
    print(singleLinkList.search(20))
    print(singleLinkList.search(30))
    print("------------头部插入-----------")
    singleLinkList.add(11)
    singleLinkList.add(22)
    singleLinkList.add(33)
    singleLinkList.travel()
    print("------------尾部插入-----------")
    singleLinkList.append(66)
    singleLinkList.append(77)
    singleLinkList.append(88)
    singleLinkList.travel()
    print("链表的长度：",singleLinkList.length())
    print("----------指定位置插入----------")
    singleLinkList.insert(2,100)
    singleLinkList.travel()
    singleLinkList.insert(-1,200)
    singleLinkList.travel()
    singleLinkList.insert(10,300)
    singleLinkList.travel()
    print("---------删除节点-----------")
    singleLinkList.remove(100)
    singleLinkList.travel()
    singleLinkList.remove(200)
    singleLinkList.travel()
    singleLinkList.remove(300)
    singleLinkList.travel()



