class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        44ms, beats: 71.60%
        """
        o_target = ord(target)
        letters = sorted(letters)

        for letter in letters:
            o_letter = ord(letter)
            if o_letter > o_target:
                return chr(o_letter)

        return letters[0]
