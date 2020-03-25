#测试CSV文件操作

import csv

with open(r"d:/python3/py_test/file/mytest.csv","r") as f:
    a_csv = csv.reader(f)            #csv文件读取后，内容以列表形式返回
    for i in a_csv:
        print(i)
with open(r"d:/python3/py_test/file/mytest.csv","w") as f:
    c_csv = csv.writer(f)                                         #养成习惯，方法赋予对象，方便操作
    b_csv = [["5","cheng","4","6666"],["6","cheng","7","6677"]]   #写入csv文件的数据以列表形式写入
    c_csv.writerows(b_csv)