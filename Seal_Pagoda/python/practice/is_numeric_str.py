# ======================================================================
# 练习007
# 字符串判断：从键盘输入一个字符串，判断该字符串是否可以被转换为一个有效的数字。
# 禁止使用Python自带方法完成
# ======================================================================


def is_numeric_str(input_str: str) -> bool:
    # 思路分析：
    # 1、有效的字符只能是数字0~9、+、-和.
    # 2、最多只能包含一个.、+、-
    # 3、+、-只能出现在字符串首位
    # 4、若字符串首位字符为0，则字符串中必须包含小数点
    is_numeric = False
    chars = ('.', '-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    init_char = input_str[0]
    count_dot = 0
    count_plus = 0
    count_minus = 0

    print('您输入的字符串为：{}'.format(input_str))

    for char in input_str:
        # 若i为非0~9、.、-、+，则终止循环；反之，则进一步判断其它条件
        if char not in chars:
            break
        else:
            # 如果字符为'.'，则其计数+1
            if char is '.':
                count_dot += 1
                continue
            # 如果字符为'-'且不是字符串的第一个字符，则终止循环；否则其计数+1，循环继续
            elif char is '-':
                count_minus += 1
                if input_str.index(char) == 0:
                    continue
                else:
                    break
            # 如果字符为'+'且不是字符串的第一个字符，则终止循环；否则其计数+1，循环继续
            elif char is '+':
                count_plus += 1
                if input_str.index(char) == 0:
                    continue
                else:
                    break
            # 如果首字符为0且字符串中不包含.符号，则终止循环
            elif char is '0' and '.' not in input_str:
                break

        is_numeric = True

    if is_numeric:
        print('该字符串可以转换成为一个有效的数字！')
    else:
        print('该字符串不能转换成为一个有效数字')

    return is_numeric


is_numeric_str(input('请输入一串字符串：'))
