# ================================================================================
# P297 - 练习题3
# 输入一个字符串，分别计算出'ab'出现的次数和'e'出现的次数。
# ================================================================================


def count_str(inputs: str) -> None:
    if len(inputs) == 0:
        inputs = 'abcdabkrajb'
        print('你输入的字符串为空，默认的字符串为：', inputs)
    ab_count = inputs.count('ab')
    e_count = inputs.count('e')
    print('"ab"在字符串{}中出现的次数为：{}'.format(inputs, ab_count))
    print('"e"在字符串{}中出现的次数为：{}'.format(inputs, e_count))

    return


print(count_str.__doc__)
count_str(input("请输入一个字符串："))
print('\n' * 3)
