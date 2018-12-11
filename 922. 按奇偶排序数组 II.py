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
