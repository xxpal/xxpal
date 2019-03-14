class User:
    # 定义一个包含字典元素的列表，用于保存所有注册用户信息，其中每个用户的信息以字典形式保存
    users = [{'name': 'steve', 'password': '123', 'tel': '13966668888', 'balance': 9000.00, 'history': ''},
             {'name': 'bill', 'password': 'abc', 'tel': '18899996666', 'balance': 7500.00, 'history': ''},
             {'name': 'jack', 'password': 'ma88', 'tel': '19977778888', 'balance': 5800.00, 'history': ''}]

    # 定义一个全局变量，用于保存当前登录用户的在users列表中的index值，默认未登录的情况下为-1
    current_user_id = -1

    def get_users(self):
        return self.users

    def get_current_user_id(self):
        return self.current_user_id
