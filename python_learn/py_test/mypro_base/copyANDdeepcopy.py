
#浅拷贝与深拷贝
import copy

a = [10,20,[5,6,7]]
def func_Copy():
    #-------浅拷贝---------
    a = [10,20,[5,6,7]]
    b = copy.copy(a)       #b为浅拷贝，只拷贝父对象a，不拷贝子对象a[0],a[1],a[2]
    b.append(30)           #b增加子对象b[3]=30,与a无关
    b[2].append(8)         #b[2]指向a[2]即id(b[2])=id(a[2]),b[2]增加子对象8，等同于a[2]增加子对象8
    print(a)
    print(b)

    #--------深拷贝---------

    c = copy.deepcopy(a)   #c为深拷贝，即完全拷贝对象a的所有内容，包含子对象
    c.append(30)           #拷贝后c不在指向a的任何子对象
    c[2].append(8)         #对象c做任何变化与a无关
    print(a)
    print(c)

func_Copy()

