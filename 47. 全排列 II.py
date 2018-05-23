class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        l = [list(x) for x in set(itertools.permutations(nums))]
        return l