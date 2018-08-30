class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        TLE
        """
        sum_a = sum(A)
        sum_b = sum(B)

        diff = (sum_a - sum_b) // 2
        for i in A:
            if i - diff in B:
                return [i, i - diff]

    def fairCandySwap2(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        88ms beats: ?
        """
        sum_a = sum(A)
        sum_b = sum(B)
        d = {}

        diff = (sum_a - sum_b) // 2
        for i in A:
            d[i - diff] = i
        for j in B:
            if j in d:
                return [d[j], j]
