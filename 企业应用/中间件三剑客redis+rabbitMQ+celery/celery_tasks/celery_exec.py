# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/29 14:40
# 文件名称： celery_exec.py
# 文件地址： celery_tasks
# 开发工具： PyCharm
# 开发功能：


from task01 import send_hello
from task02 import send_email
from task03 import send_msg


result1 = send_hello.delay('周公瑾')
result2 = send_email.delay('诸葛亮')
result3 = send_msg.delay('关云长')
print(result1.id, result2.id, result3.id)
