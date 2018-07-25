class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        964ms beats:15.19%
        """
        i = 0
        sum = 0
        while True:
            if sum == n:
                return i
            elif sum > n:
                return i - 1
            i += 1
            sum += i
