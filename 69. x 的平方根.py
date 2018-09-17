class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        1380ms beats: 3.69%~~~~~~
        """
        left = x // 2
        right = x
        while left ** 2 > x:
            right = left
            left = left // 2
        for i in range(left, right + 1):
            if i ** 2 == x:
                return i
            elif i ** 2 >= x:
                return i - 1
