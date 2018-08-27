class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        28ms beats: ?
        """
        res = []
        d = {}
        for a in A.split():
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        for b in B.split():
            if b in d:
                d[b] += 1
            else:
                d[b] = 1
        for k, v in d.items():
            if v == 1:
                res.append(k)
        return res
