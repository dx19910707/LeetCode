class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for i in str:
            o = ord(i)
            if 65 <= o <= 90:
                o += 32
                res += chr(o)
            else:
                res += i
        return res
        # one_liner
        # return ''.join([chr(ord(i) + 32) if 65 <= ord(i) <= 90 else i for i in str])
