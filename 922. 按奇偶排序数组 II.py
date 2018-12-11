class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        172ms, beats: 95.80%
        """
        copy_a = [0] * len(A)
        even_index, odd_index = 0, 1
        for i in A:
            if i % 2 == 0:
                copy_a[even_index] = i
                even_index += 2
            else:
                copy_a[odd_index] = i
                odd_index += 2
        return copy_a

    def sortArrayByParityII2(self, A):
        # 不需要多余的空间，180ms
        even, odd = 0, 1
        while even < len(A) and odd < len(A):
            if A[even] % 2 != 0:
                A[even], A[odd] = A[odd], A[even]
                odd += 2
            else:
                even += 2
        return A

