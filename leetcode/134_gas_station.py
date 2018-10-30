# coding=utf-8


def run_gas_station(gas, cost):
    """
    一条环形公路，有N个加油站。加油站i存有汽油gas[i]，从加油站i行使至加油站i+1需耗费汽油cost[i]。
    问：是否存在一个加油站，从该加油站出发，能完整地绕公路一周。
    思路：转换为diff，题目变为，是否存在一个起点，令diff之和始终大于0。
         跟求最大子数组和，有些类似
    :return: -1表示不存在满足条件的加油站，大于等于0则表示从第i个加油站出发可满足。
    """
    sum = 0  # diff 总和，最终必须大于0才能满足
    cur_sum = 0  # 当前分组 diff 总和，小于0则开始新的分组
    start = 0
    diffs = []
    for i in range(0, len(gas)):
        diffs.append(gas[i] - cost[i])
        sum += diffs[-1]
        if cur_sum >= 0:  # 分组 diff 和大于0，继续
            cur_sum += diffs[-1]
        else:  # 分组 diff 和 小于0，开始新分组
            start = i
            cur_sum = diffs[-1]

    print diffs
    print start if sum >= 0 else -1


if __name__ == '__main__':
    gas = [6, 5, 4, 5, 5, 5]
    cost = [7, 2, 8, 2, 3, 8]
    run_gas_station(gas, cost)
