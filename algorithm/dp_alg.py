# coding=utf-8
def run_coins(target):
    """
    最少需要多少个硬币，才能凑到 target 这个数
    """
    result = [0]
    for i in range(1, target + 1):
        temp = []
        for coin in [1, 3, 5]:
            if i - coin >= 0:
                temp.append(result[i - coin] + 1)
        result.append(min(temp))

    return result


def run_points(length):
    """
    切钢条（木头），长度为 length，输出最佳的价格
    """
    result = [0]
    points = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for i in range(1, length + 1):
        temp = []
        for cut_length in range(1, 11):
            if i - cut_length >= 0:
                temp.append(result[i - cut_length] + points[cut_length])

        result.append(max(temp))

    return result


if __name__ == '__main__':
    # print run_coins(14)
    result = run_points(20)
    for i in range(len(result)):
        print i, result[i]
