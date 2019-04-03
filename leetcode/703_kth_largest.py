# coding=utf-8


class KthLargest(object):
    """
    TODO 性能较差，有待改进
    编写一个对象，输入k和nums
    每次调用 add(val) 方法时，返回 nums + val 中的第 k 大的数值
    """

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.nums and len(self.nums) >= self.k and val <= self.nums[self.k-1]:
            return self.nums[self.k-1]

        i = 0
        for x in self.nums:
            if val >= x:
                break
            i = i+1

        self.nums.insert(i, val)
        return self.nums[self.k-1]


if __name__ == '__main__':
    nums = [4, 7]
    obj = KthLargest(2, nums)
    print obj.add(1)
    print obj.add(5)
    print obj.add(5)
    print obj.add(10)
    print obj.add(9)
