class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        40ms, beats: 100%
        """
        A = sorted(A, key=lambda x:len(x))
        base = {}
        for i in A[0]:
            base[i] = base.get(i, 0) + 1
        res = []
        for k, v in base.items():
            for j in A[1:]:
                v = min(j.count(k), v)
                if v == 0:
                    break
            res.extend([k] * v)
        return res
