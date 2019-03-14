# ================================================================================
# P298 - 练习题5
# 将一个列表去重，并返回一个新的列表。
# ================================================================================


def dedup_list(list_input: list = []) ->None:

    if len(list_input) == 0:
        list_input = [44, 12, 55, 44, 12, 55, 33, 100]
        print('输入的列表为空，默认的列表为：', list_input)
    print('去重之前，列表为：', list_input)
    print('去重之后，列表为：', list(set(list_input)))   # 新生成的列表中元素顺序很可能变化，因为set()是无序的
    new_list = []
    for i in list_input:
        if i not in new_list:
            new_list.append(i)

    print('去重之后，列表为：', new_list)

    return


dedup_list(list(input("请输入一个列表：")))
