# coding=utf-8


def full_permutation(arr, pick, result):
    """
    输出一个数组的全排列
    :param arr: 目标数组
    :param pick: pick[i] 为 True 表示已选择了第 i 个元素，为 False 则表示未选择
    :param result: 当前已选择的元素的列表
    """
    for i in range(len(arr)):
        if not pick[i]:
            pick[i] = True
            result.append(arr[i])

            if len(result) == len(arr):
                print result
            else:
                full_permutation(arr, pick, result)

            pick[i] = False
            result.pop()


def all_combinations(arr, start, result):
    """
    输出一个数组的全部组合（没有重复，深度优先遍历）
    :param arr: 目标数组
    :param start: 起始索引
    :param result: 当前已选择的元素的列表
    """
    for i in range(start, len(arr)):
        result.append(arr[i])
        print result  # 输出每种组合

        if i+1 != len(arr):  # 如果还不是最后一个元素，则继续递归、遍历
            all_combinations(arr, i+1, result)

        result.pop()


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    all_combinations(arr, 0, [])
