# coding=utf-8


def climbStairs(n):
    """
    每次可爬1级或2级楼梯，爬n级楼梯，共有多少种不同的方法
    :type n: int
    :rtype: int
    """
    result = [1, 2]
    for i in range(2, n):
        result.append(result[i-2] + result[i-1])

    return result[n-1]


if __name__ == '__main__':
    print climbStairs(10)