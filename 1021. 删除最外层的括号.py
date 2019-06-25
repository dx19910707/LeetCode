class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = left = right = tmp = 0
        lens = len(S)
        res = ""
        while i < lens:
            if left > 0 and left == right:
                res += S[tmp:i][1:-1]
                tmp = i
            if S[i] == '(':
                left += 1
            else:
                right += 1
            i += 1
        res += S[tmp+1:-1]
        return res
