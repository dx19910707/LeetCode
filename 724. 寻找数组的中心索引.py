class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        TLE
        """
        for k, v in enumerate(nums):
            if sum(nums[:k]) == sum(nums[k+1:]):
                return k
        return -1

    def pivotIndex2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        68ms beats 53.75%
        """
        if len(nums) <= 1:
            return -1
        nums.append(0)
        left = 0
        right = sum(nums[1:])
        for i in range(len(nums)-1):
            if left == right:
                return i
            left += nums[i]
            right -= nums[i+1]
        return -1
