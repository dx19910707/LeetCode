class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        28ms, beats: 97.81%
        """
        d = {}
        for k, v in enumerate(nums):
            if v in d:
                return [d[v], k]
            d[target - v] = k
