class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        112ms, beats:59.55%
        """
        i = 0
        lens = len(S)
        mmin, mmax = 0, lens
        if S[0] == 'I':
            res = [0]
            mmin += 1
        else:
            res = [lens]
            mmax -= 1
        while i < lens:
            if i < lens - 1:
                if S[i + 1] == 'I':
                    res.append(mmin)
                    mmin += 1
                else:
                    res.append(mmax)
                    mmax -= 1
            else:
                res.append(mmin)
            i += 1
        return res
