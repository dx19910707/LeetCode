class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        lens = len(nums)
        close = nums[0] + nums[1] + nums[2]
        close_num = abs(target - close)
        for k, v in enumerate(nums[:-2]):
            l, r = k + 1, lens - 1
            while l < r:
                num = nums[l] + nums[r] + v
                if num < target:
                    dis = abs(target - num)
                    if dis < close_num:
                        close_num = dis
                        close = num
                    l += 1
                elif num > target:
                    dis = abs(target - num)
                    if dis < close_num:
                        close_num = dis
                        close = num
                    r -= 1
                else:
                    return target
        return close


n = [-5, -4, 0, 1]
t = 0

s = Solution()
a = s.threeSumClosest(n, t)
print(a)
