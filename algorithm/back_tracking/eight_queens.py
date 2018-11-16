# coding=utf-8
from datetime import datetime


def is_valid(matrix):
    """
    check if matrix valid for n-queens
    :param matrix: means place at row i, column matrix[i]
    :return: True if valid, otherwise False
    """
    result = True
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i] == matrix[j] or (j-i) == abs(matrix[i]-matrix[j]):
                result = False
    # print "check: ", matrix, "result: ", result
    return result


def solve1(i, n, matrix):
    """
    simple solution to n-queens, by backtracking
    :param i: start from this row
    :param n: total row count
    :param matrix: start from this placement, every element means place at row i, column matrix[i]
    :return: True if valid with current initial matrix, otherwise False
    """
    if i == n:
        if is_valid(matrix):
            print "result: ", matrix
            return True
        else:
            return False

    for j in range(n):
        matrix.append(j)
        if is_valid(matrix) and solve1(i+1, n, matrix):
            return True
        matrix.pop()
    return False


def solve2(i, n, matrix):
    """
    print all solutions to n-queens
    :param i: start from this row
    :param n: total row count
    :param matrix: start from this placement, every element means place at row i, column matrix[i]
    """
    for j in range(n):
        matrix.append(j)
        if is_valid(matrix):
            if i+1 == n:
                print "result:", matrix
            else:
                solve2(i + 1, n, matrix)
        matrix.pop()


if __name__ == '__main__':
    start = datetime.now()
    solve2(0, 8, [])
    print "time: ", (datetime.now() - start).microseconds
