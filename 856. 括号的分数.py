class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        28ms, beats 56.76%
        """
        S += '('
        left = 0
        count = 0
        flag = False
        res = 0
        for i in S:
            if i == '(':
                if flag:
                    if left:
                        count += left
                    res = res + 2 ** (count-1)
                    count = 0
                    flag = False
                left += 1
            else:
                left -= 1
                count += 1
                flag = True
        return res
