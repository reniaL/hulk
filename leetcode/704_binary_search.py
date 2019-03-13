# coding=utf-8


class Solution(object):
    def search(self, nums, target):
        """
        Binary search, return index if found target, otherwise -1.
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bin_search(nums, target, 0, len(nums) -1)

    def bin_search(self, nums, target, start, end):
        if start > end:
            return -1

        if start == end:
            return start if nums[start] == target else -1

        mid = (start + end) / 2
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            return self.bin_search(nums, target, mid+1, end)
        else:
            return self.bin_search(nums, target, start, mid-1)


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 5]
    target = 5
    print solution.search(nums, target)
