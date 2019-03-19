# coding=utf-8


# Definition for a Node.
class Node(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """计算一棵 N 叉树的前序遍历节点列表
        :type root: Node
        :rtype: List[int]
        """
        values = []
        self.process(root, values)
        return values

    def process(self, node, values):
        if node:
            values.append(node.val)
            if node.children:
                for n in node.children:
                    self.process(n, values)


if __name__ == '__main__':
    solution = Solution()
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    root = Node(1, [Node(11), Node(12, [Node(121), Node(122), Node(123)]), Node(13)])
    root = Node(1, [Node(11), Node(12, [Node(121, [Node(1211), Node(1212)]), Node(122), Node(123)]), Node(13)])
    print solution.preorder(root)
