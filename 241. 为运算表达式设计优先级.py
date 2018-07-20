import operator


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        36ms beat 88%
        """
        def dfs(input):
            li = []
            if not input.isalnum():
                for i in range(len(input)):
                    if input[i] in operators:
                        li += (dfs2(input[:i], operators[input[i]], input[i+1:]))
            else:
                li.append(int(input))
            return li

        def dfs2(left, op, right):
            result = []
            x_list = dfs(left)
            y_list = dfs(right)

            for x in x_list:
                for y in y_list:
                    result.append(op(x, y))
            return result

        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

        res = []
        if input.isalnum():
            res.append(int(input))
        else:
            res = dfs(input)
        return res
