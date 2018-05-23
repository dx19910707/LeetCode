class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        s = 0
        for i in range(len(timeSeries)-1):
            s += min(timeSeries[1:][i]-timeSeries[:-1][i],d)
        if timeSeries:
            s += duration
        return s