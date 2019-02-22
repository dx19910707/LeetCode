class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        n = lens / 3
        seen = set()
        res = []
        for i in nums:
            if i in seen:
                continue
            seen.add(i)
            if nums.count(i) > n:
                res.append(i)
        return res
