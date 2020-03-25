#拷贝二进制文件流程：（1）逐行读文件；(2)创建新文件（3）逐行写文件
#write()和writelines()的区别：(1)write()传入的格式为字符串；(2)writelines()传入的为字符序列

with open(r"d:/python3/py_test/file/aaa.jfif","rb") as f:
    with open(r"d:/python3/py_test/file/aaa_copy.jfif","wb") as b:
        for line in f.readlines():
            b.write(line)

print("拷贝完成…………")