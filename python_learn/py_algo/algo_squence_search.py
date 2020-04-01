#顺序查找

def squence_search(alist,v):
    for i in range(len(alist)):
        if alist[i] == v:
            return i
    #没找到指定对象，函数的出口
    return -1

if __name__ == "__main__":
    alist = [33,4,55,34,2,46,9,24]
    index = squence_search(alist,9)
    if index != -1:
        print("9在列表中的索引为：",index)
    else:
        print("9不在列表中")