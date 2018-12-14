class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        48ms, beats: 63.89%
        """
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] < A[left + 1]:
                left += 1
            elif A[right] < A[right - 1]:
                right -= 1
            else:
                return left == right
        return left == right and right != len(A) - 1 and left != 0
