class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        d = {}
        res = 0
        for i in answers:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for k,v in d.items():
            if  v %(k+1) == 0:
                b = v // (k+1)
            else:
                b = v // (k+1) +1
            res += b * (k+1)
        return res
