class Solution(object):
    def validPalindrome(self, s, flag=True):
        """
        :type s: str
        :rtype: bool
        160ms
        """
        left = 0
        right = len(s) - 1
        while s[left] == s[right] and left < right:
            left += 1
            right -= 1
        if left >= right:
            return True
        if flag:
            s = s[left:right+1]
            return self.validPalindrome(s[1:], False) or self.validPalindrome(s[:-1], False)
        return False
