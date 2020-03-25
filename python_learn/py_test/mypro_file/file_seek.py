#测试文件对象属性和指针操作

with open(r"d:/python3/py_test/file/write01.txt","r",encoding="utf-8") as f:
    print(f.name)        #打印文件名
    print(f.tell())      #打印当前指针位置
    print(f.readline())  #读取文件的一行
    print(f.tell())      #打印当前指针位置
    print(f.readline())  #按序读取文件第二行
    f.seek(2)           #从头偏移3个字节，文本文件只允许从头计算偏移量，"UTF-8"中汉子占3个字节，不能拆字，二进制读取方式可以指定位置计算偏移量
    print(f.tell())
    print(f.readline())
    