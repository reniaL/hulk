# coding=utf-8


class Solution(object):
    """
    一个字符串列表，寻找最长的公共前缀序列
    有一些性能更好的解法，例如分治法，可参考 https://leetcode.com/problems/longest-common-prefix/solution/
    """
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        result = []
        size = min([len(x) for x in strs])
        for i in range(size):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return ''.join(result)
            result.append(char)
        return ''.join(result)


if __name__ == '__main__':
    strs = ["drag", "drap", "dragon"]
    solution = Solution()
    print solution.longestCommonPrefix(strs)