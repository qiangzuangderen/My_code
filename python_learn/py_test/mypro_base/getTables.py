#coding=UTF-8

r1 = {'name':'yang','age':6,'salary':3000,'city':'beijing'}
r2 = {'name':'ling','age':18,'salary':2000,'city':'shanghai'}
r3 = {'name':'sun','age':16,'salary':1000,'city':'hangzhou'}

table = [r1,r2,r3]

for i in table:
    if i.get('salary')>1500:
        print(i)