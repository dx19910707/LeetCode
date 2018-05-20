class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        l = []
        if len(nums) == 1:
            l += nums
        if len(nums) == 2:
            if nums[0] != nums[1]:
                l += nums
        for i in range(1,len(nums)-1):
            if i == 1:
                if nums[i-1] != nums[i]:
                    l.append(nums[i-1])
            if i == len(nums) - 2:
                if nums[i] != nums[i+1]:
                    l.append(nums[i+1])
            if nums[i-1] != nums[i] != nums[i+1]:
                l.append(nums[i])
        return l
