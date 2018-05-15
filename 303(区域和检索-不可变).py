class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        先累加算出列表每一项之前的和，leetcode使用itertools.accumulate()报错
        """
        self.nums = nums
        self.accu = [0] * (len(nums)+1)
        for k,v in enumerate(nums):
            self.accu[k] = self.accu[k-1] + v

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j] - self.accu[i-1]
