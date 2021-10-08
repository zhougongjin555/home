# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/15 9:01
# 文件名称： text.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能：


import requests
from lxml import etree

url = 'https://tushare.pro/document/2?doc_id=87'
resp = requests.get(url)

tree = etree.HTML(resp.text)
code_list = tree.xpath('/html/body/div[1]/section/div/div/div/table[3]/tbody')
for code in code_list:
    ts_code = code.xpath('./tr/td[1]/text()')
    print(ts_code)
