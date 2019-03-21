# coding=utf-8


class Solution(object):
    def fizzBuzz(self, n):
        """
        逢3输出 Fizz，逢5输出Buzz，3和5的公倍数则输出 FizzBuzz
        :type n: int
        :rtype: List[str]
        """
        result = [str(x) for x in range(1, n+1)]
        fizz = range(2, n, 3)
        buzz = range(4, n, 5)
        for i in fizz:
            result[i] = 'Fizz'
        for i in buzz:
            result[i] = 'Buzz' if result[i] != 'Fizz' else 'FizzBuzz'
        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.fizzBuzz(15)
