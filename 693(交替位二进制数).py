class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)
        str_n = str(b)[2:]  # 去掉0b
        t = None
        for i in str_n:
            if t is not None:
                if t == i:
                    return False
            t = i
        return True

    def hasAlternatingBits2(self, n):
        tmp = n & 1
        while n:
            tmp_1 = (n >> 1) & 1
            if tmp == tmp_1:
                return False
            tmp = tmp_1
            n = n >> 1
        return True

