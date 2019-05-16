class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.strip()) == 0:
            return 0

        return len(s.split())


if __name__ == '__main__':
    s = "hello, my name is   Terry.  "
    instance = Solution()
    print instance.countSegments(s)
