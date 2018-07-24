class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        64ms beats 71.74%
        """
        d = {}
        for i in words:
            if len(i) in d:
                d[len(i)].append(i)
            else:
                d[len(i)] = [i]
        words_list = sorted(d.items(), key=lambda x: x[0])
        words_list = [x[1] for x in words_list]
        for i in range(len(words_list) - 1):
            tmp = []
            for j in words_list[i+1]:
                if j[:-1] not in words_list[i]:
                    tmp.append(j)
            for x in tmp:
                words_list[i+1].remove(x)
            if not words_list[i+1]:
                return min(words_list[i])
        return min(words_list[-1])
