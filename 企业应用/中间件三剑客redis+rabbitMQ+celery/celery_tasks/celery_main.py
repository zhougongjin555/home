# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/29 14:26
# 文件名称： celery_main.py
# 文件地址： # 开发工具： PyCharm
# 开发功能：

import celery
import datetime
from celery.schedules import crontab

cel = celery.Celery(
    'celery_project',
    broker='redis://127.0.0.1:6379/1',
    backend='redis://127.0.0.1:6379/2',
    include=['task01',             # 指定任务文件
             'task02',
             'task03',
             ],
)


# 设置时区和是否使用UTC
cel.conf.timezone = 'Asia/Shanghai'
cel.conf.enable_utc = False

cel.conf.beat_schedule = {
    # 名字随意命名
    'add-every-10-seconds': {
        # 执行tasks1下的test_celery函数
        'task': 'task02.send_email',
        # 每隔2秒执行一次
        # 'schedule': 1.0,
        # 'schedule': crontab(minute="*/1"),
        'schedule': datetime.timedelta(seconds=6),
        # 传递参数
        'args': ('张三',)
    },
    # 'add-every-12-seconds': {
    #     'task': 'celery_tasks.task01.send_email',
    #     每年4月11号，8点42分执行
    #     'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     'args': ('张三',)
    # },
}

'''
启动 Beat 程序$ celery beat -A proj<br># Celery Beat进程会读取配置文件的内容，周期性的将配置中到期需要执行的任务发送给任务队列

之后启动 worker 进程.$ celery -A proj worker -l info 或者$ celery -B -A proj worker -l info
'''