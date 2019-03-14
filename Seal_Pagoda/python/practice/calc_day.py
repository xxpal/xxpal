# 输入某年某月某日，判断这一天是这一年的第几天


def calc_day(y, m, d):
    day_of_year = 0
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 判断输入的年份是否是闰年
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        # print('%d年是闰年，2月份有29天。' % y)
        print('{}年是闰年，2月份有29天。'.format(y))
        days[1] = 29
    else:
        print('{}年是平年，2月份有28天。'.format(y))

    for i in range(m-1):
        day_of_year += days[i]

    return day_of_year + d


year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
day = int(input('请输入日期：'))
count = calc_day(year, month, day)
print('{}年{}月{}日是该一年中的第{}天。'.format(year, month, day, count))
