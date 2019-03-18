# coding=utf-8


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = num1
        n2 = num2
        size1 = len(n1)
        size2 = len(n2)
        if size1 > size2:
            n2 = '0' * (size1 - size2) + n2
        else:
            n1 = '0' * (size2 - size1) + n1

        result = range(len(n1))
        flag = 0
        for i in range(-1, -len(n1) - 1, -1):
            current = int(n1[i]) + int(n2[i]) + flag
            result[i] = str((current % 10))
            flag = 1 if current >= 10 else 0

        if flag == 1:
            result.insert(0, '1')

        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    print solution.addStrings('111', '9222')
