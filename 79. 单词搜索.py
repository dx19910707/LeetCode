import copy


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        2180ms, beats: 0.97%
        """
        if not board or not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = self.recursive(board, word[1:],[i, j], {(i, j)})
                    if res == 1:
                        return True
                    elif res == 2:
                        return False
        return False

    def recursive(self, board, word, start_index,seen):
        if not word:
            return 1
        direction = [ (0, 1), (1, 0) , (-1, 0), (0, -1),]
        for i in direction:
            x = start_index[0] + i[0]
            y = start_index[1] + i[1]
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in seen:
                tmp = copy.deepcopy(seen)
                if board[x][y] == word[0]:
                    seen.add((x, y))
                    res = self.recursive(board, word[1:], [x, y], seen)
                    if res in [1,2]:
                        return res
                if len(seen) + 1 == len(board) * len(board[0]):
                    return 2
                seen = copy.deepcopy(tmp)
        return 0
