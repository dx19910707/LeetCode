class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        64ms
        """
        A.sort(reverse=True)
        lens = len(A)
        a = 0
        while a < lens - 2:
            if A[a + 1] + A[a + 2] > A[a]:
                return A[a] + A[a + 1] + A[a + 2]
            a += 1
        return 0
