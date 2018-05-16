class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        while c % 2 == 0:
            c /= 2
            if c == 0:
                return True
        if sqrt(c) == int(sqrt(c)):
            return True
        d = {}
        for i in range(1,int(sqrt(c))+1):
            if i**2 in d:
                return True
            else:
                d[c - i**2] = i**2
        return False

    def judgeSquareSum2(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        i = 0
        j = int(sqrt(c))
        while i <= j:
            if i**2 + j**2 < c:
                i += 1
            elif i**2 + j**2 > c:
                j -=1
            else:
                return True
        return False