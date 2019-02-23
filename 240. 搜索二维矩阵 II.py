class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        56ms, beats 100%
        """
        if not matrix:
            return False
        row = len(matrix)
        x = 0
        y = len(matrix[0]) - 1
        while x < row and y >= 0:
            if target > matrix[x][y]:
                x += 1
            elif target < matrix[x][y]:
                y -= 1
            else:
                return True
        return False
