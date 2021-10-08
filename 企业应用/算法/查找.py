# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/11 13:39
# 文件名称： 查找.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能：

from cal_time import timer


@timer
def linear_search(li, target):
    for index, val in enumerate(li):
        if val == target:
            return index
    return -1


@timer
def binary_search(li, target):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (right + left) // 2
        if li[mid] == target:
            return mid
        if li[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


params = (range(100), 32)
linear_search(*params)
binary_search(*params)
del params