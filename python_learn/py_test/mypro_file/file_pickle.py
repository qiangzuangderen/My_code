#测试pickle模块，用于文件读写序列化，先写再读，写和读的格式须相同

import pickle

a1 = "yang"
a2 = 333
a3 = [33,44,55,66]

with open(r"d:/python3/py_test/file/data.dat","wb") as f:    #打开文件，确定读写方式，确定文件对象
    pickle.dump(a1,f)                                        #写数据
    pickle.dump(a2,f)
    pickle.dump(a3,f)

with open(r"d:/python3/py_test/file/data.dat","rb") as f:
    b1 = pickle.load(f)                                      #读数据
    b2 = pickle.load(f)
    b3 = pickle.load(f)
    print(b1);print(b2);print(b3)

print(id(a1));print(id(b1))