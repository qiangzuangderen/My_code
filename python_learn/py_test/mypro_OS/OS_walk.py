#测试os.walk()遍历所有的子目录和子文件

import os

all_files = []                     #用于存放遍历的目录路径和文件名
path = os.getcwd()
list_files = os.walk(path)        #遍历工作目录下的所有目录和文件

for dirpath,dirnames,filenames in list_files:          #os.walk()方法返回三个参数，dirpath/dirnames/filenames
    #for dir in dirnames:
        #all_files.append(os.path.join(dirpath,dir))     #将文件目录装入all_files列表中
        #print(all_files)
    for filename in filenames:
        all_files.append(os.path.join(dirpath,filename))
        #print(all_files)

for f in all_files:
    with open(r"d:/python3/py_test/file/copy01.txt","a",encoding="utf-8") as pp:
        pp.writelines(f)