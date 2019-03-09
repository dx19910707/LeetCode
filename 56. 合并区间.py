# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        56ms, beats: 72.59%
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x.start)
        res = []
        cur = [intervals[0].start, intervals[0].end]
        for i in intervals[1:]:
            if i.start <= cur[1]:
                cur[1] = max(cur[1], i.end)
            else:
                res.append(Interval(cur[0], cur[1]))
                cur = [i.start, i.end]
        res.append(Interval(cur[0], cur[1]))
        return res
