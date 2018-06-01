class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l = S.split()
        a = 'ma'
        for i in range(len(l)):
            a += 'a'
            if l[i][0] in vowels:
                l[i] += a
            else:
                l[i] = l[i][1:] + l[i][0] + a
        res = ' '.join(l)
        return res

