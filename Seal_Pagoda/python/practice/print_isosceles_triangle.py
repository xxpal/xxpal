import random


# 打印等腰三角形
def print_isosceles_triangle(line: int = 0) -> None:
    # 如果未指定打印三角形的行数，则随机生成一个1~10的整数作为行数
    if line == 0:
        line = random.randint(1, 10)
    # 观察1：1行1颗星，2行3颗星，3行5颗星……以此类推，n行2n-1颗星
    # 观察2：若共有n行，则第i行上有(n-1)-i个空格分别分布在星号的左右两边
    print('指定三角形的高为{}，打印该等腰三角形如下：'.format(line))
    for i in range(line):
        blanks = (line - 1) - i
        asterisks = i * 2 + 1
        print(' ' * blanks + '*' * asterisks + ' ' * blanks)

    return


print_isosceles_triangle()
