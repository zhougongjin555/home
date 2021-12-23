# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/11 14:00
# 文件名称： cal_time.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能：


import timeit


def timer(function):
    def inner(*args, **kwargs):
        start = timeit.default_timer()
        result = function(*args, **kwargs)
        end = timeit.default_timer()
        name = function.__name__
        print(f'函数{name}共使用时间 {end - start} secs')
        return result
    return inner