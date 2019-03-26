class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        mid = len(nums) // 2
        return sum([abs(nums[mid]-i) for i in nums])
