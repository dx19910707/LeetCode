class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        sorted_pairs = sorted(pairs,key=lambda x:x[0])
        res = 1
        tmp = sorted_pairs[0]
        for pair in sorted_pairs[1:]:
            if pair[1] < tmp[1]:
                tmp = pair
            elif pair[0] > tmp[1]:
                tmp = pair
                res += 1
        return res