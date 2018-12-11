class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        72ms, beats: 99.21%
        """
        if len(A) <= 1:
            return True
        flag = None
        now = A[0]
        for i in A[1:]:
            pre, now = now, i
            if now > pre:
                if flag and flag != 'dz':
                    return False
                flag = "dz"
            elif now < pre:
                if flag and flag != 'dj':
                    return False
                flag = 'dj'
        return True
