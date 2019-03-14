from python.project.woniu_atm.v2.utils import *
import random


# 业务类函数：查询
def query(user_id: int) -> None:
    print('>>> 正在进行查询操作……')
    print('>>> 尊敬的%s，您的账户余额为：%.2f元，电话号码为：%s。' %
          (users[user_id]['name'],
           users[user_id]['balance'],
           users[user_id]['tel']))

    return


# 业务类函数：取款
def withdraw(user_id: int) -> None:
    print('>>> 正在进行取款操作……')
    money = input(">>> 请输入您的取款金额：")
    # 先判断输入内容是否是有效的数字
    if check_number(money):
        # 取款前先要判断账户余额
        if users[user_id]['balance'] >= float(money):
            save_transaction(user_id, '取款', float(money))
            check_balance(user_id, -float(money))
        else:
            print('>>> 您的账户余额不足，请确认后重新输入！')
    else:
        print(">>> 您输入的金额有误，请确认后重新输入！")
        withdraw(user_id)

    return


# 业务类函数：存款
def deposit(user_id: int) -> None:
    print('>>> 正在进行存款操作……')
    money = input('>>> 请输入您的存款金额：')
    # 先判断输入内容是否是有效的数字
    if check_number(money):
        save_transaction(user_id, '存款', float(money))
        check_balance(user_id, float(money))
    else:
        print('>>> 您输入的金额有误，请确认后重新输入！')
        deposit(user_id)

    return


# 业务类函数：转账
def transfer(user_id: int) -> None:
    print('>>> 正在进行转账操作……')
    payee = input('>>> 请输入对方账户名称：')
    money = input('>>> 请输入您的转账金额：')
    payee_id = check_user(payee)

    # 如果收款人不存在，则提示用户重新输入对方账户信息
    if payee_id == -1:
        print('>>> 对方账户不存在，请确认后重新输入！')
        transfer(user_id)
    else:
        # 如果输入的转账金额格式不正确，则提示用户重新输入
        if check_number(money):
            # 如果转账金额大于用户的账户余额，则提示用户账户余额不足
            if float(money) > float(users[user_id]['balance']):
                print('>>> 您的账户余额不足，请确认后重新输入！')
                transfer(user_id)
            else:
                save_transaction(user_id, '取款', float(money))
                save_transaction(payee_id, '存款', float(money))
                check_balance(user_id, float(money))
                # check_balance(payee_id, float(money))
        else:
            print('>>> 您输入的金额有误，请确认后重新输入！')

    return


# 业务类函数：审计、流水、清单
def audit(user_id: int) -> None:
    print('>>> 正在查询历史记录……')
    current_user = users[user_id]

    histories = current_user['history'].split('##')
    print('>>> 尊敬的%s，您的账户历史交易如下：' % current_user['name'])
    for history in histories:
        print('>>>\t--- ', history)

    return


# 业务类函数：注册
def register() -> bool:
    """
    用户注册
    :return: 注册成功则返回True，反之则返回False
    """
    name = input('>>> 请输入您期望注册的用户名：')
    index = check_user(name)
    status = False

    # 先判断用户名是否存在
    if index >= 0:
        print('>>> 对不起，该用户名已存在，请重新注册！')
    else:
        print('>>> 恭喜！您输入的用户名可用！')
        password = input('>>> 请设置您的账户密码：')
        tel = input('>>> 请输入您的电话号码：')
        balance = random.randint(1000, 9999)  # 生成一个随机数，模拟新注册的用户的初始的存款金额
        # 不同的属性值构成了用户记录，每个用户的信息以字典的形式保存
        user = {}
        user.update({'name': name, 'password': password, 'tel': tel,
                     'balance': balance, 'history': ''})
        # 将所有的用户记录以列表形式保存，并返回状态值
        users.append(user)
        status = True
        print('>>> 注册成功！')

    return status


# 业务类函数：登录
def login() -> bool:
    """
    用户登录
    :return: 登录成功则返回True，反之则返回False
    """
    name = input('>>> 请输入您的用户名：')
    index = check_user(name)
    status = False

    if index >= 0:
        password = input('>>> 请输入您的密码：')
        if users[index]['password'] == password:
            print('>>> 登录成功！')
            global current_user_id  # 要在函数中修改全局变量，则必须加global进行声明，若只读取不修改，直接读取即可
            current_user_id = index  # 将当前用户的index值赋值给全局变量current_user
            status = True
        else:
            print('>>> 密码错误，请重新登录！')
    else:
        print('>>> 该用户不存在，请先注册！')

    return status
