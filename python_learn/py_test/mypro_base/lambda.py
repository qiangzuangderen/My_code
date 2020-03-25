#lambda表达式

f = lambda a,b,c:a*b*c
print(f(3,4,5))

#序列的调用方法
g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]
print(g[0](3),g[1](4),g[2](5))