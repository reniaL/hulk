# coding=utf-8

def largestTimeFromDigits(list):
    """
    给4个数字，输出能组成的有效的、最大的时间
    """
    # 首先，注意查找前两个数字
    num1 = getMaxWithLimit(list, 2)
    if num1 == -1:
        return ""
    else:
        list.remove(num1)

    num2 = getMaxWithLimit(list, 3 if num1 == 2 else 9)
    if num2 == -1:
        return ""
    else:
        list.remove(num2)

    # 第三个数字，如果非法，则再检查，num1是否2，且num2能否放到1
    num3 = getMaxWithLimit(list, 5)
    if num3 == -1:
        if num1 == 2 and num2 < 2:
            return "%d%d:%d%d" % (num2, max(list), 2, min(list))
        else:
            return ""
    else:
        list.remove(num3)

    return "%d%d:%d%d" % (num1, num2, num3, list[0])


def getMaxWithLimit(list, limit):
    """
    max value no more than limit, -1 if no suitable
    """
    result = -1
    for i in list:
        if limit >= i > result:
            result = i

    return result


if __name__ == '__main__':
    print largestTimeFromDigits([4, 3, 5, 1])
    print largestTimeFromDigits([0, 2, 6, 5])
    print largestTimeFromDigits([0, 2, 6, 6])
    print largestTimeFromDigits([2, 0, 6, 7])
    print largestTimeFromDigits([2, 1, 6, 7])

    print largestTimeFromDigits([2, 2, 6, 7])
    print largestTimeFromDigits([1, 3, 6, 7])
    print largestTimeFromDigits([1, 3, 5, 7])
    print largestTimeFromDigits([0, 3, 5, 2])
