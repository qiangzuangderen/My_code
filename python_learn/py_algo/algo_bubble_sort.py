#冒泡排序，对象是列表的值，最坏时间复杂度：O(f(n))=n**2（无序数列），最优时间复杂度：n（有序数列），稳定性：稳定

def bubble_sort(alist):
    n=len(alist)
    for k in range(n):
        """n-1的目的为控制列表取值不超过列表的宽度，第一轮循环k目的为：每次将最大的数排到列表最后，下一次列表对象（列表宽度）自动-1，即n-1-k"""
        count = 0  #设置计数器count
        for i in range(n-1-k):
            """判断列表中相邻的两个值，取最大值交换位置，将最大值放到列表末尾"""
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                """如果计数器count +1，表示循环产生，传入的列表为无序列表"""
                count += 1
        """如果计数器count始终为零，表示没有产生循环，传入的列表为有序列表"""
        if count == 0:
            break

alist = [22,32,1,2,56,7,3,99,14]
print("原数组：",alist)
bubble_sort(alist)
print("排序后的数组：",alist)