class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        1052ms, beats: 22.40%
        """
        seen = {}
        res = []
        nums = sorted(nums)
        for k, v in enumerate(nums):
            if v in seen:
                continue
            new_target = 0 - v
            seen[v] = new_target
            new_start = k + 1
            seen2 = {}
            used = set()
            for k1, v1 in enumerate(nums[new_start:]):
                if v1 in used:
                    continue
                elif v1 in seen2:
                    res.append([v, seen2[v1], v1])
                    used.add(v1)
                final_target = new_target - v1
                seen2[final_target] = v1

        return res


n = [-1, 0, 1, 2, -1, -4]
s = Solution()
r = s.threeSum(n)
print(r)
