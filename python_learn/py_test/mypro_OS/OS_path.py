#测试os.path模块

import os
import os.path

###################判断是否绝对路径、是否目录、是否文件、文件是否存在#################
print(os.path.isabs(r"d:/python3/py_test/file/pp.txt"))
print(os.path.isdir(r"d:/python3/py_test/file"))
print(os.path.isfile(r"d:/python3/py_test/file/pp.txt"))
print(os.path.exists(r"d:/python3/py_test/file/pp.txt"))

##################获取文件基本信息##########################
print(os.path.getsize(r"d:/python3/py_test/file/pp.txt"))
print(os.path.abspath("pp.txt"))
print(os.path.dirname(r"d:/python3/py_test/file/pp.txt"))
print(os.path.getctime(r"d:/python3/py_test/file/pp.txt"))

#################对路径的操作###############################
path = os.path.abspath("pp.txt")
print(os.path.split(path))         #打印文件的绝对路径，返回元组("文件绝对路径","文件名")
print(os.path.splitext(path))      #打印文件的绝对路径，返回元组("文件绝对路径/文件名","文件类型")
print(os.path.join("aa","bb","cc"))   #以路径标识符"/"连接字符串