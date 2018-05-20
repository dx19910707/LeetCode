class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start = None
        sublists = []
        res = 0
        for i in range(1,len(A)-1):
            if A[i+1] - A[i] == A[i] - A[i-1]:
                if start is None:
                    start = i-1
                if i == len(A) - 2:
                    sublists.append(A[start:])
            else:
                if start is not None:
                    sublists.append(A[start:i+1])
                    start = None
        for sublist in sublists:
            for i in range(3,len(sublist)+1):
                j = 0
                while j + i <= len(sublist):
                    res += 1
                    j += 1
        return res