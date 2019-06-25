class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq
        new_stones = list(map(lambda x: -x, stones))
        heapq.heapify(new_stones)
        while new_stones:
            if len(new_stones) == 1:
                return -new_stones[0]
            x = heapq.heappop(new_stones)
            y = heapq.heappop(new_stones)
            if x == y:
                continue
            heapq.heappush(new_stones, x - y)
        return 0
