#测试返回值‘return’

def add(a,b):
    print("计算两个数的和：{0},{1},{2}".format(a,b,a+b))
    return a+b     #return: 1、返回a+b的值；2、结束函数的执行，之后的语句不执行。
    print("完成计算")

def mult(x,y,z):
    #函数返回多个值
    return [x*3,y*4,z*5]

print(add(40,50))
print(mult(3,4,5))