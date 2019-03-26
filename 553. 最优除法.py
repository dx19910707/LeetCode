class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = str(nums[0])
        if len(nums) == 2:
            res += '/' + str(nums[1])
        elif len(nums) > 2:
            res += '/('
            for i in range(1, len(nums)):
                res += str(nums[i])
                if i != len(nums) - 1:
                    res += '/'
                else:
                    res += ')'
        return res
