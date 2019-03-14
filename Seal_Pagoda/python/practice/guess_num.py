# ======================================================================
# 练习006
# 猜数字游戏：系统随机生成一个1000以内的正整数，用户每次输入一个数字，
# 如果输入数字大于系统随机生成的数字则提示"大了"，反之则提示"小了"，
# 相等则游戏结束，并提示"通关"并输出猜测的总次数。
# 提示：可以import random来生成随机数。
# ======================================================================
import random


def guess_num() -> None:
    count = 0       # 猜数字计数器
    start = 1       # 生成随机数的最小值
    stop = 1000     # 生成随机数的最大值
    random_num = random.randint(start, stop)    # 生成并保存一个随机数

    # 猜数字判断
    while True:
        input_num = int(input('请输入一个{}以内的正整数：'.format(stop)))
        count += 1
        if input_num == random_num:
            print('通关！')
            break
        elif input_num > random_num:
            print('大了！请再试试！')
            continue
        else:
            print('小了！请再试试！')
            continue

    print('你一共猜了{}次.'.format(count))
    return


guess_num()
