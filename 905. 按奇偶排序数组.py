class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        72ms, beats: 91.55%
        """
        even_list = []
        odd_list = []
        for i in A:
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
        even_list.extend(odd_list)
        return even_list
