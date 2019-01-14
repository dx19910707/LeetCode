class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        32ms, beats: 48.72%
        """
        def f(x, y, i, j, bound, l):
            if x ** i + y ** j > bound:
                return
            l.add(x ** i + y ** j)
            if x > 1:
                f(x, y, i + 1, j, bound, l)
            if y > 1:
                f(x, y, i, j + 1, bound, l)
        i = j = 0
        seen = set()
        f(x, y, i, j, bound, seen)
        return list(seen)


s = Solution()
a = 1
b = 2
bo = 100
r = s.powerfulIntegers(a, b, bo)
print(r)
