import functools


def outer(origin):
    '''aaa'''
    @functools.wraps(origin)  # 被装饰器装饰后的函数都是inner，加上此处调用__name__就会指回原函数的名称以及注释信息了，
    def inner():
        print('inner')
        res = origin()
        print("after")
        return res
    return inner


@outer  # func = outer(func)
def func():
    '''bbb'''
    print("我是func函数")
    value = (11, 22, 33, 44)
    return value


func()

print(func.__name__) # 获取函数名称
print(func.__doc__) # 获取函数的内部的注释  （‘’‘特定格式’‘’）


# 嵌套函数内容


def fib(max_count):
    n1, n2 = 1, 1
    for i in range(max_count):
        yield n1
        n1 = n1 + n2
        n2 = n1 - n2

count = input("请输入要生成斐波那契数列的个数：")
count = int(count)
fib_generator = fib(count)
for num in fib_generator:
    print(num)

data_list = [11,22,33,"alex",455,'eirc']
new_data_list = [ i for i in data_list if str(i).isdecimal()] # 请在[]中补充代码实现。
print(new_data_list)

data_list = [11,22,33,"alex",455,'eirc']
# func = lambda i: i if type(i) == int else len(i)
new_data_list = [i+100 if type(i) == int else len(i) for i in data_list ] # 请在[]中补充代码实现。
print(new_data_list)

data_list = [
    (1,'alex',19),
    (2,'老男',84),
    (3,'老女',73)
]
info_data = {num: i for num, i in enumerate(data_list)}
print(info_data)

# pow max min enumerate abs sum all any round

import sys
print(sys.path)


from sklearn.preprocessing import MinMaxScaler
data = [[-1,15, 1], [-0.5, 3, 5], [-10, 8, -1], [1, 18, 2]]
scaler = MinMaxScaler()
print(scaler.fit(data))
print(scaler.transform(data))

import random
v = random.sample([11, 22, 33, 44, 55], 3)
print(v)


ctime = time.time() # 11213245345.123
v1 = datetime.fromtimestamp(ctime)
print(v1)


import re

text = "逗2B最逗3B欢乐"
data = re.finditer("(?P<xx>\dB)", text)  # 命名分组
for item in data:
    print(item.group())


import time
#  下载进度条演示视频
for i in range(1,101):
    x = '>' * i
    y = '-' * (100 - i)
    print(f'下载进度：\r{i}%    【{x + y}】', end='')
    time.sleep(0.1)



# 装饰器
def timer(func):
    def inner(*args,**kwargs):
        ss= time.time()
        res = func(*args,**kwargs)
        ee= time.time()
        print(f'test costs time:{ee-ss}s')
        return res
    return inner

@timer
def a():
    pass

class Message:

    def __init__(self, *args):
        self.data = data

    def a(self):
        pass

    def b(self):
        pass

mes = Message(11) # 执行类方法

