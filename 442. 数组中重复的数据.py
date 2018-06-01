class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(n)time and O(n)space
        res = []
        c = nums.copy()
        for i in range(len(nums)):
            if c[nums[i]-1] == -1:
                res.append(nums[i])
            else:
                c[nums[i]-1] = -1
        return res
