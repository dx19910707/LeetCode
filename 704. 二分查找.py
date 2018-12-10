class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        40ms: beats 84.65%
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]
        if target > left[-1]:
            index = self.search(right, target)
            return index if index == -1 else len(left) + index
        else:
            return self.search(left, target)
