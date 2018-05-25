class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        def i2r(num,t):
            if num < 1:
                return ''
            a = num % 10
            s = ''
            if 1 <= a <= 3:
                s = a * d[1*t]
            elif a == 4:
                s = d[1*t] + d[5*t]
            elif a == 5:
                s = d[5*t]
            elif 6 <= a <= 8:
                s = d[5*t] + (a-5) * d[1*t]
            elif a == 9:
                s = d[1*t] + d[10*t]
            t *= 10
            num //= 10
            return i2r(num,t) + s
        return i2r(num,1)