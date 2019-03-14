class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        24ms, beats: 93.43%
        """
        d = {i: chr(64+i) for i in range(1,27)}
        res = ''
        while n > 26:
            t = n % 26
            if t == 0:
                res = 'Z' + res
                n = n // 26 - 1
            else:
                res = d[t] + res
                n = n // 26
        res = d[n] + res
        return res
