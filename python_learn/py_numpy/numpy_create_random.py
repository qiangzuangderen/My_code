#测试numpy随机建立数组
import numpy as np
"""np.random()方法返回的是[0.0,1)区间的随机数,size为确定数组的维度"""

"""创建一维数组"""
a = np.random.random(size=3)
print(a)

"""创建二维数组"""
b = np.random.random(size=(4,5))         #四行五列
print(b)

"""创建三维数组"""
c = np.random.random(size=(4,5,6))
print(c)

"""创建随机整数一维数组,randint()方法,参数：取值范围（low，high），取值数量、维度（size=）"""
def randomintTest():
    d = np.random.randint(1,6,size=10)
    print(d)
    """创建随机整数二维数组，参数：取值范围(low,high),取值数量size=(行，列)"""
    e = np.random.randint(5,12,size=(3,4))
    print(e)
    """创建随机整数三维数组"""
    f = np.random.randint(5,12,size=(3,4,5))
    print(f)

randomintTest()