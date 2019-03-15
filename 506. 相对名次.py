class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        76ms, beats: 56.29%
        """
        d = {k: v for k, v in enumerate(nums)}
        rank_index_list = sorted(d.keys(), key=lambda x: -d[x])
        first_three = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for k, v in enumerate(rank_index_list):
            if k <= 2:
                nums[v] = first_three[k]
            else:
                nums[v] = str(k + 1)
        return nums
