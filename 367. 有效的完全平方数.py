class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        32ms, beats: 25.62%
        """
        low = 0
        high = num
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 < num:
                low = mid + 1
            elif mid ** 2 > num:
                high = mid - 1
            else:
                return True
        return False

