class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        340ms, beats 39.29%
        """
        if n <= 0:
            return 0
        s = '122'
        count = 1
        slow = 2
        while len(s) < n:
            pre = s[-1]
            if pre == '2':
                if n - len(s) == 1:
                    tail = '1' * int(s[slow])
                    count += 1
                else:
                    tail = '1' * int(s[slow])
                    count += int(s[slow])
            else:
                tail = '2' * int(s[slow])
            s += tail
            slow += 1
        return count

    def magicalString2(self, n):
        """
        :type n: int
        :rtype: int
        236ms, beats 50.00%
        """
        if n <= 0:
            return 0
        s = '122'
        slow = 2
        while len(s) < n:
            pre = s[-1]
            if pre == '2':
                tail = '1' * int(s[slow])
            else:
                tail = '2' * int(s[slow])
            s += tail
            slow += 1
        return s[:n].count('1')

    def magicalString3(self, n):
        """
        :type n: int
        :rtype: int
        96ms, beats 100.00%
        """
        nums, i = [1, 2, 2], 2
        while len(nums) < n:
            nums.append(3 - nums[-1])
            if nums[i] == 2:
                nums.append(nums[-1])
            i += 1
        return nums[:n].count(1)
