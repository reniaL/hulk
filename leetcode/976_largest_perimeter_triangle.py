# coding=utf-8


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A)-3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0


if __name__ == '__main__':
    solution = Solution()
    l = [6,2,3,3]
    print solution.largestPerimeter(l)