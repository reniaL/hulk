# coding=utf-8


class Solution(object):
    def largeGroupPositions(self, S):
        """
        连续的相同字母为一组
        找出所有长度大于等于3的组，并输出每个分组的开始、结束的索引
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) < 3:
            return []

        result = []
        last = S[0]
        start = 0
        i = 1
        for i in range(1, len(S)):
            if S[i] != last:
                if i - start >= 3:
                    result.append([start, i-1])

                start = i
                last = S[i]
        if i - start >= 2:
            result.append([start, i])
        return result


if __name__ == '__main__':
    instance = Solution()
    S = "abcdddeeeeaabbb"
    print instance.largeGroupPositions(S)