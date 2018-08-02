from collections import Counter


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        36ms beats: 57.53%
        """
        if len(A) != len(B):
            return False
        dif = {}
        dif_count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                dif[A[i]] = B[i]
                dif_count += 1
                if dif_count > 2:
                    return False
        if dif_count == 2:
            for k, v in dif.items():
                if dif.get(v) != k:
                    return False
            return True
        elif dif_count == 1:
            return False
        else:
            count = Counter(A).most_common(1)
            if count and count[0][1] > 1:
                return True
            return False
