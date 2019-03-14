from python.project.woniu_atm.v3.account import Account
from python.project.woniu_atm.v3.account import User


class Menu:
    def __init__(self):
        self.account = Account()
        self.user = User()

    # 流程控制函数：WoniuATM入口程序
    def enter(self):
        """
        入口程序，启动WoniuATM
        :return:
        """
        # 构建入口程序菜单
        menu = '''
        ***************** 欢迎使用 WoniuATM **********************
        *****************   请选择操作菜单   **********************
        ************** 1、注册   2、登录   3、退出 *****************
        '''
        print(menu)

        option = input('>>> 请输入相应的“数字”选择您想进行的操作：')
        if option == '1':
            # while not register():
            #     continue
            self.account.register()
            self.enter()
        elif option == '2':
            count = 0
            # 登录失败3次，则返回入口程序
            while not self.account.login():
                count += 1
                if count == 3:
                    print('>>> 登陆失败3次，请您稍后再试或重新注册！')
                    self.enter()
                else:
                    print('>>> 登陆失败%d次，您还可尝试%d次，请确认您的登录信息！' % (count, 3 - count))
                    continue
            self.home()
        elif option == '3':
            exit('>>> 感谢使用WoniuATM，欢迎下次光临！')
        else:
            print('>>> 您输入的操作选项有误，请重新输入。')
            self.enter()

        return

    # 流程控制函数：WoniuATM业务操作主程序
    def home(self):
        """
        程序主页，WoniuATM 业务菜单
        :return:
        """
        # 构建主页面的菜单
        menu = '''
        *************************** 欢迎进入 WoniuATM **********************************
        ***************************   请选择操作菜单  ***********************************
        ********** 1、查询   2、取款   3、存款   4、转账   5、流水  6、返回  7、退出 **********
        '''
        print(menu)

        option = input(">>> 请输入相应的“数字”选择您想进行的操作：")
        current_user_id = self.user.get_current_user_id()
        if option == "1":
            self.account.query(current_user_id)
            self.home()
        elif option == "2":
            self.account.withdraw(current_user_id)
            self.home()
        elif option == "3":
            self.account.deposit(current_user_id)
            self.home()
        elif option == "4":
            self.account.transfer(current_user_id)
            self.home()
        elif option == "5":
            self.account.audit(current_user_id)
            self.home()
        elif option == "6":
            self.enter()
        elif option == "7":
            exit('>>> 感谢使用WoniuATM，欢迎下次光临！')

        return


if __name__ == '__main__':
    Menu().enter()
