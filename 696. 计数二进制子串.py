class Solution(object):
    def countBinarySubstrings(self, s):
        l,tmp = [],1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                tmp += 1
            else:
                l.append(tmp)
                tmp = 1
        l.append(tmp)
        res = sum(min(a,b) for a,b in zip(l,l[1:]))
        return res