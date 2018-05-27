class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = []
        for j in matrix:
            for i in j:
                l.append(i)
        l.sort()
        return l[k-1]