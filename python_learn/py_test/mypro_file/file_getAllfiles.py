#递归方法打印目录下所有文件
#思路：(1)确定指定路径下的目录和文件；(2)合并指定路径下的目录和文件名；(3)当指定路径下的文件存在，递归遍历

import os

all_files = []

def GetAllfiles(path,level):
    childfiles = os.listdir(path)                  #确定指定路径下的所有目录和文件
    for file in childfiles:
        filepath = os.path.join(path,file)         #合并指定路径下的目录和文件名
        if os.path.isdir(filepath):                #确定filepath路径下文件存在
            GetAllfiles(filepath,level+1)
        all_files.append("-"*level+filepath)       #将遍历的文件目录和文件写入all_files列表中

GetAllfiles(r"d:/python3/py_test",0)
for f in reversed(all_files):                      #遍历并倒序排列列表
    print(f)
