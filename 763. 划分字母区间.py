class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []
        if S[-1] == S[0]:
            return [len(S)]
        rs = S[::-1]
        l = []
        index = len(S) - rs.find(S[0])
        def get_index(S,index):
            new_index = None
            for j in S[1:index]:
                if j in S[index:]:
                    new_index = len(S) - rs.find(j)
                    break
            if new_index:
                return get_index(S,new_index)
            return index
        index = get_index(S,index)
        l.append(index)
        l += self.partitionLabels(S[index:])
        return l
