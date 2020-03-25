#递归函数计算阶乘

def factiorial(n):
    if n==1:
        return 1
    else:
        return n*factiorial(n-1)

for i in range(1,6):
    print(i,"!=",factiorial(i))