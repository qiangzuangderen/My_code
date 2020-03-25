#简单枚举
"""
求所有满足：a+b+c=1000且a**2+b**2=c**2中,a,b,c可能的组合。
"""
"""
算法的五个特征：
1.输入性：有零个或多个外部变量作为算法的输入；
2.输出性：算法至少有一个量作为输出；
3.确定性：算法中每条指令清晰，无歧义；
4.有穷性：算法中每条指令执行的次数有限，执行时间有限；
5.可行性：算法原则上能够精确运行，人为经笔算有限次运算后即可完成。
"""
import time

start_time = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000-a-b
        if a**2+b**2==c**2:
            print("a={0},b={1},c={2}".format(a,b,c))
end_time = time.time()
print("use time:{0}".format(end_time-start_time))