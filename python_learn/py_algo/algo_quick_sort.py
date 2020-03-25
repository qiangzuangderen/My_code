#快速排序，最优时间复杂度O(f(n))=nlogn,最坏时间复杂度O(f(n))=n**2,当达到最坏时间复杂度，数列为有序数列，稳定性：不稳定
"""
算法思想：
1.设定一个基准值，一般是数列的第一个数；
2.设定起始点和终点，起点一般设置为基准值所在的索引值，终点一般设置为数列的最后一个索引值；
3.从终点的索引值开始向左，当起点值索引小于终点值索引并且终点值大于等于基准值，起点值与终点值交换位置；
4.从起点的索引值向右移动，当起点值索引小于终点值索引并且起点值小于基准值，终点值与起点值交换位置；
5.当终点的索引与起点的索引重合，将基准值放入重合位置；
6.此时比基准值小的在左边，比基准值大的在右边，生成两个子序列；
7.相同方法排序子序列，退出。
"""

def quick_sort(alist,start,end):

    #递归退出条件，当起点与终点重合
    if start >= end:
        return

    mid = alist[start]
    low = start
    high = end

    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid

    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)

if __name__ == "__main__":
    alist = [22, 32, 1, 2, 56, 7, 3, 99, 14]
    print("原数组：", alist)
    quick_sort(alist,0,len(alist)-1)
    print("排序后的数列：", alist)

