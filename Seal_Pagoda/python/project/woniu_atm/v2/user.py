# 定义单独的列表，分别保存不同的用户属性
# names = ['steve', 'bill', 'jack']
# passwords = ['112233', 'abc', 'ma88']
# tels = ['13966668888', '18899996666', '19977778888']

# 定义一个包含列表元素的列表，用于保存注册用户信息
# users = [['steve', '112233', '13966668888'],
#          ['bill', 'abc', '18899996666'],
#          ['jack', 'ma88', '19977778888']]

# 定义一个包含字典元素的列表，用于保存所有注册用户信息，其中每个用户的信息以字典形式保存
users = [{'name': 'steve', 'password': '123', 'tel': '13966668888', 'balance': 9000.00, 'history': ''},
         {'name': 'bill', 'password': 'abc', 'tel': '18899996666', 'balance': 7500.00, 'history': ''},
         {'name': 'jack', 'password': 'ma88', 'tel': '19977778888', 'balance': 5800.00, 'history': ''}]

# 定义一个全局变量，用于保存当前登录用户的在users列表中的index值，默认未登录的情况下为-1
current_user_id = -1


def get_users():
    return users


def get_current_user_id():
    return current_user_id
