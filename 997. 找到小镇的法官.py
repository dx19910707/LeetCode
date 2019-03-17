class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        144ms
        """
        if not trust:
            if N == 1:
                return 1
            return -1
        a,b = list(zip(*trust))
        a = set(a)
        d = {}
        for i in b:
            d[i] = d.get(i, 0) + 1
        for k, v in d.items():
            if k not in a and v == N - 1:
                return k
        return -1
