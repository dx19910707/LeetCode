class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        228ms
        """
        return self.judge(board) and self.judge_col(board) and self.judge_box(board)

    def judge(self, board):
        for i in board:
            i = list(filter(lambda x: x != '.', i))
            if len(set(i)) != len(i):
                return False
        return True

    def judge_col(self, board):
        new_board = zip(*board)
        return self.judge(new_board)

    def judge_box(self, board):
        new_board = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                new_board.append([board[x][y] for x in range(i,i+3) for y in range(j, j+3)])
        return self.judge(new_board)
