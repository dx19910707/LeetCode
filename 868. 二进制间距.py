class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        28ms, beats: 85.26%
        """
        b = bin(N)
        start = None
        res = 0
        for k, v in enumerate(b[2:]):
            if v == '1':
                if start is None:
                    start = k
                else:
                    res = max(res, k - start)
                    start = k
        return res
