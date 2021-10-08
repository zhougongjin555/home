# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/28 16:39
# 文件名称： rabbitMQ_server.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能： rabbitMQ学习


import pika


# 简单模式
#
# # 连接rabbitMQ
# conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = conn.channel()
#
# # 声明一个队列的名称，防止此程序先运行，导致dui列还未创建的报错
# channel.queue_declare(queue='hello')
#
# # 确定回调函数
# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)
#     ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动应答设置
#
# # 确定监听队列
# # channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)  # 默认应答，可能出现数据丢失
# channel.basic_consume(queue='hello', auto_ack=False, on_message_callback=callback)  # 手动应答
#
#
# print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()  # 开始监听


# 交换机模式

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

# channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.exchange_declare(exchange='logs', exchange_type='direct')


# 创建队列，使用系统自动创建的唯一的名字
result = channel.queue_declare("", exclusive=True)
queue_name = result.method.queue

# channel.queue_bind(exchange='logs', queue=queue_name) # 普通交换机

# 可以绑定多个关键字
channel.queue_bind(exchange='logs', queue=queue_name, routing_key='error') # 交换机之关键字
channel.queue_bind(exchange='logs', queue=queue_name, routing_key='info') # 交换机之关键字
''' 还可以使用通配符的模式：
    # ：匹配多个单词
    * ：匹配一个单词
'''

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()


