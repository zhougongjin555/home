# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/29 11:00
# 文件名称： celery_test.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能：

'''
博客地址：https://www.cnblogs.com/pyedu/p/12461819.html
异步任务 和 定时任务

不要直接运行，在终端用命令行的方式启动文件

celery V5之上的版本堆windows不再支持
所以安装
    pip install celery==4.4.7
同时为了防止执行函数后报错，要安装eventlet
    pip install eventlet

celery worker -A celery_test -l info -P eventlet

'''


import time
import celery
from datetime import datetime


backend = 'redis://127.0.0.1:6379/1'   # 存储结果的数据库
broker = 'redis://127.0.0.1:6379/2'    # 数据库中间件
cel = celery.Celery('test', backend=backend, broker=broker)

@cel.task
def send_email(name):
    print(f'发送邮件给{name}')
    time.sleep(5)
    print('发送完成')
    return "ok"


