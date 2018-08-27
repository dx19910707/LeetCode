# Definition for a Node.
class Node(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        172ms beats: 67.86%
        """
        res = []
        if not root:
            return res
        current_level = [root]
        while current_level:
            tmp = []
            next_level = []
            for current_root in current_level:
                tmp.append(current_root.val)
                if current_root.children:
                    next_level.extend(current_root.children)
            res.append(tmp)
            current_level = next_level
        return res
