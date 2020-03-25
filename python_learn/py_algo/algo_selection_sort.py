#选择排序,对象是列表的索引,最优时间复杂度O(f(n))=n**2,最坏时间复杂度O(f(n))=n**2,稳定性：不稳定（完全改变原有顺序）

def selection_sort(alist):
    n = len(alist)
    """确定剩余列表中最小值的索引"""
    for i in range(n-1):
        min_index = i
        """找出最小值并定义它的索引"""
        for j in range(i+1,n):
            if alist[min_index] > alist[j]:
                min_index = j
        """将找出的最小值放到当前的索引位置上，如果最小值在当前位置就不需要交换"""
        if min_index != i:
            alist[i],alist[min_index] = alist[min_index],alist[i]

alist = [22,32,1,2,56,7,3,99,14]
print("原数组：",alist)
selection_sort(alist)
print("排序后的列表：",alist)