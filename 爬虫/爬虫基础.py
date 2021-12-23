# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2021/12/15
# @Author  : 周公瑾
# @File    : 爬虫基础.py
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-


import requests
from pprint import pprint


url = 'https://www.baidu.com'
res = requests.get(url)
pprint(res.text)

with open('baidu.txt', encoding='utf-8', mode='w') as f:
    f.write(res.text)
