class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if i == 0:
                    nums[i] = nums[i+1]
                else:
                    if nums[i+1] > nums[i-1]:
                        nums[i] = nums[i+1]
                    else:
                        nums[i+1] = nums[i]
                break
        return nums == sorted(nums)