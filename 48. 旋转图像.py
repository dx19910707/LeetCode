class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        tmp = [[] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                tmp[i].insert(0,matrix[j][i])
        matrix[:] = tmp[:]

    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        z = list(zip(*matrix))
        matrix[:] = z[:]
