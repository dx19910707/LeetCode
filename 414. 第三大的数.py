class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        164ms
        """
        if not nums:
            return 0
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        a = nums[:3]
        a.sort(reverse=True)
        for i in nums[3:]:
            if i > a[2]:
                t = 2
                while i > a[t] and t >= 0 :
                    t -= 1
                index = t + 1
                a.insert(index, i)
                a.pop()
        return a[2]

    def thirdMax2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        92ms
        """
        if not nums:
            return 0
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        t = nums[:3]
        t.sort()
        first = t[2]
        second = t[1]
        third = t[0]
        for i in nums[3:]:
            if i > third:
                if i > second:
                    if i > first:
                        first, second, third = i, first, second
                    else:
                        second, third = i, second
                else:
                    third = i
        return third
