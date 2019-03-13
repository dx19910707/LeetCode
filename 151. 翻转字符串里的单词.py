class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        24ms, beats: 99.78%
        """
        return ' '.join(s.split()[::-1])
