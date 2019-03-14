from python.project.woniu_atm.v3.user import User
import time


class Utils:
    def __init__(self):
        self.user = User()

    # 功能性函数：保存历史交易记录
    def save_transaction(self, user_id, tran_type, money):
        """
        :param user_id:
        :param tran_type:
        :param money:
        :return:
        """
        users = self.user.get_users()
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
    def check_balance(self, user_id, money):
        users = self.user.get_users()
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
    def check_user(self, name):
        """
        检查用户名是否存在
        :param name: 用户名
        :return: 用户名存在则返回其所在列表中的index值，反之则返回-1
        """

        # 通过index()函数，返回其所在列表中的index
        users = self.user.get_users()
        for user in users:
            if user['name'] == name:
                return users.index(user)

        return -1

    # 功能性函数：检查输入的字符串是否能被转化成一个有效的数字
    def check_number(self, input_str):
        """
        对输入的字符串进行判断，确认其是否可以转换为一个有效的数字
        :param input_str:
        :return:
        """
        is_valid = False  # 标识是否是有效的字符串
        dot_num = 0

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
