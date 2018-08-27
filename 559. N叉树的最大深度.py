# Definition for a Node.
class Node(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: List[int]
        132ms beats: 84.62%
        """
        if not root:
            return 0
        depth = 0
        current_level = [root]
        while current_level:
            depth += 1
            next_level = []
            for current_root in current_level:
                if current_root.children:
                    next_level.extend(current_root.children)
            current_level = next_level
        return depth
