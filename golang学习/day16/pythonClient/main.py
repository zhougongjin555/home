import socket
import json

request = {
    "id": 0,
    "params": [{"X": 3.0, "Y": 4.0}],
    "method": "ServiceA.Square"
}

# create_connection 会创建一个连接到TCP服务器的对象
client = socket.create_connection(("127.0.0.1", 9999), 3)  # 前一个参数元组为urk&端口，后一个参数为超时时间（s）
client.sendall(json.dumps(request).encode())
print(json.dumps(request).encode())

resp = client.recv(1024)
resp = json.loads(resp.decode())
print("得到微服务返回值： ", resp)
