class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words,key=len,reverse=True)
        def judge(word1,word2):
            for k in word1:
                if k in word2:
                    return False
            return True
        i = 0
        res = 0
        while i < len(words)-1:
            if len(words[i]) * len(words[i+1]) < res:
                break
            for word in words[i+1:]:
                flag = judge(word,words[i])
                if flag:
                    res = max(res,len(word) * len(words[i]))
            i += 1
        return res