# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/29 14:27
# 文件名称： task01.py
# 文件地址： celery_tasks
# 开发工具： PyCharm
# 开发功能：

import time
from celery_main import cel

@cel.task
def send_hello(name):
    print(f"{name}, hello")
    time.sleep(3)
    print('hello发送完成')
    return '200 OK'





