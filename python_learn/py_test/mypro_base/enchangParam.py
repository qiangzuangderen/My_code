#可变参数

#*param,收集放入元组中

def test01(a,b,*c):
    print(a,b,c)

test01(3,4,5,6)

#**param，收集放入字典中

def test02(a,b,**c):
    print(a,b,c)

test02(3,4,name="yang",age=18)

#可变参数后面要加参数，必须强制命名

def test03(*c,a,b):
    print(c,a,b)

test03(3,a=4,b=5)