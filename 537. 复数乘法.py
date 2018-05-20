class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = a.split('+')
        a1,a2 = int(la[0]),int(la[1][:-1])
        lb = b.split('+')
        b1,b2 = int(lb[0]),int(lb[1][:-1])
        x = a1 * b1 - a2 * b2
        y = a1 * b2 + a2 * b1
        s = str(x) + '+' + str(y) + 'i'
        return s