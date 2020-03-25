#!/usr/bin/env python3
#coding=UTF-8

yourname = 'flamingo'
name = ''
count = 0

while True:
    print('Please type your name:')
    name = input()
    if name == yourname:
        while True:
            print('Please input your password:')
            password = input()
            if password != 'qwe123':
                print('The password is wrong')
                count += 1
                if count == 3:
                    print('The password is input wrong 3 times')
                    break
            else:
                print('Good,password is right')
                break
        break
    
            
print('Thank you')
                