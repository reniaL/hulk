# coding=utf-8


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        start = 1
        end = n
        num = n / 2

        while 1:
            result = guess(num)
            if result == 0:
                return num
            elif result < 0:
                end = num - 1
                num = (start + end) / 2
            else:
                start = num + 1
                num = (start + end) / 2


target = 0


def guess(num):
    # print 'guess', num
    if num == target:
        return 0

    return 1 if target > num else -1


if __name__ == '__main__':
    target = 33
    solution = Solution()
    print solution.guessNumber(100)
