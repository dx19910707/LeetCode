class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        56ms beats: 99.92%
        """
        tmp1 = ''
        tmp2 = ''
        for i in s:
            if i in tmp2:
                if len(tmp2) > len(tmp1):
                    tmp1 = tmp2
                tmp2 = tmp2[tmp2.index(i) + 1:] + i
            else:
                tmp2 += i
        return max(len(tmp1), len(tmp2))
