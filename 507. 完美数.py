class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        24ms beats:100%
        """
        if num in [6, 28, 496, 8128, 33550336]:
            return True
        return False
