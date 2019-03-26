class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0
        col = len(A[0])
        for a in range(1, len(A)):
            r = A[a]
            for i in range(col):
                r[i] = min([r[i]+A[a-1][j] for j in range(i-1,i+2) if 0 <= j < col])
        return min(A[-1])
