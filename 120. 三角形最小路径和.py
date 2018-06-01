class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        i = 1
        while i < len(triangle):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
            for j in range(1,len(triangle[i])-1):
                triangle[i][j] = min(triangle[i][j]+triangle[i-1][j-1],triangle[i][j]+triangle[i-1][j])
            i += 1
        return min(triangle[-1])
