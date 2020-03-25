#coding=UTF-8

import time

time1 = time.time()
a = ' '
for i in range(1000000):
    a += 'sxt'
time2 = time.time()

t = time2-time1
print('time is ' + str(t))