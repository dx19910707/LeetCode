import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        a = collections.Counter(nums)
        b = a.most_common(k)
        return [x[0] for x in b]