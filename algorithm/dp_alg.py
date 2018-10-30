# coding=utf-8


def run_coins_simple(target):
    """
    最少需要多少个硬币，才能凑到 target 这个数
    仅输出硬币个数
    """
    result_count = [0]

    for i in range(1, target + 1):
        temp = []
        for coin in [1, 3, 5]:
            if i - coin >= 0:
                temp.append(result_count[i - coin] + 1)

        result_count.append(min(temp))

    print result_count


def run_coins(target):
    """
    最少需要多少个硬币，才能凑到 target 这个数。输出结果硬币列表
    """
    result_count = [0]  # 每个 target 的解
    chosen_coins = []  # 每个 target 所选取的最后一个硬币面值

    for i in range(1, target + 1):
        chosen_coin = 100
        temp_count = 100
        for coin in [1, 3, 5]:
            if i - coin >= 0 and (result_count[i - coin] + 1) < temp_count:
                temp_count = result_count[i - coin] + 1
                chosen_coin = coin

        chosen_coins.append(chosen_coin)
        result_count.append(temp_count)

    # 从后往前追溯，拼接出硬币列表
    result_coins = []
    index = target - 1
    while index >= 0:
        result_coins.append(chosen_coins[index])
        index = index - chosen_coins[index]

    print result_coins


def run_points(length):
    """
    切钢条（木头），长度为 length，输出最佳的价格
    """
    result = [0]
    points = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for i in range(1, length + 1):
        temp = []
        for cut_length in range(1, 11):
            if i - cut_length >= 0:
                temp.append(result[i - cut_length] + points[cut_length])

        result.append(max(temp))

    print result[-1]


def run_brick_stack(height):
    """
    用砖头砌墙，有几种特定高度的砖头，能否砌出高度为 height 的墙
    """
    result = [True]
    bricks = [7, 11]
    for i in range(1, height + 1):
        cur_result = False
        for brick in bricks:
            if i - brick >= 0 and result[i-brick]:
                cur_result = True
        result.append(cur_result)
    print result[-1]

def run_sum_path(tree):
    """
    树的最佳求和路径
    TODO 路径输出还有问题
    """
    result_nodes = []  # 每个节点的最佳路径和
    result_layer = []  # 每一层的最佳路径和
    result_node_index = []
    last_node_index = 0

    for i in range(0, len(tree)):
        result_nodes.append([])
        result_node_index.append([])
        for j in range(0, len(tree[i])):
            node_sum_left = 0 if (i == 0 or j == 0) else result_nodes[i-1][j-1]  # 当前节点的左上节点
            node_sum_right = 0 if (i == 0 or j == len(tree[i]) - 1) else result_nodes[i-1][j]  # 当前节点的右上节点
            result_nodes[i].append(max(node_sum_left, node_sum_right) + tree[i][j])
            result_node_index[i].append(j if node_sum_left < node_sum_right else j-1)

        layer_max = 0
        for k in range(0, len(result_nodes[i])):
            if result_nodes[i][k] > layer_max:
                layer_max = result_nodes[i][k]
                last_node_index = k

        result_layer.append(layer_max)

    print result_layer

    for layer in tree:
        print layer

    # for layer in result_node_index:
    #     print layer

    i = len(tree) - 1
    j = last_node_index
    result_path = [tree[i][j]]
    while i > 0:
        i = i-1
        j = result_node_index[i][j]
        result_path.append(tree[i][j])

    print result_path


def climbing_stairs(steps):
    """
    有 steps 级楼梯，每次可以爬1级或两级，共有多少种方法
    """
    result = [0, 1, 2]
    for i in range(3, steps+1):
        result.append(result[i-1] + result[i-2])
    print result


if __name__ == '__main__':
    # run_coins_simple(14)
    # run_coins(14)
    # run_points(20)

    climbing_stairs(10)

    # tree = [
    #     [1],
    #     [3, 5],
    #     [8, 2, 9],
    #     [7, 4, 3, 1],
    #     [2, 4, 8, 5, 6],
    #     [3, 7, 8, 6, 1, 2],
    #     [8, 6, 5, 9, 1, 2, 6],
    #     [7, 1, 4, 2, 9, 5, 3, 8],
    #     [6, 4, 1, 9, 3, 5, 2, 7, 8]
    # ]
    # run_sum_path(tree)
