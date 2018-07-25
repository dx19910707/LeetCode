class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        24ms beats:100%
        """
        s = s.strip()
        l = s.split(' ')
        if not l:
            return 0
        return len(l[-1])
