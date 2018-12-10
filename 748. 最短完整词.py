class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        52ms, beats: 70.97%
        """
        def count_words(chars):
            d = {}
            for char in chars:
                char = char.lower()
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1
            return d
        license_plate = filter(lambda x: x.isalpha(), licensePlate)
        d_license = count_words(license_plate)
        words = sorted(words, key=lambda x: len(x))
        for word in words:
            flag = True
            d_word = count_words(word)
            for k, v in d_license.items():
                if d_word.get(k, 0) < v:
                    flag = False
                    break
            if flag:
                return word
