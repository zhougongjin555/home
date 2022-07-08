# hailstone

# 算法有穷性探讨
def hailstone(n):
    res = [n]
    while n > 1:
        n = 3*n+1 if n % 2 else n/2
        res.append(int(n))
    return res
# print(hailstone(100))


# 冒泡
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return li
    return li
# print(bubble_sort([1,3,2,7,4,6,10,5]))


def fibo(n):
    li = [0, 1]
    if n < 2:
        return li[n-1]
    while n-2 > 0:
        li.append(li[-1] + li[-2])
        n -= 1
    return li[-1]
# print(fibo(100))


# 中缀表达转后缀表达
def mySplit(str):
    li = list(str)
    tmp, res = [], []
    for i in range(len(li) - 1):
        if li[i].isdigit():
            tmp.append(li[i])
        else:
            res.append("".join(tmp))
            res.append(li[i])
            tmp = []
    res.append("".join(tmp))
    return res


def toStr(n, base):
    # 进制转换
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]

print(toStr(1235612345, 16))


