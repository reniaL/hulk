# coding=utf-8


class Solution(object):
    def rotatedDigits(self, N):
        """
        将一个数值中的每个数字旋转180度后，是否一个"好"数值，且不等于原数值。
        旋转效果：
            0、1、8 -> 0、1、8
            2、5、6、9 -> 5、2、9、6
            3、4、7 -> bad
        输入N，返回 1-N 中有多少个好数值
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1, N + 1):
            s = str(i)
            if '3' in s or '4' in s or '7' in s:
                continue

            if '2' in s or '5' in s or '6' in s or '9' in s:
                count = count + 1

        return count


if __name__ == '__main__':
    instance = Solution()
    print instance.rotatedDigits(2000)
