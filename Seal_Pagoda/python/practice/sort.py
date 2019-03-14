# ======================================================================
# 练习009
# 给定一个列表，里面包含一批纯数字，按从小到大对其进行排序。
# 禁止使用Python自带的sort方法。
# ======================================================================


def bubble_sort_simple(nums: list) -> None:
    nums_len = len(nums)
    print('排序之前，列表为：', nums)

    for i in range(nums_len):
        for j in range(i+1, nums_len):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

    print('排序之后，列表为：', nums)
    return


nums = [5, 3, 9, 11, 2, 0, 1, 1, 3, 8, 5, 5, 6, 6, 1, 7, 9, 1]
bubble_sort_simple(nums)
