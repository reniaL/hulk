# coding=utf-8


def run_house_robber(nums):
    """
    你是一个专业的小偷，从不失手！这次你要偷遍整条街！
    氮素，如果相邻的两家店都被偷，则会触发报警系统，警察蜀黍会来哦。
    肿么样作案，才能安全又最高回报呢？展示你的身手吧~
    :param nums 每家店的现金额
    """
    if not nums:
        return 0

    if len(nums) < 3:
        return max(nums)

    result = nums[0:2]
    result.append(max(nums[0] + nums[2], nums[1]))
    for i in range(3, len(nums)):
        result.append(max(result[i - 1], result[i - 2] + nums[i], result[i - 3] + nums[i]))

    return result[-1]


if __name__ == '__main__':
    nums = [5, 2, 4, 7, 3, 8]
    print run_house_robber(nums)
