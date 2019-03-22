# coding=utf-8


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True

        s = str(x)
        return s[::-1] == s


if __name__ == '__main__':
    nums = [-123, -1, 0, 1, 5, 9, 10, 11, 22, 23, 121, 131, 1221, 1341, 12345654321]
    solution = Solution()
    for num in nums:
        print num, solution.isPalindrome(num)

