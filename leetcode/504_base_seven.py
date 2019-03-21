# coding=utf-8


class Solution(object):
    def convertToBase7(self, num):
        """
        将一个数值转换为7进制
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        result = []
        negative = num < 0
        num = abs(num)
        while num > 0:
            result.append(str(num % 7))
            num = num / 7

        if negative:
            result.append("-")
        result.reverse()
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    for i in range(100):
        print i, solution.convertToBase7(i)
    print solution.convertToBase7(-7)
    print solution.convertToBase7(-100)
