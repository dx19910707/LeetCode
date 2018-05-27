class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        m = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > m:
                m = nums[i+1] - nums[i]
        return m