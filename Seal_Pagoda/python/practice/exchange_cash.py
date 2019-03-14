# ======================================================================
# 练习003
# 组合问题：用1元纸币兑换1分，2分和5分的硬币，要求兑换总数为50枚。
# 问可以有多少种组合，每种组合对应1分，2分，5分分别是多少？
# ======================================================================


def exchange_cash(cash: int = 100, coins: int = 50) -> None:
    combs = []   # 不同兑换方式的组合保存在集合里
    loop1_count = 0     # 记录第一层for循环的次数
    loop2_count = 0     # 记录第二层for循环的次数
    # loop3_count = 0

    # 方法1：三层for循环，第一层判断5分硬币个数，第二层判断2分硬币个数，第三层判断1分硬币个数
    # 性能分析：循环1 ==> 21次；循环2 ==> 1071次；循环3 ==> 108171次
    # for coin5 in range(0, cash//5 + 1):
    #     loop1_count += 1
    #     for coin2 in range(0, cash//2 + 1):
    #         loop2_count += 1
    #         for coin1 in range(0, cash + 1):
    #             loop3_count += 1
    #             if (coin1 + coin2 + coin5 == coins) and (coin1 + 2 * coin2 + 5 * coin5 == cash):
    #                 combs.append({'1分': coin1, '2分': coin2, '5分': coin5})   # 将合适的兑换组合以字典的形式保存

    # 方法2：三层for循环，第一层判断5分硬币个数，第二层判断1分硬币个数，第三层判断2分硬币个数
    # 性能分析：循环1 ==> 21次；循环2 ==> 2121次；循环3 ==> 108171次
    # for coin5 in range(0, cash//5):
    #     loop1_count += 1
    #     for coin1 in range(0, cash):
    #         loop2_count += 1
    #         for coin2 in range(0, cash//2 + 1):
    #             loop3_count += 1
    #             if (coin1 + coin2 + coin5 == coins) and (coin1 + 2 * coin2 + 5 * coin5 == cash):
    #                 combs.append({'1分': coin1, '2分': coin2, '5分': coin5})   # 将合适的兑换组合以字典的形式保存

    # 方法3：三层for循环，第一层判断5分硬币个数，第二层判断2分硬币个数，第三层判断1分硬币个数
    # 性能分析：循环1 ==> 21次；循环2 ==> 2121次；循环3 ==> 108171次
    # for coin5 in range(0, cash//5):   # 5分硬币b最多19个
    #     loop1_count += 1
    #     for coin1 in range(0, cash//2 + 1):   # 2分硬币最多50个
    #         loop2_count += 1
    #         for coin2 in range(0, cash):   # 1分硬币最多49个
    #             loop3_count += 1
    #             if (coin1 + coin2 + coin5 == coins) and (coin1 + 2 * coin2 + 5 * coin5 == cash):
    #                 combs.append({'1分': coin1, '2分': coin2, '5分': coin5})   # 将合适的兑换组合以字典的形式保存

    # 方法3：两层for循环，第一层判断5分硬币个数，第二层判断2分硬币个数
    # 性能分析：循环1 ==> 21次；循环2 ==> 1071次；循环3 ==> 108171次
    for coin5 in range(0, cash//5):
        loop1_count += 1
        for coin2 in range(0, cash//2 + 1):
            loop2_count += 1
            coin1 = coins - coin2 - coin5
            if coin1 + 2 * coin2 + 5 * coin5 == cash:
                combs.append({'1分': coin1, '2分': coin2, '5分': coin5})   # 将合适的兑换组合以字典的形式保存

    print('first for loop:', loop1_count)
    print('second for loop:', loop2_count)
    # print('third for loop:', loop3_count)

    print('您一共有{}元现金，如需兑换{}个硬币，共有{}种兑换方案。具体如下：'.format(cash, coins, len(combs)))
    for item in combs:
        print(item)

    return


exchange_cash()
