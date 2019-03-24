class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        72ms, beats: 12.63%
        """
        d1 = {}
        res = []
        for i in nums1:
            d1[i] = d1.get(i, 0) + 1
        for i in nums2:
            if d1.get(i, 0) > 0:
                res.append(i)
                d1[i] -= 1
        return res
