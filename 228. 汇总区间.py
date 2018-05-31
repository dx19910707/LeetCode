class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        mi = ma = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > ma + 1:
                if mi == ma:
                    res.append(str(mi))
                else:
                    res.append('%s->%s'%(mi,ma))
                mi = ma = nums[i]
            else:
                ma = nums[i]
        if mi == ma:
            res.append(str(mi))
        else:
            res.append('%s->%s' % (mi, ma))
        return res