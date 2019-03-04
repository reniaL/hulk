# coding=utf-8


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def eraseOverlapIntervals(intervals):
    """
    有一个区间列表，问，最少去除几个区间，可以让剩下的区间不重叠？
    :type intervals: List[Interval]
    :rtype: int
    """
    intervals.sort(cmp=lambda x, y: x.start - y.start if x.end == y.end else x.end - y.end)
    valid = 1
    cur = 0
    for i in range(1, len(intervals)):
        if intervals[i].start >= intervals[cur].end:
            valid = valid + 1
            cur = i

    return len(intervals) - valid


if __name__ == '__main__':
    intervals = [Interval(1, 2), Interval(2, 5), Interval(3, 4), Interval(1, 3), Interval(2, 4)]
    print eraseOverlapIntervals(intervals)
