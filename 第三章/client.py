import socket



 # ###################智障客服#################################
# # 1. 向指定IP发送连接请求
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 8001))
#
# # 2.连接成功后，获取系统登录信息
# message = client.recv(1024)
# print(message.decode("utf-8"))
#
# while True:
#     content = input("请输入(q/Q退出)：")
#     if content.upper() == 'Q':
#         break
#     client.sendall(content.encode("utf-8"))
#
#     # 3. 等待，消息的回复
#     reply = client.recv(1024)
#     print(reply.decode("utf-8"))
#
# # 关闭连接，关闭连接时会向服务端发送空数据。
# client.close()
###########################################################





# ##############文件上传
# import time
# import os
# import socket
#
# client = socket.socket()
# client.connect(('127.0.0.1', 8001))
#
# file_path = input("请输入要上传的文件：")
#
# # 先发送文件大小
# file_size = os.stat(file_path).st_size
# client.sendall(str(file_size).encode('utf-8'))
#
# print("准备...")
# time.sleep(2)
# print("开始上传..")
# file_object = open(file_path, mode='rb')
# read_size = 0
# while True:
#     chunk = file_object.read(1024) # 每次读取1024字节
#     client.sendall(chunk)
#     read_size += len(chunk)
#     if read_size == file_size:
#         break
#
# client.close()
#
#  # UDP 协议
# import socket
#
# client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# while True:
#     text = input("请输入要发送的内容：")
#     if text.upper() == 'Q':
#         break
#     client.sendto(text.encode('utf-8'), ('127.0.0.1', 8002))
#     data, (host, port) = client.recvfrom(1024)
#     print(data.decode('utf-8'))
#
# client.close()
#
#
#
#
#
#
# # TCP 协议
# import socket
#
# # 1. 向指定IP发送连接请求
# client = socket.socket()
# client.connect(('127.0.0.1', 8001))
#
# # 2. 连接成功之后，发送消息
# client.sendall(b'hello')
#
# # 3. 等待，消息的回复（阻塞）
# reply = client.recv(1024)
# print(reply)
#
# # 4. 关闭连接
# client.close()
#
#


######################### 并发，非阻塞，io多路复用

