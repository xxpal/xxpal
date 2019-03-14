# ===============================================================================
# product: WoniuTalk（客户端）
# version: 1.2
# author: Leo
# updated: 02/20/2019
#
# 基本要求：
# 信息的接收与发送           ==> Done
# 多线程实现                ==> Done
# 群聊和私聊                ==> TBD
# ===============================================================================
import socket
import threading


class WoniuTalkClient:
    def __init__(self):
        self.client = socket.socket()   # 实例化socket对象

    def connect_server(self, ip, port):
        # 1. 建立与服务器端的连接
        # 2. 发送数据
        # 3. 关闭连接
        self.client.connect((ip, port))
        threading.Thread(target=self.send_message).start()
        threading.Thread(target=self.receive_message).start()

    def send_message(self):
        while True:
            msg_to_server = input("请输入您要发送的消息：\n")
            self.client.send(msg_to_server.encode())   # 将一个字符串以特定的编码格式进行编码，默认是utf-8

    def receive_message(self):
        while True:
            msg_from_server = self.client.recv(1024).decode()  # 接收来自服务器端的消息
            print(msg_from_server)

    def __del__(self):
        self.client.close()


if __name__ == '__main__':
    server_ip = '19.19.19.251'
    server_port = 7777
    talk_client = WoniuTalkClient()
    talk_client.connect_server(server_ip, server_port)
