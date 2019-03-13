class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        36ms, beats: 6.12%
        """
        if len(nums) <= 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        lens = len(nums)
        middle = lens // 2
        if nums[middle] < nums[middle-1]:
            return self.findPeakElement(nums[:middle])
        elif nums[middle] < nums[middle+1]:
            return middle + self.findPeakElement(nums[middle:])
        else:
            return middle
