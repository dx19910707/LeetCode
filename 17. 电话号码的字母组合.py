class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if not digits:
            return []
        res = ['']
        tmp = []
        for i in digits:
            for a in res:
                for b in d[i]:
                    tmp.append(a+b)
            res = tmp
            tmp = []
        return res