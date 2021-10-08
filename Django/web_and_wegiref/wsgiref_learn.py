''':cvar
wsgiref模块的功能:
1、把字符串转换为字典格式或者path等其他方便拿取的数据格式
    (按照HTTP协议解析数据)

2、发送数据的时候自动加上响应头，组装成浏览器呢能够识别的响应报文格式
    (按照HTTP协议封装数据)
'''


from wsgiref.simple_server import make_server

# 必建函数


def application(environ, start_response):
    # 按照HTTP协议解析数据：environ
    # 按照HTTP协议封装数据：start_response
    # print(environ)
    # print(start_response)

    # 获取当前请求路径
    path = environ.get('PATH_INFO')
    print('PATH:', path)

    start_response('200 OK', [])
    return [b'<h1>hello world</h1>']   # 注意此处要求列表格式,一定要加 b ，不然报错


sock = make_server('127.0.0.1', 8001, application)  # 封装socket

# 等待用户连接
sock.serve_forever()

