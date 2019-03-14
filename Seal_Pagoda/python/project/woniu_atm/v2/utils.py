from python.project.woniu_atm.v2.user import *
import time


# 功能性函数：保存历史交易记录
def save_transaction(user_id: int, tran_type: str, money: float) -> None:
    """

    :param user_id:
    :param tran_type:
    :param money:
    :return:
    """
    current_user = users[user_id]
    before_transaction = current_user['history']
    this_transaction = current_user['name'] + ' ' + time.strftime('%Y-%m-%d %H:%M:%S') + \
        ' ' + tran_type + ' ' + str(money)
    history = before_transaction + '##' + this_transaction
    current_user['history'] = history
    # users[user_id] = current_user
    print('>>> 尊敬的%s，您有一条新的交易记录：\n\t--- %s' % (current_user['name'], this_transaction))

    return


# 功能性函数：检查账户余额
def check_balance(user_id: int, money: float) -> None:
    current_user = users[user_id]
    current_user['balance'] = current_user['balance'] + money
    # users[current_user_id] = current_user
    if money < 0:
        print('>>> 尊敬的%s，您已成功取款：%.2f元，当前账户余额为：%.2f元。' %
              (current_user['name'], -money, current_user['balance']))
    else:
        print('>>> 尊敬的%s，您已成功存款：%.2f元，当前账户余额为：%.2f元。' %
              (current_user['name'], money, current_user['balance']))

    return


# 功能性函数：检查用户名是否存在
def check_user(name: str) -> int:
    """
    检查用户名是否存在
    :param name: 用户名
    :return: 用户名存在则返回其所在列表中的index值，反之则返回-1
    """
    # 法一：通过列表和字典的[][]操作比对name值，找到其所在列表中的index
    # for i in range(len(users)):
    #     if users[i]['name'] == name:
    #         return i

    # 法二：通过index()函数，返回其所在列表中的index
    for user in users:
        if user['name'] == name:
            return users.index(user)

    return -1


# 功能性函数：检查输入的字符串是否能被转化成一个有效的数字
def check_number(input_str: str) -> bool:
    """
    对输入的字符串进行判断，确认其是否可以转换为一个有效的数字
    :param input_str:
    :return:
    """
    is_valid = False  # 标识是否是有效的字符串
    dot_num = 0
    # 只考虑整数情况
    # for char in input_str:
    #     if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
    #         if char is '0' and input_str.index(char) == 0:
    #             is_valid = False
    #             break
    #         else:
    #             is_valid = True
    #     else:
    #         is_valid = False
    #         break

    # 考虑小数情况
    for char in input_str:
        if char in ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if char is '.':
                dot_num += 1
                if dot_num >= 2:
                    is_valid = False
                    break
            elif char is '0' and input_str.index(char) == 0:
                is_valid = False
                break
            else:
                is_valid = True
        else:
            is_valid = False
            break

    return is_valid
