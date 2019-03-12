# coding=utf-8


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        每次可爬一级或两级楼梯，每级楼梯耗费cost[i]，可从第一级或第二级楼梯开始。
        求爬完楼梯的最小消费
        :type cost: List[int]
        :rtype: int
        """
        result = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            result.append(cost[i] + min(result[i-1], result[i-2]))
        return min(result[-1], result[-2])


if __name__ == '__main__':
    solution = Solution()
    cost = [1, 2, 5, 3, 2, 1, 3, 9, 6, 4]
    print solution.minCostClimbingStairs(cost)
