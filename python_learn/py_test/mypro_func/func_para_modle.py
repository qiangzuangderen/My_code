#参数的模式

#位置参数
def test01(a,b,c):
    print(a,b,c)

#默认参数
def test02(d=11,e=22,f=33):
    print(d,e,f)


test01(3,4,5)
test02()
test01(b=55,c=77,a=88)   #命名参数