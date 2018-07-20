class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        28ms beat 100%
        """
        def change(list):
            for i in range(len(list)):
                if list[i] == 0:
                    list[i] = 1
                else:
                    list[i] = 0
            return list

        for row in A:
            if row[0] == 0:
                change(row)
        zip_a = list(zip(*A))
        tmp = []
        for row in zip_a:
            if row.count(0) > row.count(1):
                row = change(list(row))
            tmp.append(row)
        result = list(zip(*tmp))
        res = 0
        for row in result:
            s = ''
            for i in row:
                s += str(i)
            res += int(s, 2)
        return res
