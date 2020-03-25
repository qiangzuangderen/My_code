#测试文件关闭流程，异常机制下管理文件操作的关闭流程

try:
    f = open(r"d:/python3/py_test/file/write01.txt","a",encoding="utf-8")
    s = ["小明\n","胖子\n","呆瓜\n"]
    f.writelines(s)
except BaseException as e:
    print(e)
finally:
    f.close()