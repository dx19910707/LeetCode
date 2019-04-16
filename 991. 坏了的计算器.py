class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        28ms, beats: 55.91%
        """
        res = 0
        while Y > X:
            res += 1
            if Y % 2 == 1:
                Y += 1
            else:
                Y /= 2
        return res + X - Y
