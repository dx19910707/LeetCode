import itertools


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        36ms
        """
        h = [1,2,4,8]
        m = [1,2,4,8,16,32]
        res = []
        i = 0
        while i <= num:
            h1 = [str(sum(x)) for x in itertools.combinations(h, i) if sum(x) < 12]
            m1 = [str(sum(x)) if sum(x) > 9 else '0' + str(sum(x)) for x in itertools.combinations(m, num-i) if sum(x) < 60]
            res += ['{}:{}'.format(x, y) for x in h1 for y in m1]
            i += 1
        return res
