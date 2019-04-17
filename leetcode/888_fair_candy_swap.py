# coding=utf-8


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        交换 A 和 B 中的一个元素，令 A 和 B 的和相等。输出 A 和 B 分别要交换的元素值
        保证至少有一个解
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a = sum(A)
        target = (sum_a + sum(B)) / 2
        diff = target - sum_a
        set_b = set(B)  # 如果不用set，就会超时

        for i in A:
            swap_target = i + diff
            if swap_target >= 1 and swap_target in set_b:
                return [i, swap_target]
        return []


if __name__ == '__main__':
    A = [1, 2, 5]
    B = [2, 4]
    instance = Solution()
    print instance.fairCandySwap(A, B)
