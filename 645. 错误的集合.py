class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        TLE
        """
        lens = len(nums)
        l = range(1, lens+1)
        res = []
        for i in l:
            try:
                nums.remove(i)
            except:
                res.append(i)
        res = nums + res
        return res

    def findErrorNums2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        116ms beats:11.96%
        """
        nums = sorted(nums)
        i = 0
        lens = len(nums)
        flag = False
        first = []
        second = []
        while i < lens:
            if flag:
                if i + 1 == nums[i]:
                    if first:
                        first.append(i)
                    else:
                        second.insert(0, nums[i])
                    break
            else:
                if i + 1 > nums[i]:
                    first.append(nums[i])
                    flag = True
                elif i + 1 < nums[i]:
                    second.append(i+1)
                    flag = True
            i += 1
        if len(first) == 1:
            first.append(lens)
        return first or second
