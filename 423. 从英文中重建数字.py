class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # a = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
        # d = {'o': 1240,
        #      'n': 179,
        #      'e': 1357890,
        #      't': 238,
        #      'w': 2,
        #      'h': 38,
        #      'r': 340,
        #      'u': 4,
        #      'i': 5689,
        #      'v': 57,
        #      'x': 6,
        #      's': 67, }
        #
        # z - 0
        # w - 2
        # u - 4
        # x - 6
        # s - 7(减去x)
        # r - 3(减去z, u)
        # o - 1(减去z, w, u)
        # v - 5(减去s)
        # n - 9(减去s, o)
        # i - 8(减去v, x, n)
        res = ''
        z = s.count('z')
        w = s.count('w')
        u = s.count('u')
        x = s.count('x')
        s1 = s.count('s')
        r = s.count('r')
        o = s.count('o')
        v = s.count('v')
        n = s.count('n')
        i = s.count('i')
        if z > 0:
            res += '0' * z
            r -= z
            o -= z
        if w > 0:
            res += '2' * w
            o -= w
        if u > 0:
            res += '4' * u
            r -= u
            o -= u
        if x > 0:
            res += '6' * x
            s1 -= x
            i -= x
        if s1 > 0:
            res += '7' * s1
            v -= s1
            n -= s1
        if r > 0:
            res += '3' * r
        if o > 0:
            res += '1' * o
            n -= o
        if v > 0:
            res += '5' * v
            i -= v
        if n > 0:
            res += '9' * (n//2)
            i -= n//2
        if i > 0:
            res += '8' * i
        res = ''.join(sorted(res))
        return res
