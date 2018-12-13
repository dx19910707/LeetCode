class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        40ms, beats: 82.81%
        """
        lens = len(deck)
        if lens <= 1:
            return False
        d = {}
        for i in deck:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        middle = lens // 2

        for i in range(2, middle + 2):
            if lens % i == 0:
                if all(map(lambda x: x % i == 0, d.values())):
                    return True
        return False
