from functools import reduce
import re
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        son = []
        parent = []
        l = re.split(r'[/+]',expression)
        for i in range(len(l)):
            if len(son) == len(parent):
                son.append(int(l[i]))
            else:
                if l[i].isalnum():
                    parent.append(int(l[i]))
                else:
                    index = l[i].find('-')
                    parent.append(int(l[i][:index]))
                    son.append(int(l[i][index:]))
        m = reduce(lambda x,y:x*y,parent)
        for i in range(len(parent)):
            son[i] *= m // parent[i]
        s = sum(son)
        if s == 0:
            return '0/1'
        for i in [2,3,5,7]:
            while s%i==0 and m%i==0:
                s //= i
                m //= i
        return str(s) + '/' + str(m)
