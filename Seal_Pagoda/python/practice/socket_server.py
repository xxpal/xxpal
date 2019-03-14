# 文件名：socket_server.py

# 导入socket、sys模块
import socket
import sys


# 创建socket对象
# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server = socket.socket()

# 获取本地主机名
host = socket.gethostname()
# 设置端口号
port = 9999

# 绑定端口号
socket_server.bind((host, port))

# 设置最大连接数，超过后排队
socket_server.listen(5)

while True:
    # 建立客户端连接, 等待连接的到来
    # accept() -> (socket object, address info)
    socket_client, addr = socket_server.accept()

    print('终于等到你——%s，还好我没放弃！' % str(addr))

    # 服务端给连接上来的客户端发送消息
    msg = '我的世界从此以后多了一个你——%s' % str(addr) + '\r\n'
    socket_client.send(msg.encode('utf-8'))
    socket_client.close()
