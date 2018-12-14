class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        144ms, beats: 8.81%
        """
        s = set()
        for email in emails:
            flag = False
            new_email = ''
            for k, v in enumerate(email):
                if v == '@':
                    new_email += email[k:]
                    s.add(new_email)
                    break
                if flag:
                    continue
                else:
                    if v == '.':
                        continue
                    elif v == '+':
                        flag = True
                    else:
                        new_email += v
        return len(s)

    def numUniqueEmails2(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        44ms, beats: 90.42%
        """
        s = set()
        for email in emails:
            after_split = email.split('@')
            left, right = after_split[0], after_split[1]
            left = left.split('+')[0]
            left = left.replace('.', '')
            new = left + '@' + right
            s.add(new)
        return len(s)
