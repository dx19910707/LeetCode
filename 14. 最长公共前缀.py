class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        36ms beats:74.39%
        """
        if not strs:
            return ''
        key = strs[0]
        i = 1
        res = ''
        while i <= len(key):
            for j in strs[1:]:
                if key[:i] != j[:i]:
                    return res
            res = key[:i]
            i += 1
        return res
