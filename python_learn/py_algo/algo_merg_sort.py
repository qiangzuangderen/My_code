#归并排序

"""
算法思想：
1.以数列中点的索引为基准，将排序的列表分解到以单个数为单位；
2.创建目标数列；
3.将单个数列合并，小的放前面，大的放后面，左右两个数列第一个索引为指针，逐个对比，小的数添加到目标数列中；
4.比较一次，取数后的列表指针向右一格；
5.比较结束后，将剩余的数添加到目标数列中，返回目标数列。
"""
def merg_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    left_list = merg_sort(alist[0:mid])
    right_list = merg_sort(alist[mid:])

    result = []
    left_list_pointer,right_list_pointer = 0,0
    while left_list_pointer < len(left_list) and right_list_pointer < len(right_list):
        if left_list[left_list_pointer] < right_list[right_list_pointer]:
            result.append(left_list[left_list_pointer])
            left_list_pointer += 1
        else:
            result.append(right_list[right_list_pointer])
            right_list_pointer += 1

    result += left_list[left_list_pointer:]
    result += right_list[right_list_pointer:]
    return result

if __name__ == "__main__":
    alist = [22, 32, 1, 2, 56, 7, 3, 14]
    print("原数组：", alist)
    result_list = merg_sort(alist)
    print("排序后的数列：", result_list)

