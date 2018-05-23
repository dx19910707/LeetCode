class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        l = sorted(d.items(),key= lambda x:x[1],reverse=True)
        c = sorted(d.values())
        res = ''
        for i in l:
            res += i[0] * i[1]
        return res