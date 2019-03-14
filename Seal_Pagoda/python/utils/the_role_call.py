import random

wnsh_test_c003 = ["周浩文",
                  "周世文",
                  "赵天朔",
                  "沈剑春",
                  "祝源",
                  "成金梅",
                  "张宁"]
# wnsh_test_c003 = {"WNSH201811005": "周浩文",
#                   "WNSH201812001": "周世文",
#                   "WNSH201812003": "赵天朔",
#                   "WNSH201812005": "沈剑春",
#                   "WNSH201812006": "祝源",
#                   "WNSH201812007": "成金梅",
#                   "WNSH201812008": "张宁"}


def bingo(class_id: list) -> str:
    sn = random.randint(0, len(class_id)-1)
    return wnsh_test_c003[sn]


print(bingo(wnsh_test_c003))
