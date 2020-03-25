#函数嵌套

def printName(isChinaese,Name,familyName):
    def inner_print(a,b):               #函数封装
        print("{0}{1}".format(a,b))

    if isChinaese:
        inner_print(familyName,Name)
    else:
        inner_print(Name,familyName)

printName(True,"语棋","杨")
printName(False,"fork","Tom")