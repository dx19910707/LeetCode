class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        1280ms
        """
        nums = [i for i in range(1, n+1)]
        index = 1
        for i in range(1, k):
            nums = nums[:index] + nums[index:][::-1]
            index += 1
        return nums

    def constructArray2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        80ms
        """
        left = 1
        right = n
        i = 1
        res = []
        flag = k % 2 == 0
        while i <= k:
            if i % 2:
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
            i += 1
        t = [i for i in range(left, right+1)]
        if flag:
            t = t[::-1]
        res.extend(t)
        return res
