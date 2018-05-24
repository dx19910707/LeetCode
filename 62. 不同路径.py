class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [[1] * m for i in range(n)]
        for j in range(1,n):
            for i in range(1,m):
                l[j][i] = l[j-1][i] + l[j][i-1]
        return l[-1][-1]