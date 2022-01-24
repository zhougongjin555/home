# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2021/12/22
# @Author  : 周公瑾
# @File    : test.py
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-

def handler(num):
    li = []
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            li.append('FizzBuzz')
        elif i % 3 == 0:
            li.append('Fizz')
        elif i % 5 == 0:
            li.append('Buzz')
        else:
            li.append(i)
    return li

lis = handler(100)
print(lis)


