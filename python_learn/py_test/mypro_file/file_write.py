#测试file写文件
#coding=UTF-8

f = open(r"d:/python3/py_test/file/write01.txt","w",encoding="UTF-8")    #创建文件的同时启动操作系统IO，windows默认字符为"GBK"，python本身默认为UTF-8,会形成乱码
f.write("节日快乐\n今天是年初一\n")
f.close()