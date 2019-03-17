class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        688ms, beats: 5.28%
        """
        n1 = n2 = 0
        len1 = len(num1)
        len2 = len(num2)
        for i in num1:
            n1 += (ord(i) - 48) * 10 ** (len1 - 1)
            len1 -= 1
        for i in num2:
            n2 += (ord(i) - 48) * 10 ** (len2 - 1)
            len2 -= 1
        return str(n1 + n2)

    def addStrings2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        68ms, beats: 30.57%
        """
        while len(num1) < len(num2):
            num1 = '0' + num1
        while len(num1) > len(num2):
            num2 = '0' + num2
        res = ''
        flag = 0
        for i in range(len(num1)-1, -1, -1):
            tmp = ord(num1[i]) + ord(num2[i]) - 2 * ord('0') + flag
            if tmp >= 10:
                flag = 1
                tmp = tmp % 10
            else:
                flag = 0
            res = str(tmp) + res
        if flag:
            res = '1' + res
        return res
