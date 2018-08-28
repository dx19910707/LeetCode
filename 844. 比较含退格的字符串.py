class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        28ms beats:100%
        """
        str_s = ''
        str_t = ''
        for s in S:
            if s == '#':
                str_s = str_s[:-1]
            else:
                str_s += s
        for t in T:
            if t == '#':
                str_t = str_t[:-1]
            else:
                str_t += t
        if str_s == str_t:
            return True
        return False
