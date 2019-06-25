class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = []
        for i in S:
            if l and i == l[-1]:
                l.pop()
            else:
                l.append(i)
        return "".join(l)
