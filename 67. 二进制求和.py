class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        s2i可以替换成int(s,2)
        """
        def s2i(s):
            lens = len(s)
            interger = 0
            for i in s:
                if i == '1':
                    interger += 2**(lens-1)
                lens -=1
            return interger
        return bin(s2i(a)+s2i(b))[2:]