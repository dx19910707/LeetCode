class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def get(i,j,row,col,M):
            l = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
            res = [m[i][j],1]
            for p in l:
                tmp = calc(i+p[0],j+p[1],row,col,M)
                res[0] += tmp[0]
                res[1] += tmp[1]
            return int(res[0]/res[1])
        def calc(i,j,row,col,M):
            if 0 <= i < row and 0 <= j <col:
                return [M[i][j],1]
            else:
                return [0,0]
        row = len(M)
        col = len(M[0])
        m = [x.copy() for x in M]
        for i in range(row):
            for j in range(col):
                m[i][j] = get(i,j,row,col,M)
        return m
