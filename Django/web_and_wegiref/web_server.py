import django
import socket


sock = socket.socket()
sock.bind(('127.0.0.1', 8001))
sock.listen(5)


while True:
    conn, attr = sock.accept()
    data = conn.recv(1024)
    print(data.decode()) #按照utf-8格式返回数据
    with open('F:\我的坚果云\markdown\前端代码\employers_new.html', mode='r', encoding='utf-8') as f:
        html = f.read()
    conn.sendall(('HTTP/1.1 200 OK \r\n\r\n' + html).encode('utf-8'))



