
#enumerate()方法的作用，将列表中的元素加上索引，以元组的形式返回

with open(r"d:/python3/py_test/file/write.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    aa = enumerate(lines)
    print(list(aa))
    #读取列表中元素的两个值（索引，值），重新排列，索引排在前（从1开始计数），值排在后
    lines = ["0" + str(index+1) + line.rstrip() + "\n" for index,line in enumerate(lines)] 

with open(r"d:/python3/py_test/file/write01.txt","a",encoding="utf-8") as a:
    a.writelines(lines)