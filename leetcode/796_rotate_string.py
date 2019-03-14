# coding=utf-8


class Solution(object):
    def rotateString(self, A, B):
        """
        判断，将B"旋转"（将首字母移到末尾）一定次数之后，能否等于A
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True

        if len(A) != len(B):
            return False

        # 每次找到B的第一个字符，都将A进行裁切，判断是否等于B。不相等则继续往后找。
        start = 0
        size = len(A)
        i = A.find(B[0], start)
        while start < size and i > -1:
            if A[i:] + A[:i] == B:
                return True
            start = i + 1
            i = A.find(B[0], start)
        return False


if __name__ == '__main__':
    solution = Solution()
    a = "abcbc"
    b = "bcabc"
    print solution.rotateString(a, b)
