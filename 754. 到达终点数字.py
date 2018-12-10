class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        108ms, beats: 37.84%
        """
        target = abs(target)
        count = 0
        step = 0
        while True:
            if count == target:
                return step
            step += 1
            count += step
            if count > target:
                tmp = count - target
                if tmp % 2 == 0:
                    return step
