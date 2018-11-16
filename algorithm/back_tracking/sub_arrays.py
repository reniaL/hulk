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


def all_combinations(arr, pick, result):
    """
    输出一个数组的全部组合（TODO 没去重）
    :param arr: 目标数组
    :param pick: pick[i] 为 True 表示已选择了第 i 个元素，为 False 则表示未选择
    :param result: 当前已选择的元素的列表
    """
    for i in range(len(arr)):
        if not pick[i]:
            pick[i] = True
            result.append(arr[i])
            print result

            if len(result) != len(arr):
                all_combinations(arr, pick, result)

            pick[i] = False
            result.pop()


if __name__ == '__main__':
    arr = [1, 2, 3]
    all_combinations(arr, [False] * len(arr), [])
