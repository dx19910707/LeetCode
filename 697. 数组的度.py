class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for k,v in enumerate(nums):
            if v in d:
                d[v].append(k)
            else:
                d[v] = [k]
        max_lens = 0
        res = 1
        for i in d.values():
            if len(i) > max_lens:
                max_lens = len(i)
                res = i[-1] - i[0] + 1
            elif len(i) == max_lens:
                res = min(i[-1] - i[0] + 1,res)
        return res