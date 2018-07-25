class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        48ms beats: 82.35%
        """
        pre = None
        res = 0
        for index, value in enumerate(seats):
            if value == 1:
                if pre is None:
                    res = index
                    pre = index
                else:
                    if (index - pre) / 2 == (index - pre) // 2:
                        res = max((index - pre) // 2, res)
                    else:
                        res = max((index - pre) // 2 + 1, res)
                    pre = index

        res = max(len(seats) - 1 - pre, res)

        return res
