class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == res:
                res = nums[i+1]
                i += 2
            else:
                break
        return res