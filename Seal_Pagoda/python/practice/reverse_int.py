# ======================================================================
# 练习005
# 数字处理：用户输入一个正整数，将该正整数倒序输出，并求各位数相加之和。
# 要求：不允许把用户输入的正整数处理为字符串，只能按照数值运算的规律完成本题。
# 扩展：完成此题后，进一步求小数的每位之和，如1234.567，并让该小数顺序按位输出。
# ======================================================================


def reverse_int(value: int = 0) -> None:
    print('您输入的正整数为：', value)

    # 首先需要判断输入的整数的位数
    flag = True         # 循环判断标志用于控制while循环
    digit = 0           # 记录输入的正整数的位数
    quotient = value    # 记录该正整除每次整除操作的商
    nums = []           # 顺序保存该正整数的每一位数字
    total = 0           # 记录改正整数每一位数字之和
    value_reverse = 0   # 记录输入的正整数所对应的倒序正整数

    # 用该整数整除10，同时计数器加一，循环此过程，直至整除的商为0。
    while flag:
        quotient //= 10
        digit += 1
        if quotient == 0:
            flag = False
            quotient = value

    # 确定整数位数后，提取每一位数字
    for i in range(digit-1, -1, -1):
        n = quotient // 10**i
        nums.append(n)
        quotient -= n * 10**i
        # print(quotient)
        # print(nums)
        total += n          # 通过累加得到所有位置上的数字之和

    # 生成输入的整数所对应的倒序正整数
    for j in range(len(nums)):
        value_reverse += nums[j] * 10**j

    print('该正整数所对应的倒序正整数为：', value_reverse)
    print('该正整数各位置上的数字之和为：', total)
    return


value = int(input('请输入一个任意位数的正整数：'))
reverse_int(value)
