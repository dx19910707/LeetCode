import itertools
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        nums.sort()
        for i in range(len(nums)+1):
            a = list(itertools.combinations(nums,i))
            l += [list(x) for x in set(a)]
        return l