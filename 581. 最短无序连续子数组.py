class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = sorted(nums)
        if nums == nums2:
            return 0
        i = 0
        while nums[i] == nums2[i]:
            i += 1
        j = -1
        while nums[j] == nums2[j]:
            j -= 1
        return len(nums[i:j])+1