#测试traceback模块

import traceback
import os

try:
    print("step1")
    num = 1/0
except:
    with open("d:/python3/py_test/file/pp.txt","w") as f:
        traceback.print_exc(file=f)
        os.remove(r"d:/python3/pp.txt")
        