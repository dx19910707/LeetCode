import itertools
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 直接获取所有排列去第K-1个， TLE
        l = [str(i) for i in range(1,n+1)]
        all_perm = list(itertools.permutations(l,n))
        return ''.join(all_perm[k-1])

    def getPermutation2(self, n, k):
        # 参考地址：https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
        l = [str(i) for i in range(1,n+1)]
        def helper(n,k,l):
            if n == 1:
                return l[0]
            fac = math.factorial(n-1)
            a = (k-1) // fac
            res = l[a]
            res += helper(n-1,k-(a*fac),l[:a]+l[a+1:])
            return res
        res = helper(n,k,l)
        return res