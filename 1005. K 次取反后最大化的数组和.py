class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        28ms, beats:100%
        """
        A.sort()
        i = 0
        while A[i] < 0 < K :
            A[i] = -A[i]
            i += 1
            K -= 1
        if K == 0:
            return sum(A)
        elif K % 2 == 0:
            return sum(A)
        else:
            return sum(A) - 2 * min(A)
