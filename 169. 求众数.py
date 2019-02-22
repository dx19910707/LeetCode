class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        36ms, 8.2MB, beats:90.07%
        """
        lens = len(nums)
        n = lens / 2
        seen = set()
        for i in nums:
            if i in seen:
                continue
            seen.add(i)
            if nums.count(i) > n:
                return i
