class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        56ms, beats 38.10%
        """
        deck.sort()
        res = []
        while deck:
            tmp = deck.pop()
            res = [tmp] + res[-1:] + res[:-1]
        return res
