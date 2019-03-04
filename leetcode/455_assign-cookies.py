# coding=utf-8


def findContentChildren(g, s):
    """
    给孩子分饼干，g 是孩子的胃口列表，s 是饼干列表。求最多能满足多少个孩子的胃口。
    使用贪心算法
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    g.sort()
    s.sort()
    count = 0
    gi = len(g) - 1
    si = len(s) - 1
    while gi >= 0 and si >= 0:
        if g[gi] <= s[si]:
            count = count + 1
            gi = gi - 1
            si = si - 1
        else:
            gi = gi - 1

    return count


if __name__ == '__main__':
    g = [3, 1, 5, 7]
    s = [1, 2, 3, 4]
    print findContentChildren(g, s)
