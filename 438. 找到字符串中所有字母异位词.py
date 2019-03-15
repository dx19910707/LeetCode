class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        len_p = len(p)
        res = []
        d_p = {}
        for i in p:
            d_p[i] = d_p.get(i, 0) + 1
        d_t = {}
        for i in s[:len_p]:
            d_t[i] = d_t.get(i, 0) + 1
        for i in range(0, len(s)-len_p):
            if d_p == d_t:
                res.append(i)
            d_t[s[i]] -= 1
            if d_t[s[i]] == 0:
                del d_t[s[i]]
            d_t[s[len_p+i]] = d_t.get(s[len_p+i], 0) + 1
        if d_p == d_t:
            res.append(len(s) - len_p)
        return res
