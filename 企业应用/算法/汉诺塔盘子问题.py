# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/11 13:23
# 文件名称： 汉诺塔盘子问题.py
# 文件地址：
# 开发工具： PyCharm
# 开发功能：


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print('moving from %s to %s' % (a, c))
        hanoi(n - 1, b, a, c)

hanoi(6, 'A', 'B', 'C')
