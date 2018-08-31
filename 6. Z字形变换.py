class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        932ms beats: 8.52%!!!!!!!!!!!!!!
        """
        if len(s) <= numRows or numRows == 1:
            return s

        col = len(s) // numRows
        l1 = [['' for __ in range(col * numRows)] for _ in range(numRows)]
        x = y = 0
        tmpx = tmpy = 0
        for i in s:
            if tmpx < numRows:
                l1[x][y] = i
                tmpx += 1
                if tmpx == numRows:
                    tmpy = numRows - 2
                else:
                    x += 1
            else:
                x -= 1
                y += 1
                l1[x][y] = i
                if x == 0:
                    tmpx = 1
                    x = 1
                else:
                    tmpy -= 1
                    if tmpy < 0:
                        tmpx = 0

        res = ''
        for i in l1:
            res += ''.join(i)

        return res
