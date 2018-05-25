class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d = {}
        for i in T:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        res = ''
        for i in S:
            if i in d:
                res += i * d[i]
                d.pop(i)
        for k,v in d.items():
            res += k*v
        return res
