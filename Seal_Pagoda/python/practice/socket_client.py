# 导入socket、sys模块
import socket
import sys

# 创建socket对象
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于1024字节的数据
msg = s.recv(1024)

# 关闭连接
s.close()

# 打印输出从服务端接收的信息，默认就是utf-8
print(msg.decode('utf-8'))
