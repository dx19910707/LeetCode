class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s = list(map(''.join,map(sorted,strs)))
        d = {}
        res = []
        for k,v in enumerate(s):
            if v in d:
                d[v].append(k)
            else:
                d[v] = [k]
        for v in d.values():
            res.append([strs[x] for x in v])
        return res