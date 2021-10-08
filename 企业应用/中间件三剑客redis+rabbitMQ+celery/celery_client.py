# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/29 11:00
# 文件名称： celery_test.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能：

from celery_test import send_email
from datetime import datetime

# 定时任务
v1 = datetime(2021, 9, 29, 15, 00, 00)
v2 = datetime.utcfromtimestamp(v1.timestamp())

# 异步任务、函数通过delay传参数
# result = send_email.delay("周公瑾")
# print(result.id)
# 
# result2 = send_email.delay("诸葛亮")
# print(result2.id)

# 定时任务：
result = send_email.apply_async(args=['周公瑾'], eta=v2)
