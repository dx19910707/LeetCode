class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        32ms, beats: 98.72%
        """
        lens = len(cost)
        f = [0] * lens
        f[:2] = cost[:2]
        for i in range(2, lens):
            f[i] = min(f[i-1], f[i-2]) + cost[i]
        m = min(f[-1], f[-2])
        return m

    def minCostClimbingStairs2(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        32ms, beats: 98.72%
        """
        lens = len(cost)
        m1 = cost[0]
        m2 = cost[1]
        for i in range(2, lens):
            m1, m2 = m2, cost[i] + min(m1, m2)
        return min(m1, m2)
