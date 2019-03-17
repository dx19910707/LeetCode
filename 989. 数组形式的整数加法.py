class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        代码很丑220ms, beats:95%
        """
        k_list = []
        while True:
            a = K % 10
            k_list.append(a)
            K = K // 10
            if K < 10:
                if K > 0:
                    k_list.append(K)
                break
        k_list.reverse()
        if len(A) < len(k_list):
            A, k_list = k_list, A
        tmp = 0
        i = -1
        while i > -(len(k_list)+1):
            t = k_list[i] + A[i] + tmp
            if t >= 10:
                tmp = 1
                t = t % 10
            else:
                tmp = 0
            A[i] = t
            i -= 1
        while tmp and i > -(len(A)+1):
            t = A[i] + tmp
            if t >= 10:
                tmp = 1
                t = t % 10
            else:
                tmp = 0
            A[i] = t
            i -= 1
        if tmp:
            A = [1] + A
        return A
