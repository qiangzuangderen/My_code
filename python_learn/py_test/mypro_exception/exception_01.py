#测试0做除数的异常
'''
print("step0:")
try:
    print("step1:")
    a = 3 / 4
    print("step2:")
except BaseException as e:
    print("step3:")
    print("0不能做除数")
    print(e)
    print(type(e))
print("step4:")
print("end…………")
'''

while True:
    try:
        a = int(input("请输入一个数字："))
        print("输入的数字为：",a)
        if a == 88:
            print("程序退出")
            break
    except BaseException as e:
        print(e)
        print("输入的不是数字")

print("程序结束。")

try:
    a = input("请输入被除数：")
    b = input("请输入除数：")
    c = float(a) / float(b)
except BaseException as e:
    print(e)
else:
    print(c)
finally:
    print("try……except后必须执行finally，释放try申请的资源")

print("程序结束。")

#print(BaseException.mro())