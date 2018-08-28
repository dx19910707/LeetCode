class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        40ms bests:92.39%
        """
        change = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if change[5] == 0:
                    return False
                change[5] -= 1
                change[10] += 1
            else:
                if change[10] == 0:
                    if change[5] < 3:
                        return False
                    else:
                        change[5] -= 3
                else:
                    if change[5] == 0:
                        return False
                    else:
                        change[10] -= 1
                        change[5] -= 1
        return True
