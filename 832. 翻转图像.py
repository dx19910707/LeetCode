class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for i in A:
            for j in range(len(i)):
                if i[j] == 1:
                    i[j] = 0
                else:
                    i[j] = 1
            res.append(i[::-1])
        return res