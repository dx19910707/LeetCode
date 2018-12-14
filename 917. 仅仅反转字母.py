class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        24ms, beats: 100%
        """
        left = 0
        right = len(S) - 1
        new_s = [''] * len(S)
        while left <= right:
            if not S[left].isalpha():
                new_s[left] = S[left]
                left += 1
            elif not S[right].isalpha():
                new_s[right] = S[right]
                right -= 1
            else:
                new_s[left] = S[right]
                new_s[right] = S[left]
                left += 1
                right -= 1
        return ''.join(new_s)
