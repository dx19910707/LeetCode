class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        24ms, beats: 99.51%
        """
        if not matrix:
            return []

        self.col = self.min_col = self.min_row = 0
        self.max_col = len(matrix[0])
        self.max_row = len(matrix)
        self.times = self.max_col * self.max_row
        self.time = 0
        res = []

        def right():
            if len(res) == self.times:
                return res
            tmp = matrix[self.min_row]
            for i in tmp[self.min_col: self.max_col]:
                res.append(i)
            self.max_col -= 1
            down()
            return res

        def down():
            if len(res) == self.times:
                return res
            for i in range(self.min_row + 1, self.max_row):
                res.append(matrix[i][self.max_col])
            self.max_row -= 1
            left()
            return res

        def left():
            if len(res) == self.times:
                return res
            tmp = matrix[self.max_row]
            for i in tmp[self.min_col:self.max_col][::-1]:
                res.append(i)
            self.min_col += 1
            up()
            return res

        def up():
            if len(res) == self.times:
                return res
            for i in range(self.max_row - 1, self.min_row, -1):
                res.append(matrix[i][self.min_col - 1])
            self.min_row += 1
            right()
            return res

        result = right()
        return result
