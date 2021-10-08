# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/28 16:39
# 文件名称： rabbitMQ_server.py
# 文件地址：
# 开发工具： PyCharm
# 开发功能： rabbitMQ学习

'''
学习日志：
0：教程博客: https://www.cnblogs.com/pyedu/p/11866829.html
1：rabbitmq安装方式： https://www.tqwba.com/x_d/jishu/290073.html

内容：
    1，简单模式：轮询分发，对于接收者一个一个的订阅
        可以设置手动应答，用速度换取准确接收
        可以设置持久化，防止MQ崩溃导致数据丢失

    2，交换机模式：一次性分发给所有的用户
        普通发布订阅模式: fanout
        关键字模式: direct
            设置关键字和通配符，实现消息过滤，让接收者只接收到自己感兴趣的数据
            # ：匹配多个单词
            * ：匹配一个单词

'''











# 简单模式（只能一个一个订阅）

import pika

# # 连接rabbitMQ
# conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = conn.channel()
#
# # 声明一个队列的名称
# channel.queue_declare(queue='hello')
# # 声明一个可持久化的队列，防止rabbitmq崩溃数据丢失
# channel.queue_declare(queue='hello2', durable=True)
#
#
# # 向指定队列中插入参数
# channel.basic_publish(
#     exchange='',
#     routing_key='hello',
#     body=b"Hello zhougongjin")
#
# channel.basic_publish(
#     exchange='',
#     routing_key='hello2',
#     body=b"Hello,zhougongjin,wonengchijiuhua",
#     properties=pika.BasicProperties(
#         delivery_mode=2,   #
#     ))


# 交换机模式（支持同时订阅数据）
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

# 声明一个交换机
channel.exchange_declare(exchange='logs', exchange_type='fanout')  # fanout:发布订阅模式
channel.exchange_declare(exchange='logs2', exchange_type='direct')  # direct:关键字模式

message = b'hello wa world'
channel.basic_publish(exchange='logs', routing_key='', body=message)

message1 = b'info: hello wa world'
channel.basic_publish(exchange='logs2', routing_key='info', body=message1)


print(" [x] Sent %r" % message)
conn.close()