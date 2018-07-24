import re


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        40ms beats
        """
        new_p = re.split(r'\W+', paragraph)
        tmp = {}
        for i in new_p:
            i = i.lower()
            if i in tmp:
                tmp[i] += 1
            else:
                tmp[i] = 1
        sorted_tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
        for item in sorted_tmp:
            if item[0] and item[0] not in banned:
                return item[0]
