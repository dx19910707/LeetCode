class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        44ms, beats:87.94%
        """
        str = str.strip()
        num_str = ''
        flag = True
        has_flag = False
        for i in str:
            if i == '+':
                if has_flag:
                    break
                else:
                    has_flag = True
            elif i == '-':
                if has_flag:
                    break
                else:
                    flag = False
                    has_flag = True
            elif i.isnumeric():
                num_str += i
                has_flag = True
            else:
                if not num_str:
                    return 0
                break

        if not num_str:
            return 0

        if flag is False:
            num = -int(num_str)
            if num < -2147483648:
                return -2147483648
        else:
            num = int(num_str)
            if num > 2147483647:
                return 2147483647

        return num


a = "2-1"
s = Solution()
r = s.myAtoi(a)
print(r)
