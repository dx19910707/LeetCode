class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab = {}
        for i in (a+b for a in A for b in B):
            if i in ab:
                ab[i] += 1
            else:
                ab[i] = 1
        return sum(ab.get(-(c+d),0) for c in C for d in D)

    def fourSumCount2(self, A, B, C, D):
        def f(list1, list2):
            res = {}
            for i in list1:
                for j in list2:
                    if i + j in res:
                        res[i + j] += 1
                    else:
                        res[i + j] = 1
            return res
        def f2(d1,d2):
            res = 0
            for k in d1.keys():
                if 0 - k in d2.keys():
                    res += d1[k]*d2[0 - k]
            return  res
        d1 = f(A, B)
        d2 = f(C, D)
        res = f2(d1,d2)
        return res