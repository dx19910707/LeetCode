class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        28ms, beats: 58.82%
        """
        def get_list(chars):
            char_list = []
            pre = None
            pre_count = 0
            for char in chars:
                if char == pre:
                    pre_count += 1
                else:
                    if pre and pre_count:
                        tmp = [pre, pre_count]
                        char_list.append(tmp)
                    pre = char
                    pre_count = 1
            char_list.append([pre, pre_count])
            return char_list

        name_list = get_list(name)
        typed_list = get_list(typed)
        for k, v in enumerate(name_list):
            try:
                if typed_list[k][0] != v[0] or typed_list[k][1] < v[1]:
                    return False
            except Exception:
                return False
        return True
