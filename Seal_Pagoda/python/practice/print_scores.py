# ================================================================================
# P298 - 练习题6
# 给定一个成绩单（字典），找出最大最小值，并求出平均成绩，成绩自己定义。
# ================================================================================


def print_scores(trans: dict = {}) -> None:

    student_num = len(trans)
    student_best = set()
    student_worst = set()
    scores = list(trans.values())
    score_max = 0       # 最高分的初初始值应设为最小值
    score_min = 100     # 最低分的初始值值应设为最大值
    score_sum = 0
    score_average = 0

    # 找到最高分、最低分，计算总分、平均分
    for i in range(student_num):
        score_sum += scores[i]      # 循环累加可得总分
        # 两两循环比较，取较大值
        if scores[i] > score_max:
            score_max = scores[i]
        # 两两循环比较，取较小值
        if scores[i] < score_min:
            score_min = scores[i]
        # 所有成绩累加完成后，计算平均分
        if i == student_num - 1:
            score_average = score_sum/student_num

    # 更简便的方式：调用Python自带的max()和min()函数
    # score_max = max(transcript.values())
    # score_max = min(transcript.values())

    # 找到所有的最高分获得者和最低分获得者
    for k, v in trans.items():
        if v == score_max:
            student_best.add(k)
        if v == score_min:
            student_worst.add(k)

    print('现在公布考试成绩：')
    # 格式化打印所有学生的成绩，每行输出5个人的成绩
    count = 0
    for item in trans.items():
        print('%-16s' % str(item), end='')
        count += 1
        if count % 5 == 0:
            print()

    print('全班最高分：%.2f，获得者：%s' % (score_max, student_best))
    print('全班最低分：%.2f，获得者：%s' % (score_min, student_worst))
    print('全班平均分：%.2f' % score_average)

    return


transcript = {'刘德华': 80, '张学友': 82, '周杰伦': 61, '王力宏': 97, '沈腾': 38,
              '马丽': 42, '杨幂': 77, '赵丽颖': 75, '郭德纲': 66, '岳云鹏': 38,
              '何炅': 96, '撒贝宁': 96, '谢娜': 49, '王宝强': 58, '蔡康永': 90}
print_scores(transcript)
