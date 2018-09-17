import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        44ms beats:96.15%
        """
        a = re.findall(r'\w+', s)
        new_s = ''.join(a).lower()
        if new_s == new_s[::-1]:
            return True
        return False
