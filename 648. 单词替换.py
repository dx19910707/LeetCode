class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        dict = set(dict)
        def repalce(word,dict):
            for j in range(1,len(word)):
                if word[:j] in dict:
                    return word[:j]
            return word
        return ' '.join([repalce(word,dict) for word in words])