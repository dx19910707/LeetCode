def guess(n):
    # if n == N:
    #     return 0
    # elif n < N:
    #     return 1
    # else:
    #     return -1
    pass

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        24ms beats 99.21%
        """
        mid = n // 2
        while guess(mid) != 0:
            if guess(mid) == 1:
                if n - mid == 1:
                    mid += 1
                else:
                    mid = (n - mid) // 2 + mid
            else:
                n = mid
                mid = mid // 2

        return mid
