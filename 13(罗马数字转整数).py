class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        while len(s) > 1:
            if d[s[0]] < d[s[1]]:
                res += d[s[1]] - d[s[0]]
                s = s[2:]
            else:
                res += d[s[0]]
                s = s[1:]
        return res if len(s) == 0 else res + d[s[0]]