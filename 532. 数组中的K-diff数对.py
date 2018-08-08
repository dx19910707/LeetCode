class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        80ms beats 44.14%
        状态不好，不想写代码，不想思考！！！！
        """
        if k < 0:
            return 0
        elif k == 0:
            d = {}
            for i in nums:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            res = 0
            for k, v in d.items():
                if v > 1:
                    res += 1
            return res
        else:
            nums = set(nums)
            d = {}
            s = set()
            for i in nums:
                a = i - k
                b = i + k
                if a in d:
                    s.add((a, i))
                else:
                    d[a] = i
                if i in d:
                    s. add((i, b))
                else:
                    d[i] = b
            return len(s)
