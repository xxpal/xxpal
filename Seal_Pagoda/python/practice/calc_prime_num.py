# ======================================================================
# 练习010
# 请计算200以内的所有质数。
# 质数（prime number）又称素数，有无限个。
# 质数定义为在大于1的自然数中，除了1和它本身以外不再有其它因数。
# ======================================================================


def calc_prime_num(start: int = 2, stop: int = 200) -> None:
    prime_nums = []     # 用于存放每一个质数

    # 如果一个数能被2整除，则表明此数不是素数，反之是素数。
    # 改进算法：在一般领域，如果一个正整数n，不能被2到math.sqrt(n)之间的任一整数整除，则n为质数
    for num in range(start, stop):
        is_prime_num = True
        for n in range(start, num):    # for n in range(2, int(math.sqrt(num))+1)
            if num % n == 0:
                is_prime_num = False
                break
        if is_prime_num:
            prime_nums.append(num)

    print('{}到{}之间，一共有{}个质数。分别是：'.format(start, stop, len(prime_nums)))
    # 打印输出列表中所有的质数
    for i in range(len(prime_nums)):
        print(prime_nums[i], end='\t\t')
        if (i+1) % 10 == 0:
            print()

    return


calc_prime_num()
