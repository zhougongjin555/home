# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2021/12/21
# @Author  : 周公瑾
# @File    : 多线程.py
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-

import threading
import random
import time
from concurrent.futures import ThreadPoolExecutor


'''
def handler(a):
    time.sleep(1)
    print(a)

t = threading.Thread(target=handler, args=(1,))
t.start()
# t.join()     # 测试阻塞和不阻塞的输出
print('done')




def handler(a):
    time.sleep(random.random())
    a = a+1
    return a

def done_func(res):
    print('200 ok')

li = []
with ThreadPoolExecutor(10) as t:
    for i in range(20):
        res = t.submit(handler, i)
        print(res.result())
        li.append(res.result())
        res.add_done_callback(done_func)
    t.shutdown()
print(li)
'''