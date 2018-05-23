class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        bin_list = [bin(x)[2:].zfill(8)[-8:] for x in data]
        i = 0
        while i < len(bin_list):
            if bin_list[i].startswith('0'):
                i += 1
                continue
            elif bin_list[i].startswith('110'):
                try:
                    if bin_list[i + 1].startswith('10'):
                        i += 2
                        continue
                    return False
                except:
                    return False
            elif bin_list[i].startswith('1110'):
                try:
                    if bin_list[i + 1][:2] == bin_list[i + 2][:2] == '10':
                        i += 3
                        continue
                    return False
                except:
                    return False
            elif bin_list[i][:5] == '11110':
                try:
                    if bin_list[i + 1][:2] == bin_list[i + 2][:2] == bin_list[i + 3][:2] == '10':
                        i += 4
                        continue
                    return False
                except:
                    return False
            else:
                return False
        return True
