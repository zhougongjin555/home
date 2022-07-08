# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/11 14:07
# 文件名称： 排序.py
# 文件地址：
# 开发工具： PyCharm
# 开发功能：
import random
from cal_time import timer
import heapq

'''
# 1、冒泡排序法  O(n^2)
@timer
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return li
    return li


# 2，选择排序  O(n^2)
@timer
def selected_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
    return li


# 3，插入排序  O(n^2)
@timer
def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
    return li


################################################################

# 4，快速排序法        O(nlog(n))
# @timer
def quick_sort(li):
    if len(li) < 2:
        return li
    else:
        tmp = li[0]  # 随便取第一个值
        greater = [i for i in li[1:] if i > tmp]  # 所有大于首位的值
        less = [j for j in li[1:] if j <= tmp]  # 所有小于首位的值
        li = quick_sort(less) + [tmp] + quick_sort(greater)  # 递归 重组列表
        return li


@timer  # 可以防止递归函数被装饰器装饰后多次打印
def _quick_sort(li):
    quick_sort(li)


# 5，堆排序法      O(nlog(n))
def shit(li, low, high):
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j是左孩子   2*i+2是右孩子
    tmp = li[low]
    while j <= high:
        if j + 1 < high and li[j + 1] > li[j]:
            j = j + 1  # 如果右孩子更大，j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 向下一层
            j = 2 * i + 1
        else:
            break
    else:
        li[i] = tmp
    return li


@timer
def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        shit(li, i, n - 1)
    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        shit(li, 0, i - 1)


# 或者使用heapq模块
def heapq_mouble(li, n):
    heapq.heapify(li)
    for i in range(n):
        print(heapq.heappop(li), end=',')


# 堆的应用   topK问题
def sift(li, low, high):
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j是左孩子   2*i+2是右孩子
    tmp = li[low]
    while j <= high:
        if j + 1 < high and li[j + 1] < li[j]:
            j = j + 1  # 如果右孩子更大，j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j  # 向下一层
            j = 2 * i + 1
        else:
            break
    else:
        li[i] = tmp
    return li


@timer
def topK(li, k):
    heap = li[0:k]
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    # 1，建堆
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    # 2，遍历
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    print(heap)
    return heap


# 6，归并排序      O(nlog(n))
def merge(left, right):
    merged = []
    # 擂台比武，谁小谁进
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0)
        else:
            merged.append(right.pop(0))
    # 添加剩余的元素（eg: left 所有大于 right 最大值的元素）
    merged.append(right if right else left)
    return merged
            
def merge_sort(li):
    if len(li) <= 1:
        return li
    mid = len(li) // 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])
    merge(left, right)
    


##########################################################
# 7，希尔排序
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):  # i 表示摸到的牌的下标
        tmp = li[i]
        j = i - gap  # j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


@timer
def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


# 8，计数排序
@timer
def count_sort(li, max_num):
    count = [0 for i in range(max_num + 1)]
    for num in li:
        count[num] += 1
    i = 0
    for num, m in enumerate(count):
        for j in range(m):
            li[i] = num
    i += 1


# 9，桶排序
@timer
def bucket_sort(li, max_num, n=100):
    buckets = [[] for i in range(n)]  # 创建n个桶
    for var in li:
        i = min(var // (max_num // n), n - 1)
        buckets[i].append(var)
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li


# 10，基数排序
@timer
def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        # 先个位数排序入桶，然后十位数...
        buckets = [[] for _ in range(10)]
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)

        li.clear()
        for buc in buckets:
            li.extend(buc)

        it += 1
    return li





def li(n):
    data = [random.randint(1, 100000) for i in range(n)]
    return data

# bubble_sort(li(10000))         # 冒泡
# selected_sort(li(10000))       # 选择
# insert_sort(li(10000))         # 插入
# _quick_sort(li(10000))         # 快速
# heap_sort(li(10000))           # 堆排序
# heapq_mouble(li(10000), 10000)
# topK(li(10000), 10)            # topK
# merge_sort(li(10), 0, 9)       # 归并
# shell_sort(li(1000))           # 希尔
# count_sort(li(10000), 100000)  # 计数
# bucket_sort(li(10000), 100000)   # 桶排序
# radix_sort(li(10000))            # 基数
'''


# 冒泡排序
def bubble_sort(li):
    n = len(li)
    exchange = False
    for i in range(n):
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return li
    return li

lis = [1, 344, 5, 3, 42, 456, 4, 343, 4234]
res = bubble_sort(lis)
print(res, lis, id(res), id(lis))    # [1, 3, 4, 5, 42, 343, 344, 456, 4234]


from functools import reduce
def quick_sort(li):
    if len(li) < 2:
        return li
    num = li[0]
    greater = [i for i in li[1:] if i >= num]
    less = [i for i in li[1:] if i < num]
    li = quick_sort(less) + [num] + quick_sort(greater)
    return li

lis = [1, 344, 5, 3, 42, 456, 4, 343, 4234]
res = quick_sort(lis)
print(res, lis, id(res), id(lis))     # [1, 3, 4, 5, 42, 343, 344, 456, 4234]
