# Definition for a Node.
class Node(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        140ms beats: 97.67%
        """
        res = []
        if not root:
            return res
        if root.children:
            for child in root.children:
                res.extend(self.postorder(child))
        res.append(root.val)
        return res
