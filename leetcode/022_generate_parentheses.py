# coding=utf-8


def generateParenthesis(n):
    """
    n对括号，返回所有有效匹配的列表
    :type n: int
    :rtype: List[str]
    """
    cur = ""
    output = []
    generate(n, cur, output, n, n)
    return output


def generate(n, cur, output, left, right):
    if left > right:
        return

    if left == 0 and right == 0:
        output.append(cur)
        return

    if left > 0:
        generate(n, cur + "(", output, left-1, right)

    if right > 0:
        generate(n, cur + ")", output, left, right-1)


if __name__ == '__main__':
    for x in generateParenthesis(3):
        print x
