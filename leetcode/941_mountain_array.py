# coding=utf-8


class Solution(object):
    def validMountainArray(self, A):
        """
        检查一个数组是否"山峰"数组，即前面升序，后面降序
        :type A: List[int]
        :rtype: bool
        """
        if not A or len(A) < 3 or A[0] > A[1]:
            return False

        flag = False
        prev = A[0]
        for i in A[1:]:
            if i == prev:
                return False

            if not flag:
                if i < prev:
                    flag = True
                prev = i
            else:
                if i < prev:
                    prev = i
                else:
                    return False
        return flag


if __name__ == '__main__':
    solution = Solution()
    A = [2, 5, 8, 3, 0]
    print solution.validMountainArray(A)