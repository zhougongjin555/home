import socket


############智障客服######################################
# # 监听IP和端口
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('127.0.0.1', 8001)) # 绑定本机ip
# sock.listen(5)
#
# while True:
#     # 等待链接
#     conn, addr = sock.accept()
#     print('有人试图链接')
#
#     # 连接成功后返回信息
#     conn.sendall("欢迎使用xx系统，请输入您想要办理的业务！".encode("utf-8"))
#
#     while True:
#         # 等待客户发信息，如果客户端关闭了链接，默认返回一个空值
#         data = conn.recv(1024)
#         if not data:  # 捕获空值
#             break
#         data_str = data.decode('utf-8')
#
#         # 返回消息
#         conn.sendall(f'你发送的消息是{data_str}'.encode('utf-8'))
#
#     print('断开连接')
#     # 关闭连接
#     conn.close()
#
# # 关闭服务器
# sock.close()

######################################################################



#
# # ##############文件上传
# sock = socket.socket(socket.AF_INET, socket.SOCK_LIST)
# sock.bind(('127.0.0.1',8001))
# sock.listen(5)
#
#
# conn,addr = sock.accept()
#
# # 接收文件
# data = conn.recv(1024)
# total_file_size = int(data.decode('utf-8'))
#
# # 接收文件内容
# file_object = open('xxx.png', mode='wb')
# recv_size = 0
# while True:
#     # 每次最多接收1024字节
#     data = conn.recv(1024)
#     file_object.write(data)
#     file_object.flush()
#
#     recv_size += len(data)
#     # 上传完成
#     if recv_size == total_file_size:
#         break
#
# # 接收完毕，关闭连接
# conn.close()
# sock.close()
#
#



# # UDP协议
# import socket
#
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind(('127.0.0.1', 8002))
#
# while True:
#     data, (host, port) = server.recvfrom(1024) # 阻塞
#     print(data, host, port)
#     server.sendto("好的".encode('utf-8'), (host, port))


 # TCP协议
#
# import socket
#
# # 1.监听本机的IP和端口
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('127.0.0.1', 8001))
# sock.listen(5)
#
# while True:
#     # 2.等待，有人来连接（阻塞）
#     conn, addr = sock.accept()
#
#     # 3.等待，连接者发送消息（阻塞）
#     client_data = conn.recv(1024)
#     print(client_data)
#
#     # 4.给连接者回复消息
#     conn.sendall(b"hello world")
#
#     # 5.关闭连接
#     conn.close()
#
# # 6.停止服务端程序
# sock.close()





######################### 并发，非阻塞，io多路复用
import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 采用非阻塞形式运行
sock.setblocking(False)
sock.bind(('127.0.0.1', 8001))  # 绑定主机
sock.listen(5)

inputs = [sock, ]

while True:
    r, w, e = select.select(inputs, [], [], 0.05)
    for soc in r:
        if soc == sock:  # 判断一下传入的是连接还是数据包
            conn, addr = soc.accept()
            print('有新连接接入')
            inputs.append(conn)
        else:
            data = soc.recv(1024) # 接收数据
            if data:
                data = data.encode('utf-8')
                print('收到消息：', data)
                inputs.remove(soc)





