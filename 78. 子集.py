class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        res = []
        for i in range(len(nums)+1):
            res += [list(x) for x in itertools.combinations(nums,i)]
        return res