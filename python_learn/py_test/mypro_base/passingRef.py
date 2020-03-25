#coding=UTF-8

def eggs(someParameter):
    someParameter.append('hello')

spam = [1,2,3]
eggs(spam)
print(spam)