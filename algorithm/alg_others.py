# coding=utf-8
import sys


def find_greatest_sum_of_sub_array(arr):
    """
    只要 arr 有正数，则结果子数组肯定以正数开始和结束
    """
    result = -sys.maxsize
    cur_max = 0
    for i in arr:
        if cur_max <= 0:  # 如果为负数或0，则该子数组已结束（不可能结合到后续子数组中，会令后续子数组更小）
            cur_max = i
        else:
            cur_max += i

        result = max(result, cur_max)
    print result


if __name__ == '__main__':
    find_greatest_sum_of_sub_array([5, 2, 3, -5, 6, -6, 3])
