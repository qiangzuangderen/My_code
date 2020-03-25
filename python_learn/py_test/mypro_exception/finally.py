#测试finally

try:
    f = open("d:/aa.txt","r")
    content = f.readline()
except:
    print("文件未找到")
finally:
    print("执行finally,关闭资源")
    try:
        f.close()                         #当文件未找到时，“关闭”动作也形成异常。
    except BaseException as e:
        print(e)
print("程序结束")
