#测试文件的读方式

with open(r"d:/python3/py_test/file/write01.txt","r",encoding="utf-8") as f:
    while True:
        str = f.readline()
        if not str:
            break
        else:
            print(str,end="")