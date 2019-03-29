# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            t1 = A[i]
            t2 = B[j]
            if t1.end >= t2.start and t1.start <= t2.end:
                start = max(t1.start, t2.start)
                end = min(t1.end, t2.end)
                if t1.end >= t2.end:
                    j += 1
                else:
                    i += 1
                res.append(Interval(start, end))
            elif t2.end >= t1.start and t2.start <= t1.end:
                start = max(t1.start, t2.start)
                end = min(t1.end, t2.end)
                if t2.end >= t1.end:
                    i += 1
                else:
                    j += 1
                res.append(Interval(start, end))
            elif t1.end < t2.start:
                i += 1
            elif t2.end < t1.start:
                j += 1
        return res
