#eval()函数的用法，别忘了""

s = "print('abcde')"
eval(s) 

dict1 = dict(a=100,b=200)
c = eval('a+b',dict1)
print(c)
