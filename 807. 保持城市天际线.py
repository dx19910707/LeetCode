class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid1 = list(zip(*grid))
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(max(grid[i]),max(grid1[j])) - grid[i][j]
        return res