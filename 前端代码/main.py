import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8001))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print('has data')
    data = conn.recv(1024)
    print(data.decode())
    with open('./HTML/index.html') as f:
        html = f.read()
    conn.sendall(('HTTP/1.1 200 OK \r\n\r\n'+html).encode('gbk'))
    conn.close()






