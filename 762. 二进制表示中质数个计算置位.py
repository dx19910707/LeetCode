class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        L,R最大值为10**6，转换为2进制后最多有20位
        """
        l = [2,3,5,7,11,13,17,19,23]
        count = 0
        for i in range(L,R+1):
            n = bin(i).count('1')
            if n in l:
                count += 1
        return count