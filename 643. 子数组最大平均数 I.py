class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        使用max, 224ms, beats: 70.78%
        """
        pre_sum = max_sum = sum(nums[:k])
        for i in range(0, len(nums) - k):
            pre_sum = pre_sum - nums[i] + nums[i+k]
            max_sum = max(max_sum, pre_sum)
        return max_sum / k

    def findMaxAverage2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        不使用max, 176ms, beats: 96.43%
        """
        pre_sum = max_sum = sum(nums[:k])
        for i in range(0, len(nums) - k):
            pre_sum = pre_sum - nums[i] + nums[i+k]
            if pre_sum > max_sum:
                max_sum = pre_sum
        return max_sum / k

