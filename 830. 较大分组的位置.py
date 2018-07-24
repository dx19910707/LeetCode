class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        56ms beats 68.13%
        """
        tmp = ('', [0, 0])
        res = []
        for k, v in enumerate(S):
            if v == tmp[0]:
                tmp[1][1] = k
            else:
                count = tmp[1][1] - tmp[1][0]
                if count >= 2:
                    res.append(tmp[1])
                tmp = (v, [k, k])

        count = tmp[1][1] - tmp[1][0]
        if count >= 2:
            res.append(tmp[1])

        return res
