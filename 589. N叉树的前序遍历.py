# Definition for a Node.
class Node(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        144ms beats: 95%
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        if root.children:
            for child in root.children:
                res += self.preorder(child)
        return res
