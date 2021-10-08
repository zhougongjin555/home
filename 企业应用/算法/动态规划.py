# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/16 14:13
# 文件名称： 动态规划.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能：


#  斐波那契数列
def fibnacci(n):
    '''
    递归
    :param n:
    :return:
    '''
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


# 动态规划（DP）思想 = 最优子结构（递推式） + 评估子问题
def fibnacci_no_recurision(n):
    """
    非递归
    :param n:
    :return:
    """
    f = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


# print(fibnacci(10))
# print(fibnacci_no_recurision(100))


#  钢条切割问题
def cut_iron(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_iron(p, i) + cut_iron(p, n-i))
        return res

def cut_iron_2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i] + cut_iron_2(p, n-i))
        return res


def cut_iron_3(p, n):
    r, s, fs = [0], [0], []
    for i in range(1, n+1):
        res_r = 0  # 价格最优值
        res_s = 0  # 最优价格的切割的左边值，比如，9=2+7，保留2
        for j in range(1, i+1):
            if res_r < p[j] + r[i-j]:
                res_r = p[j] + r[i-j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    tmp = n - s[n]
    fs.append(s[n])
    while tmp != 0:
        fs.append(s[tmp])
        tmp = tmp - s[tmp]
    return r[n], s, fs


# p = [0,1,5,8,9,10,17,17,20,24,30,32,35,42,55,56,57]
# print(cut_iron_3(p, 5))


# 最长公共子序列
def lcs_length(x, y):
    m, n = len(x), len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]


def lcs(x, y):
    m, n = len(x), len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    p = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 0,1,2分别代表左·斜·上三个方向
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                p[i][j] = '↖'
            else:
                if c[i-1][j] >= c[i][j-1]:   # 等与不等结果两个值，都对
                    c[i][j] = c[i-1][j]
                    p[i][j] = '👆'
                else:
                    c[i][j] = c[i][j - 1]
                    p[i][j] = '👈'
    for _ in c:
        print(_)
    print('------------------------------------')
    for _ in p:
        print(_)
    print('------------------------------------')
    print(c[m][n], lcs_traceback(x, p))


def lcs_traceback(x, p):
    j = len(p[0])-1
    i = len(p)-1
    res = []
    while i > 0 and j > 0:
        if p[i][j] == '↖':
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif p[i][j] == '👆':
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(res))


# lcs('abcbdab', 'bdcaba')





#  最大公约数

def gcd(a, b):
    c = a % b
    if not c:
        return b
    else:
        return gcd(b, c)

print(gcd(100, 24))