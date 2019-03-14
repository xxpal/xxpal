# ======================================================================
# 练习002
# 统计字符：从键盘输入一个字符串，统计该字符串中的字符。
# 该字符串当中包含几个大写字母，几个小写字母，几个数字，几个特殊符号。
# ======================================================================


def court_char(str_input: str = '') -> None:
    lower = []
    upper = []
    nums = []
    other = []

    for char in str_input:
        if char.isupper():
            upper.append(char)
        elif char.islower():
            lower.append(char)
        elif char.isnumeric():
            nums.append(char)
        else:
            other.append(char)

    print('您输入的字符串为：', str_input)
    print('该字符串共有{}个字符，包含了{}个大写字母，{}小写字母，{}个数字，{}个其它字符。'
          .format(len(str_input), len(upper), len(lower), len(nums), len(other)))
    return


str_input = input('请输入一个字符串：')
court_char(str_input)
