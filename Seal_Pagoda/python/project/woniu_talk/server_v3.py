# ===============================================================================
# product: WoniuTalk（服务端）
# version: 1.3
# author: Leo
# updated: 02/21/2019
#
# 基本要求：
# 信息的接收与发送           ==> Done
# 多线程实现                ==> Done
# 群聊和私聊                ==> Done
# ===============================================================================
import socket
import threading


class WoniuTalkServer:
    def __init__(self, ip, port):
        # 以二维列表的形式保存所有的客户端用户姓名和连接，如下格式：
        # [ ['leo', client_user1], ['steve', client_user2], ...]
        self.clients = []
        # 服务器接收消息：
        # 1、绑定一个确定的端口地址
        # 2、启动监听端口的进程
        # 3、准备接收信息
        # 4、当有信息时，接收它
        self.server = socket.socket()
        self.server.bind((ip, port))
        self.server.listen()
        print('服务器启动成功，欢迎来撩！')

    def accept_client(self):
        # while死循环，用于等待建立与客户端的通道，表示可以接受无数个。
        while True:
            client_user, address = self.server.accept()  # 等待新的连接通道的建立：阻塞
            welcome_msg = '[服务器回复]：欢迎来自%s的朋友，请输入您的姓名：' % str(address)
            client_user.send(welcome_msg.encode())
            user_name = client_user.recv(1024).decode()
            print('[服务器回复]：欢迎来自%s的朋友<%s>加入群聊！' % (str(address), user_name))

            # 将当前对话的用户名和client_user组成一个列表加入到clients列表中，构成了一个二维列表
            self.clients.append([user_name, client_user])

            # 群发消息给所有连接的客户端用户，告知有新用户加入
            for c in self.clients:
                c[1].send(('欢迎<%s>加入群聊！' % user_name).encode())

            threading.Thread(target=self.send_receive, args=(user_name, client_user, address)).start()

    def send_receive(self, user_name, client_user, address):
        try:
            while True:
                msg_from_client = client_user.recv(1024).decode()  # 接收来自客户端的消息
                print('来自%s的朋友<%s>说：' % (str(address), user_name) + msg_from_client)

                # 判断是群发还是私信
                if str(msg_from_client).startswith("@"):
                    msg_list = msg_from_client.split('##')   # 拆分消息，以空格为标识，将'@用户名'和'消息内容'存至列表
                    private_name = msg_list[0][1:]  # 获取用户姓名
                    private_msg = msg_list[1]       # 获取消息内容
                    private_client = self.search_for_client(private_name)
                    if private_client is not None:
                        private_client.send(('<%s>悄悄地对你说：%s' % (user_name, private_msg)).encode())
                    else:
                        client_user.send(('您私聊的用户<%s>不存在！' % private_name).encode())

                else:
                    msg_to_client = '<%s>说：%s' % (user_name, msg_from_client)  # 往客户端连接通道发消息
                    # 一旦收到一个客户端的消息，则群发
                    for c in self.clients:
                        c[1].send(msg_to_client.encode())
        except:
            print('好像有异常出现，服务器自行停止！')

    # 根据用户的昵称或姓名，找到对应的连接
    def search_for_client(self, user_name):
        for c in self.clients:
            if user_name == c[0]:
                return c[1]
        else:
            return None


if __name__ == '__main__':
    server_ip = '19.19.19.251'
    server_port = 7777
    talk_server = WoniuTalkServer(server_ip, server_port)
    try:
        talk_server.accept_client()        # 只要receive方法中有异常发生，均会进入except分支运行其代码
    except ConnectionResetError:
        print("好像有异常出现，服务器自行停止。")
