class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        普通
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        x = d.get(0,0)
        y = d.get(1,0)
        z = d.get(2,0)

        nums[:x] = [0] * x
        nums[x:x+y] = [1] * y
        nums[x+y:] = [2] * z

    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        进阶
        """
        start = 0
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == 0:
                nums[start],nums[i] = nums[i],nums[start]
                start += 1
                i += 1
            elif nums[i] == 2:
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
            else:
                i += 1