#插入排序,最坏时间复杂度：O(f(n))=n**2,最优时间复杂度：O(f(n))=n,稳定性：稳定

def insert_sort(alist):
    n = len(alist)
    """确定索引alist[i]"""
    for i in range(1,n):
        while i>0:
            """以列表中第一个数为有序数列，下一个跟前一个做比较，比它小交换位置，比它大保持位置不变"""
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
            else:
                break
            i -= 1

if __name__ == "__main__":
    alist = alist = [22,32,1,2,56,7,3,99,14]
    print("原数组：",alist)
    insert_sort(alist)
    print("排序后的数列：",alist)