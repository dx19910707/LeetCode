class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        i = 1
        while len(A) * i <= len(B) * 2:
            if B in A*i:
                return i
            i += 1
        if B in A*i:
            return i
        return -1