class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        2496ms !!!!
        """
        if K > len(points):
            return points
        points_values = [i[0] ** 2 + i[1] ** 2 for i in points]
        tmp = sorted(points_values)
        res = []
        for i in tmp[:K]:
            index = points_values.index(i)
            res.append(points[index])
            points_values[index] = -1
        return res

    def kClosest2(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        556ms
        """
        import heapq
        return heapq.nsmallest(K, points, lambda x_y: x_y[0] * x_y[0] + x_y[1] * x_y[1])

    def kClosest3(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        440ms
        """
        return sorted(points, key=lambda x: x[0] * x[0] + x[1] + x[1])[:K]


s = Solution()
p = [[3,3],[5,-1],[-2,4]]
k = 2
r = s.kClosest(p, k)
print(r)
