class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n-1
        elif n == 4:
            return n
        res = 1
        while n - 3 > 1:
            res *= 3
            n = n-3
        res *= n
        return res