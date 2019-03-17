class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        140ms, beats: 42.25%
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        d = sorted(d.items(), key=lambda x:x[0])
        res = 0
        for i in range(len(d)-1):
            if d[i+1][0] - d[i][0] == 1:
                res = max(res, d[i+1][1] + d[i][1])
        return res

    def findLHS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        反向优化牛逼4500ms
        """
        s = sorted(set(nums))
        res = 0
        for i in range(len(s)-1):
            if s[i] + 1 == s[i+1]:
                res = max(res, nums.count(s[i]) + nums.count(s[i+1]))
        return res

    def findLHS3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        100ms, beats: 80.99%
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        res = 0
        for k, v in d.items():
            if k + 1 in d:
                if d[k] + d[k+1] > res:
                    res = d[k] + d[k+1]
        return res
