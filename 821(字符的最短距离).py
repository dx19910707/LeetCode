class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        l = []
        pre_index = None
        next_index = S.find(C)
        while True:
            if pre_index is None:
                for i in range(0,next_index+1):
                    l.append(next_index-i)
            else:
                for i in range(pre_index+1,next_index+1):
                    l.append(min(abs(next_index - i), abs(i - pre_index)))
            pre_index = next_index
            if S[next_index+1:].find(C) == -1:
                break
            next_index += S[next_index + 1:].find(C) + 1
        for i in range(len(S[next_index+1:])):
            l.append(i+1)
        return l

s = 'baab'
c = 'b'
print(Solution().shortestToChar(s,c))
print(len(s))
