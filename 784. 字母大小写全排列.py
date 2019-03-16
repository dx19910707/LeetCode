class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        84ms, beats: 69.78%
        """
        res = []
        for k, v in enumerate(S):
            if v.isalpha():
                tmp = []
                if res:
                    for r in res:
                        tmp.append(r[:k] + v.upper() + S[k+1:])
                        tmp.append(r[:k] + v.lower() + S[k+1:])
                else:
                    tmp.append(S[:k] + v.upper() + S[k+1:])
                    tmp.append(S[:k] + v.lower() + S[k+1:])
                res = tmp
        return res or [S]
