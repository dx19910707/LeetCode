class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        60ms, beats: 100%
        """
        lens = len(A)
        n = lens // 2
        d = {}
        for i in A:
            if i in d:
                if d[i] == n - 1:
                    return i
                d[i] += 1
            else:
                d[i] = 1
